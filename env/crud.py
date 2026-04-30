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

    #Read
    def read_acoes():
        cmd_select = "SELECT ticker, nome_empresa, setor, preco, data_cotacao FROM acoes_b3;"
        cursor.execute(cmd_select)
        acoes = cursor.fetchall()
        for acao in acoes:
            print(acao)
        return acoes
    
    #Update
    def update_acoes(ticker, novo_preco):
        cmd_update = f"UPDATE acoes_b3 SET preco = {novo_preco} WHERE ticker = '{ticker}';"
        cursor.execute(cmd_update)
        connection.commit()
        print("Os dados foram atualizados!")

    #Delete
    def delete_acoes(ticker):
        cmd_delete = f"DELETE FROM acoes_b3 WHERE ticker = '{ticker}';"
        cursor.execute(cmd_delete)
        connection.commit()
        print("Os dados foram deletados!")

    #Exemplos de uso

    #insert
    #insert_acoes("PETR4", "Petrobras", "Petróleo", 28.50, "2024-06-01")

    #read
    #read_acoes()

    #update
    #update_acoes("PETR4", 30.00)

    #delete
    #delete_acoes("PETR4")

    #desconectar do banco de dados
    disconnect(connection)

if __name__ == "__main__":
    main()