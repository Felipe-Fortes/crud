import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error

load_dotenv()

password = os.getenv("password")

#funcão para conectar ao banco de dados
def connect():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password=password,
            host="localhost",
            port="5432",
            database="acoes"
        )

        print("Boa nerdola conseguiu se conectar ao banco de dados!")

        return connection
    except (Exception, Error) as error:
        print("Erro ao conectar com o banco de dados:", error)

#funcão para desconectar do banco de dados
def disconnect(connection):
    if connection:
        connection.close()
        print("Conexão com o banco de dados fechada.")