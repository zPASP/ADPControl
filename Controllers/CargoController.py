import services.database as db
import models.cargo as cargo
import pandas as pd

def Incluir(cargo):
    cargo_id = ""
    try:
        print('------------')
        database = db.Database()
        database.connect()
        add_cargo = ("INSERT INTO cargo "
                        "(id, nome, descricao)"
                        "VALUES (%s ,%s ,%s)")
        data_cargo = (  cargo.id, 
                        cargo.nome, 
                        cargo.descricao )
        resultado, cargo_id = database.execute_query(add_cargo, data_cargo)
        print ('CADASTRO DO CARGO REALIZADO')

        print(f'Codigo Interno do cargo = {cargo_id}')
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        database.disconnect()
    return cargo_id

def lojaExiste(cnpj):
    try:
        print('------------')
        database = db.Database()
        database.connect()
        verifica = ("SELECT cnpj FROM loja WHERE cnpj = %s")
        params = (cnpj,)
        resultado = database.execute_query_one(verifica, params)
        print('RESULTADO CNPJ:', resultado)
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        database.disconnect()
    return resultado

def listaLoja():
    try:
        print('------------')
        database = db.Database()
        database.connect()
        query = ("SELECT * FROM loja")
        resultado, id= database.view_table(query)
        df_lojas = pd.DataFrame(resultado)
        df_lojas['telefone'] = df_lojas['telefone'].astype(str)
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        database.disconnect()
    return df_lojas

def Excluir(cnpj, idEndereco):
    try:
        print('------------')
        queryExcluirEndereco = "DELETE FROM endereco WHERE id = (%s) "
        queryExcluirLoja = "DELETE FROM loja WHERE cnpj = (%s) "
        database = db.Database()
        database.connect()
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        database.disconnect()

