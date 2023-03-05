import streamlit as st
import models.loja as loja



def inicio():
    col_voltar, col_titulo, col_top_vazio = st.columns((1.3,2,0.5), gap= "large")

    if col_voltar.button("◀ **VOLTAR**"):
        st.session_state['pagina_atual'] = 'inicio'
        st.experimental_rerun()
    col_titulo.title('CADASTRAR LOJA')

    #informações da loja
    ## CNPJ, nome, dd, telefone

