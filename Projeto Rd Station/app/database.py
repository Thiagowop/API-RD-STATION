
import pyodbc
from flask import current_app as app

# Detalhes de conexão ao banco de dados
db_server = 'servidor'
db_database = 'database'  
db_username = 'usuario'
db_password = 'senha'

def connect_to_database():
    try:
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={db_server};DATABASE={db_database};UID={db_username};PWD={db_password}'
        connection = pyodbc.connect(connection_string)
        app.logger.info("Conexão ao banco de dados bem-sucedida")
        return connection
    except Exception as e:
        app.logger.error(f"Falha ao conectar ao banco de dados: {e}")
        return None

def extract_data_from_database():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM customers c JOIN companies co ON c.company_id = co.id')
            data = cursor.fetchall()

            extracted_data = []
            for row in data:
                customer_data = {
                    'id': row[0],
                    'nome': row[1],
                    'email': row[2],
                    'telefone': row[3],
                    'cargo': row[4],
                    'company_id': row[5]
                }

                company_data = {
                    'id': row[5],
                    'nome': row[6],
                    'segmento': row[7],
                    'segmento_secundario': row[8]
                }

                extracted_data.append({
                    'cliente': customer_data,
                    'empresa': company_data
                })

            return extracted_data
        except Exception as e:
            app.logger.error(f"Falha ao extrair dados do banco de dados: {e}")
            return None
    else:
        return None
