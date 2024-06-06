from flask import Flask,  render_template, request, redirect, session, flash, url_for, json
from modelos.cad_produto import Cadastrar_produto
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

uri = "mongodb+srv://henriquefeitosa:12345@cluster-pipiline.gh2pwzy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-pipiline"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["db_produtos"]
collection = db["produtos"]
items_collection = db["items"]
preparacao_collection = db["preparacao"]

app = Flask(__name__)
app.secret_key = 'impacta'

@app.get('/')
def inicio():
    return render_template('tela_inicial.html', titulo = 'Bem Vindo ao Cardapio Digital' ) 

@app.get('/cadastrar')
def cadastrar():
    return render_template('cad_produto.html', titulo = 'Cadastro de Produtos' )

@app.route('/form_cadastrar', methods=['POST'] )
def form_cadastrar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    preco = request.form['preco']
    produto = {"produto": nome, "valor": preco, "categoria": categoria}
    collection.insert_one(produto)
    return redirect(url_for('cadastrar'))

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Tela de Login')
    
@app.route('/autenticar', methods=['POST'])
def autenticar():
    if '123456' == request.form['password']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect(url_for('inicio'))
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('inicio'))
   
@app.get('/cadastrados')
def cadastrados():
    return render_template('cadastrados.html', titulo = 'Cardapio', exibe = collection.find())

@app.route('/form_pedido', methods=['POST'])
def form_pedido():
    selected_ids = request.form.getlist('items_selecionados')
    selected_items = [collection.find_one({"_id": ObjectId(item_id)}) 
                      for item_id in selected_ids]
    items_collection.insert_many(selected_items)
    return redirect(url_for('cadastrados'))

@app.route('/deletar_item', methods=['POST'])
def deletar_item():
    items_collection.delete_many({})
    return redirect(url_for('pedido'))

@app.get('/pedido')
def pedido():
    items = items_collection.find()
    total_items = sum(float(item["valor"]) for item in items)
    total_formatado = f"R$ {total_items:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return render_template('pedido.html', titulo = 'Área do Pedido', items = items_collection.find(), total_items = total_formatado)
    
@app.get('/finalizar')
def finalizar():
    return render_template('finalizar_pedido.html', titulo = 'Preparação', preparacao = preparacao_collection.find())

@app.route('/preparar', methods=['POST'])
def preparar():
    selected_items = list(items_collection.find({}))
    preparacao_collection.insert_many(selected_items)
    items_collection.delete_many({})
    return redirect(url_for('pedido'))

if __name__ == '__main__':
    app.run(debug=True)
