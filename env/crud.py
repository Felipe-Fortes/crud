from database import connect, disconnect

def main():
    connection = connect()
    cursor = connection.cursor()

    #Create
    def insert_acoes(ticker, nome_empresa, setor, preco, data_cotacao):
        cmd_insert = "INSERT INTO acoes_b3 (ticker, nome_empresa, setor, preco, data_cotacao) VALUES (%s, %s, %s, %s, %s);"
        values = (ticker, nome_empresa, setor, preco, data_cotacao)
        cursor.execute(cmd_insert, values)
        connection.commit()
        print("Os dados foram inseridos!")