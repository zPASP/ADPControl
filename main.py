import streamlit as st
import pages.menu.inicio as inicio
import pages.funcionario.cadastrar as cadFuncionario
import pages.ponto.bater_ponto as baterPonto
import pages.loja.cadastrar as cadLoja
import pages.loja.visualizar as verLoja

#st.write(st.session_state)

if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = 'inicio'
    st.experimental_rerun()

match st.session_state['pagina_atual']:
    case 'inicio':
        inicio.inicio()
    case 'cadastrar_funcionario':
        cadFuncionario.inicio()
    case 'bater_ponto':
        baterPonto.inicio()
    case 'cadastrar_loja':
        cadLoja.inicio()
    case 'visualizar_loja':
        verLoja.inicio()

# import models.endereco as endereco
# import services.database as db

# def Incluir(endereco):
#     add_endereco = ("INSERT INTO endereco "
#                     "(id, rua, numero, bairro, cidade, estado, cep)"
#                     "VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s )")
#     data_endereco = (endereco.id, 
#                      endereco.rua, 
#                      endereco.numero, 
#                      endereco.bairro, 
#                      endereco.cidade, 
#                      endereco.estado,  
#                      endereco.cep)
#     db.cursor.execute(add_endereco, data_endereco)

#     db.cnx.commit()
#     print ('CADASTRO DE ENDEREÇO REALIZADO')

#     db.cursor.execute("SELECT LAST_INSERT_ID()")
#     endereco_id = db.cursor.fetchone()[0]

#     print(f'Numero do ID do endereço = {endereco_id}')

#     db.cursor.close()
#     return endereco_id


# teste = endereco.Endereco(0,'RUA 1', '99', 'Bairro don', 'Rio Grande', 'RS', '99999999')
# retorno = Incluir(teste)
# print(retorno)

