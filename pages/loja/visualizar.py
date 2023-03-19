import streamlit as st
import models.loja as loja
import models.endereco as endereco
import Controllers.cepValidador as Cep
import Controllers.EnderecoController as EnderecoController
import Controllers.LojaController as LojaController
import utils

@st.cache_resource
def funListaLoja ():
    return LojaController.listaLoja()

def inicio():
    validador = True

    col_voltar, col_titulo, col_top_vazio = st.columns((.6,2,0.1), gap= "large")

    if col_voltar.button("◀ **VOLTAR**"):
        st.session_state['pagina_atual'] = 'inicio'
        st.experimental_rerun()
    col_titulo.title('VISUALIZAR LOJA(s)')

    st.subheader('Informações da Loja:')

    lojas = funListaLoja()
    # CSS to inject contained in a string
    hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

        # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    lojas_mostrar = lojas[['cnpj', 'nome', 'ddd', 'telefone']]

    st.table(lojas_mostrar)

    if 'statusBt' not in st.session_state:
        st.session_state['statusBt'] = False


    botao = st.button('TESTE', disabled=st.session_state['statusBt'])

    if botao:
        st.session_state['statusBt'] = not st.session_state['statusBt']
        st.experimental_rerun()