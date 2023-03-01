import streamlit as st

def centralizarPalavra(texto):
    return f"<p style='text-align: center;'>{texto}</p>"

def inicio():
    st.title('ADPControl')
    # st.subheader('Escolha a opção desejada')

    col_dir, col_ponto, col_esq = st.columns(3)

    #PONTO ELETRONICO
    ponto_form = col_ponto.form("ponto_form")
    ponto_form.write(centralizarPalavra('PONTO ELETRONICO'), unsafe_allow_html=True)
    if ponto_form.form_submit_button('BATER PONTO', type='primary',use_container_width=True):
        # st.session_state['pagina_atual'] = 'bater_ponto'
        # st.experimental_rerun()
        pass

    #GERENCIAMENTO LOJA
    Loja_form = st.form("Loja_form")
    Loja_form.write(centralizarPalavra('GERENCIAMENTO LOJA'), unsafe_allow_html=True)
    col_verLoja, col_cadLoja = Loja_form.columns(2)
    
    if col_verLoja.form_submit_button('VISUALIZAR LOJA', use_container_width=True, disabled = True):
        st.session_state['pagina_atual'] = 'cadastra_loja'
        st.experimental_rerun()

    if col_cadLoja.form_submit_button('CADASTRAR LOJA', use_container_width=True):
        st.session_state['pagina_atual'] = 'cadastra_loja'
        st.experimental_rerun()

    ##GERENCIAMENTO FUNCIONARIOS
    func_form = st.form("funcionario_form")
    func_form.write(centralizarPalavra('GERENCIAMENTO DE FUNCIONARIOS'), unsafe_allow_html=True)
    col_verFunc, col_cadfunc = func_form.columns(2)

    if col_verFunc.form_submit_button('VISUALIZAR LOJA', use_container_width=True, disabled = True):
        st.session_state['pagina_atual'] = 'cadastra_loja'
        st.experimental_rerun()

    if col_cadfunc.form_submit_button('CADASTRAR FUNCIONARIO', use_container_width=True):
        st.session_state['pagina_atual'] = 'cadastrar_funcionario'
        st.experimental_rerun()


    ##
    if st.button('EDITAR FUNCIONARIO', disabled = True):
        st.session_state['pagina_atual'] = 'cadastrar'
        st.experimental_rerun()

    if st.button('VISUALIZAR PONTO', disabled = True):
        st.session_state['pagina_atual'] = 'cadastrar'
        st.experimental_rerun()
    