from flask import Flask,  render_template, request, redirect, session, flash, url_for
from modelos.cad_produto import Cadastrar_produto
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://henriquefeitosa:12345@cluster-pipiline.gh2pwzy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-pipiline"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["db_produtos"]
collection = db["produtos"]

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
    '''produto = Cadastrar_produto(nome, categoria, preco)
    Cadastrar_produto.cadastrados.append(produto)'''
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
    return render_template('cadastrados.html', titulo = 'Cadastrados', exibe = Cadastrar_produto.cadastrados)

@app.get('/carrinho')
def carrinho():
    return render_template('carrinho.html', titulo = 'Em desenvolvimento')
    
@app.get('/finalizar')
def finalizar():
    return render_template('finalizar_pedido.html', titulo = 'Em desenvolvimento')

if __name__ == '__main__':
    app.run(debug=True)
