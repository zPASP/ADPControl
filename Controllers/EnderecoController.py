import services.database as db
import models.endereco as endereco

def Incluir(endereco):
    try:
        print('------------')
        print('1')
        database = db.Database()
        print('2')
        database.connect()
        add_endereco = ("INSERT INTO endereco "
                        "(id, rua, numero, bairro, cidade, estado, cep)"
                        "VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s )")
        data_endereco = (endereco.id, 
                        endereco.rua, 
                        endereco.numero, 
                        endereco.bairro, 
                        endereco.cidade, 
                        endereco.estado,  
                        endereco.cep)
        print('3')
        resultado = database.execute_query(add_endereco, data_endereco)
        print('4')
        resultado, endereco_id = resultado

        print ('CADASTRO DE ENDEREÇO REALIZADO')

        print(f'Numero do ID do endereço = {endereco_id}')
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        database.disconnect() # desconectar do banco de dados
        # db.cursor.close()
        # db.cnx.close()
    return endereco_id



def Incluir1(endereco):
    try:
        # db.cnx.cursor()
        add_endereco = ("INSERT INTO endereco "
                        "(id, rua, numero, bairro, cidade, estado, cep)"
                        "VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s )")
        data_endereco = (endereco.id, 
                        endereco.rua, 
                        endereco.numero, 
                        endereco.bairro, 
                        endereco.cidade, 
                        endereco.estado,  
                        endereco.cep)
        db.cursor.execute(add_endereco, data_endereco)

        db.cnx.commit()
        print ('CADASTRO DE ENDEREÇO REALIZADO')

        db.cursor.execute("SELECT LAST_INSERT_ID()")
        endereco_id = db.cursor.fetchone()[0]

        print(f'Numero do ID do endereço = {endereco_id}')
    finally:
        pass
        # db.cursor.close()
        # db.cnx.close()
    return endereco_id


#teste = endereco.Endereco(0,'RUA 1', '99', 'Bairro don', 'Rio Grande', 'RS', '99999999', 0, 0)
#retorno = Incluir(teste)
#print(retorno)

