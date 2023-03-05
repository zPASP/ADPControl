import streamlit as st
import models.loja as loja
import utils



def inicio():
    validador = True

    col_voltar, col_titulo, col_top_vazio = st.columns((.6,2,0.1), gap= "large")

    if col_voltar.button("◀ **VOLTAR**"):
        st.session_state['pagina_atual'] = 'inicio'
        st.experimental_rerun()
    col_titulo.title('CADASTRAR LOJA')

    st.subheader('Informações da Loja:')

    #informações da loja
    ## CNPJ, nome, dd, telefone

    nome = st.text_input('Nome:', placeholder= 'Loja principal LTDA.' )
    col_cnpj, col_ddd, col_telefone  = st.columns((2,0.6,2))
    cnpj = col_cnpj.text_input('CNPJ:', max_chars=14)
    ddd = col_ddd.text_input('DDD:', max_chars=2, help='Somente Numeros')
    telefone = col_telefone.text_input('Celular:', max_chars=9, help='INSIRA O NUMERO DO FUNCIONARIO')
    

    col_voltar2, col_enviar, col_limpar, col_2 = st.columns((1,2,2,1))
    #voltar2 = col_voltar2.button("◀ **VOLTAR**")
    enviar = col_enviar.button("CADASTRAR LOJA", type='primary', use_container_width=True)
    limpar = col_limpar.button("LIMPAR CADASTRO", type='secondary', use_container_width=True)

    if enviar:
        #validador do nome
        if nome == "":
            st.warning('NOME - não pode ficar em branco')
            validador = False

        #validador do CNPJ
        if cnpj == "":
            st.warning('CNPJ - Não pode ficar em branco')
            validador = False
        elif len(cnpj) < 14:
            st.warning('CNPJ - Invalido')
            validador = False
        

        #validador telefone
        if ddd == "" or telefone == "":
            st.warning('DDD / CELULAR - Não pode ficar em branco')
            validador = False
        elif len(ddd) < 2:
            st.warning('DDD - Invalido')
            validador = False
        elif len(telefone) < 9:
            st.warning('CELULAR - Digite um numero valido')
            validador = False


        if validador:
            st.success('CADASTRO REALIZADO COM SUCESSO')
