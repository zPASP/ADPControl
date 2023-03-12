import streamlit as st
import models.loja as loja
import models.endereco as endereco
import Controllers.cepValidador as Cep
import Controllers.EnderecoController as EnderecoController
import Controllers.LojaController as LojaController
import utils



def inicio():
    validador = True

    col_voltar, col_titulo, col_top_vazio = st.columns((.6,2,0.1), gap= "large")

    if col_voltar.button("◀ **VOLTAR**"):
        st.session_state['pagina_atual'] = 'inicio'
        st.experimental_rerun()
    col_titulo.title('VISUALIZAR LOJA(s)')

    st.subheader('Informações da Loja:')

    lojas = LojaController.listaLoja()

    st.write(lojas)

    