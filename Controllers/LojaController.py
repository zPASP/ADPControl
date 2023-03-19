import services.database as db
import models.loja as loja
import pandas as pd

def Incluir(loja):
    try:
        print('------------')
        database = db.Database()
        database.connect()
        add_loja = ("INSERT INTO loja "
                        "(cnpj, nome, ddd, telefone, endereco_id)"
                        "VALUES (%s ,%s ,%s ,%s ,%s)")
        data_loja = (   loja.cnpj, 
                        loja.nome, 
                        loja.ddd, 
                        loja.telefone, 
                        loja.endereco_id)
        resultado = database.execute_query(add_loja, data_loja)
        loja_id = loja.cnpj
        print ('CADASTRO DA LOJA REALIZADO')

        print(f'Numero do CNPJ da LOJA = {loja_id}')
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        database.disconnect()
    return loja_id

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


