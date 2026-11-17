# import pyodbc

# # Configurando o endereço do seu banco local
# dados_conexao = (
#     "Driver={ODBC Driver 17 for SQL Server};"
#     "Server=localhost\\SQLEXPRESS;"
#     "Database=BancoTreino;"
#     "Trusted_Connection=yes;"
#     "TrustServerCertificate=yes;"
# )

# # Tentando abrir a porta do banco
# conexao = pyodbc.connect(dados_conexao)
# print("Conexão realizada com sucesso! O Python entrou no banco!")
import pandas as pd
import pyodbc

# 1. Lê a planilha do Excel
tabela = pd.read_excel('clientes_novos.xlsx', engine='openpyxl')

# 2. Abre a porta do banco de treino
dados_conexao = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=BancoTreino;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

# 3. Passa linha por linha da planilha e envia para o SQL
for index, linha in tabela.iterrows():
    cursor.execute("""
        INSERT INTO Clientes_Excel (Nome, Idade, Profissao, Renda)
        VALUES (?, ?, ?, ?)
    """, linha['Nome'], linha['Idade'], linha['Profissao'], linha['Renda'])

# 4. Confirma e salva tudo no banco
conexao.commit()
print("Sucesso! Todos os dados do Excel foram enviados para o SQL Server!")

