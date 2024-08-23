# Integração de Banco de Dados com RD Station

Este projeto é uma aplicação Flask que conecta-se a um banco de dados SQL Server, extrai dados de clientes e empresas, e os integra na plataforma RD Station Marketing via API. A aplicação foi projetada para ser modular e fácil de manter, com o uso de boas práticas de organização de código.

## Funcionalidades

- **Extração de Dados**: Conecta-se a um banco de dados SQL Server e extrai informações de clientes e empresas.
- **Transformação de Dados**: Transforma os dados extraídos em um formato compatível com a API do RD Station Marketing.
- **Integração com RD Station**: Envia os dados transformados para a API do RD Station Marketing, criando ou atualizando contatos e empresas.

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:


## Pré-requisitos

- Python 3.x
- SQL Server
- RD Station Marketing API Key

## Instalação

 **Clone o repositório:**

Instale as dependências:
pip install -r requirements.txt

Execute a aplicação:


python run.py