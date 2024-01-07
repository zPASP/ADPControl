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
        # st.rerun()
        pass

    #GERENCIAMENTO LOJA
    Loja_form = st.form("Loja_form")
    Loja_form.write(centralizarPalavra('GERENCIAMENTO LOJA'), unsafe_allow_html=True)
    col_verLoja, col_cadLoja = Loja_form.columns(2)
    
    if col_verLoja.form_submit_button('VISUALIZAR LOJA', use_container_width=True):
        st.session_state['pagina_atual'] = 'visualizar_loja'
        st.rerun()

    if col_cadLoja.form_submit_button('CADASTRAR LOJA', use_container_width=True):
        st.session_state['pagina_atual'] = 'cadastrar_loja'
        st.rerun()

    ##GERENCIAMENTO FUNCIONARIOS
    func_form = st.form("funcionario_form")
    func_form.write(centralizarPalavra('GERENCIAMENTO DE FUNCIONARIOS'), unsafe_allow_html=True)
    col_verFunc, col_cadfunc = func_form.columns(2)

    if col_verFunc.form_submit_button('VISUALIZAR FUNCIONARIO', use_container_width=True, disabled = True):
        st.session_state['pagina_atual'] = 'visualizar_funcionario'
        st.rerun()

    if col_cadfunc.form_submit_button('CADASTRAR FUNCIONARIO', use_container_width=True):
        st.session_state['pagina_atual'] = 'cadastrar_funcionario'
        st.rerun()


    ##GERENCIAMENTO CARGOS
    func_form = st.form("cargo_form")
    func_form.write(centralizarPalavra('GERENCIAMENTO DE CARGOS'), unsafe_allow_html=True)
    col_verFunc, col_cadfunc = func_form.columns(2)

    if col_verFunc.form_submit_button('VISUALIZAR CARGO', use_container_width=True, disabled = True):
        st.session_state['pagina_atual'] = 'visualizar_cargo'
        st.rerun()

    if col_cadfunc.form_submit_button('CADASTRAR CARGO', use_container_width=True):
        st.session_state['pagina_atual'] = 'cadastrar_cargo'
        st.rerun()


    ##
    if st.button('EDITAR FUNCIONARIO', disabled = True):
        st.session_state['pagina_atual'] = 'cadastrar'
        st.rerun()

    if st.button('VISUALIZAR PONTO', disabled = True):
        st.session_state['pagina_atual'] = 'cadastrar'
        st.rerun()
    