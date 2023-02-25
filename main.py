import streamlit as st
import pages.menu.inicio as inicio
import pages.funcionario.cadastrar as cadFuncionario
import pages.funcionario.bater_ponto as baterPonto


if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = 'inicio'
    st.experimental_rerun()

match st.session_state['pagina_atual']:
    case 'inicio':
        inicio.inicio()
    case 'cadastrar':
        cadFuncionario.inicio()
    case 'bater_ponto':
        baterPonto.inicio()

