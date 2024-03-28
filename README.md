# Cardápio Digital

Este é um projeto de aplicação web em Python utilizando o framework Flask, que visa criar um cardápio digital para gerenciar produtos e pedidos.

## Requisitos

- Python 3.x
- Flask
- pymongo

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. Instale as dependências:

    ```bash
    pip install flask pymongo
    ```

3. Configure o MongoDB:
   
   - Crie uma conta no MongoDB Atlas (https://www.mongodb.com/cloud/atlas).
   - Crie um cluster e configure as credenciais de acesso.
   - Substitua a variável `uri` no arquivo `app.py` com a URI de conexão fornecida pelo MongoDB Atlas.

## Execução

Execute a aplicação com o seguinte comando:

```bash
python app.py
```

Acesse a aplicação em um navegador web utilizando o endereço `http://localhost:5000`.

## Funcionalidades

- **Cadastro de Produtos**: Permite cadastrar novos produtos no cardápio.
- **Login**: Permite acesso ao cardápio digital com autenticação.
- **Visualização de Produtos Cadastrados**: Exibe os produtos cadastrados no cardápio.
- **Carrinho de Compras**: Funcionalidade em desenvolvimento para adicionar produtos ao carrinho.
- **Finalizar Pedido**: Funcionalidade em desenvolvimento para finalizar um pedido.

## Estrutura do Projeto

- `app.py`: Arquivo principal contendo a lógica da aplicação.
- `templates/`: Diretório contendo os templates HTML para renderização das páginas.
- `modelos/`: Diretório contendo as classes de modelo, como `Cadastrar_produto`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções ou novas funcionalidades.

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
