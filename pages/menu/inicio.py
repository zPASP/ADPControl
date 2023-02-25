import streamlit as st

def inicio():
    st.title('ADPControl')
    st.subheader('Escolha a opção desejada')

    if st.button('BATER PONTO'):
        st.session_state['pagina_atual'] = 'bater_ponto'
        st.experimental_rerun()
    
    if st.button('CADASTRAR FUNCIONARIO'):
        st.session_state['pagina_atual'] = 'cadastrar'
        st.experimental_rerun()

    if st.button('EDITAR FUNCIONARIO', disabled = True):
        st.session_state['pagina_atual'] = 'cadastrar'
        st.experimental_rerun()

    if st.button('VISUALIZAR PONTO', disabled = True):
        st.session_state['pagina_atual'] = 'cadastrar'
        st.experimental_rerun()
    