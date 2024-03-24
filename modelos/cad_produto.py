class Cadastrar_produto:
    '''Este metodo realiza o processo de cadastro de produtos. '''
    
    cadastrados = [] 
    '''esta lista guarda os produtos cadastrados. '''
    
    def __init__(self, nome, categoria, valor):
        self.nome = nome
        self.categoria = categoria
        self.valor = float(valor)
        Cadastrar_produto.cadastrados.append(self)
          
    def __str__(self):
        return f'{self.nome} {self.categoria} {self.valor}' 
    '''Este metodo trasforma os objetos em string. '''