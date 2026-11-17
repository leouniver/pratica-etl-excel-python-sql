# pratica-etl-excel-python-sql  
# Prática de Automação de Dados (ETL): Excel, Python e SQL Server

Este repositório guarda um projeto prático desenvolvido para treinar a integração e o fluxo de dados (processo de **ETL**: Extração, Transformação e Carga) entre planilhas, código de automação e banco de dados relacional.

## Fluxograma do Projeto

![Fluxograma do Projeto ETL](fluxograma_etl.png)

## O que este projeto faz

1. **Extração (Excel):** Lê automaticamente os dados cadastrais de clientes a partir de uma planilha local (`clientes_novos.xlsx`).
2. **Processamento (Python):** Utiliza as bibliotecas `pandas` e `pyodbc` para estruturar as linhas e abrir a conexão segura com o banco de dados.
3. **Carga (SQL Server):** Insere cada registro da planilha diretamente dentro da tabela `Clientes_Excel` no SQL Server sem necessidade de digitação manual.

## Ferramentas Utilizadas

- **Python 3** (Automação e leitura de dados)
- **Pandas & OpenPyXL** (Manipulação de arquivos Excel)
- **PyODBC** (Conexão entre Python e banco de dados)
- **SQL Server & SSMS** (Armazenamento e estruturação da tabela)

## Estrutura dos Arquivos

- `automacao_banco.py`: Script principal em Python que realiza a leitura do Excel e o envio para o SQL.
- `clientes_novos.xlsx`: Planilha de exemplo utilizada como fonte de dados.
- `criar_tabela_excel.sql`: Script SQL utilizado para criar a estrutura da tabela de destino no banco.
- `fluxograma_etl.png`: Diagrama visual explicando o caminho dos dados.
