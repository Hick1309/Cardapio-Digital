# -*- coding: utf-8 -*-
from graphviz import Digraph

# Função para gerar o diagrama de casos de uso
def gerar_diagrama_de_casos_de_uso():
    use_case_diagram = Digraph(comment='Diagrama de Casos de Uso')

    # Definir o estilo dos nós e arestas
    use_case_diagram.attr('node', shape='ellipse', fontsize='12')
    use_case_diagram.attr('edge', fontsize='10')

    # Atores
    use_case_diagram.node('A', 'Funcionário', shape='box')

    # Casos de Uso
    use_case_diagram.node('UC1', 'Acessar Cardápio')
    use_case_diagram.node('UC2', 'Selecionar Produtos')
    use_case_diagram.node('UC3', 'Acessar Comanda')
    use_case_diagram.node('UC4', 'Tela de Preparo')

    # Conexões
    use_case_diagram.edge('A', 'UC1')
    use_case_diagram.edge('A', 'UC2')
    use_case_diagram.edge('A', 'UC3')
    use_case_diagram.edge('A', 'UC4')

    use_case_diagram.render('diagrama_de_casos_de_uso', format='png', cleanup=True)

# Função para gerar o diagrama de classes
def gerar_diagrama_de_classes():
    class_diagram = Digraph(comment='Diagrama de Classes')

    # Definir o estilo dos nós
    class_diagram.attr('node', shape='record', fontsize='12')

    # Classes e Atributos/Métodos
    class_diagram.node('Cardapio', '''{Cardapio|+ itens : list|+ exibirItens() : void\\l+ adicionarItem(item) : void\\l+ removerItem(item) : void}''')
    class_diagram.node('Produto', '''{Produto|+ nome : string\\l+ preco : float\\l+ descricao : string|+ atualizarPreco(preco) : void\\l+ atualizarDescricao(descricao) : void}''')
    class_diagram.node('Comanda', '''{Comanda|+ id : int\\l+ produtos : list\\l+ status : string|+ adicionarProduto(produto) : void\\l+ removerProduto(produto) : void\\l+ atualizarStatus(status) : void}''')
    class_diagram.node('Pedido', '''{Pedido|+ id : int\\l+ comanda : Comanda\\l+ status : string|+ iniciarPreparo() : void\\l+ finalizarPreparo() : void}''')
    class_diagram.node('Funcionario', '''{Funcionario|+ id : int\\l+ nome : string\\l+ cargo : string|+ acessarCardapio() : void\\l+ selecionarProdutos() : void\\l+ acessarComanda() : void\\l+ informarPedidoPronto() : void}''')

    # Relacionamentos
    class_diagram.edge('Cardapio', 'Produto', label='contém', arrowhead='none')
    class_diagram.edge('Comanda', 'Produto', label='contém', arrowhead='none')
    class_diagram.edge('Pedido', 'Comanda', label='associa-se a')
    class_diagram.edge('Funcionario', 'Pedido', label='prepara', arrowhead='none')

    class_diagram.render('diagrama_de_classes', format='png', cleanup=True)

# Gerar os diagramas
gerar_diagrama_de_casos_de_uso()
gerar_diagrama_de_classes()
