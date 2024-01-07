import services.database as db
import models.funcionario as funcionario

def Incluir(funcionario):
    try:
        print('------------')
        print('-CADASTRO FUNCIONARIO-')
        print(funcionario.endereco_id)
        database = db.Database()
        database.connect()
        add_funcionario = ("INSERT INTO funcionario "
                        "(cpf, nome, ddd, telefone, cargo_id, salario_base, endereco_id, loja_cnpj)"
                        "VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s, %s )")
        data_funcionario = (funcionario.cpf, 
                            funcionario.nome, 
                            funcionario.ddd, 
                            funcionario.telefone, 
                            funcionario.cargo_id, 
                            funcionario.salario_base,  
                            funcionario.endereco_id,
                            funcionario.loja_cnpj)
        print(data_funcionario)
        print("EXECUTE QUERY")
        resultado, funcionario_id = database.execute_query(add_funcionario, data_funcionario)
        print(resultado)
        print(f'Numero do ID do funcionario = {funcionario_id}')
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        pass
        #database.disconnect() # desconectar do banco de dados
    return funcionario_id








def Excluir(id):
    try: 
        print('------------')
        print(f'-EXCLUIR ENDEREÇO: {id}-')
        database = db.Database()
        database.connect()

        remover_endereco = ("DELETE FROM endereco "
                        "WHERE id"
                        "VALUES (%s)")
        resultado = database.execute_query_one(remover_endereco, id)
        print(f'ENDEREÇO EXCLUIDO: {id}')
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        database.disconnect()
    return resultado
        

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

