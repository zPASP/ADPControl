import services.database as db
import models.loja as loja

def Incluir(loja):
    try:
        # db.cnx.cursor()
        add_loja = ("INSERT INTO loja "
                        "(cnpj, nome, ddd, telefone, endereco_id)"
                        "VALUES (%s ,%s ,%s ,%s ,%s)")
        data_loja = (   loja.cnpj, 
                        loja.nome, 
                        loja.ddd, 
                        loja.telefone, 
                        loja.endereco_id)
        db.cursor.execute(add_loja, data_loja)

        db.cnx.commit()
        print ('CADASTRO DA LOJA REALIZADO')

        db.cursor.execute("SELECT LAST_INSERT_ID()")
        loja_id = db.cursor.fetchone()[0]

        print(f'Numero do ID da LOJA = {loja_id}')
    finally:
        pass
        # db.cursor.close()
        # db.cnx.close()
    return loja_id


# teste = endereco.Endereco(0,'RUA 1', '99', 'Bairro don', 'Rio Grande', 'RS', '99999999', 0, 0)
# retorno = Incluir(teste)
# print(retorno)

