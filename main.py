import streamlit as st
import pages.menu.inicio as inicio
import pages.funcionario.cadastrar as cadFuncionario
import pages.funcionario.bater_ponto as baterPonto
import pages.loja.cadastrar as cadLoja

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

