import streamlit as st
import models.cargo as cargo
import Controllers.CargoController as CargoController
import utils



def inicio():
    validador = True

    col_voltar, col_titulo, col_top_vazio = st.columns((.6,2,0.1), gap= "large")

    if col_voltar.button("◀ **VOLTAR**"):
        st.session_state['pagina_atual'] = 'inicio'
        st.rerun()
    col_titulo.title('CADASTRAR CARGO')

    st.subheader('Informações do cargo:')

    #informações do cargo

    nome = st.text_input('CARGO:', placeholder= 'Administrador' )
    descricao = st.text_area('Descricao:', max_chars=90)


    col_voltar2, col_enviar, col_limpar, col_2 = st.columns((1,2,2,1))
    #voltar2 = col_voltar2.button("◀ **VOLTAR**")
    enviar = col_enviar.button("CADASTRAR LOJA", type='primary', use_container_width=True, key='btnCadastrar', )
    limpar = col_limpar.button("LIMPAR CADASTRO", type='secondary', use_container_width=True)
    
    if enviar:
        #validador do nome
        if nome == "":
            st.warning('CARGO - Digite um cargo valido')
            validador = False

        #validador do CNPJ
        if descricao == "":
            st.warning('DESCRIÇÃO - Digite uma breve descrição do cargo')
            validador = False
        
        

        if validador:
            import time
            print ('-VALIDADOR-')
            barCadastro = st.progress(0, text="CADASTRO VALIDADO - Criando endereço")
            cargo_obj = cargo.Cargo(0,nome, descricao, 0, 0)

            time.sleep(1)
            barCadastro.progress(50,text="BANCO DE DADOS - Salvar Cargo")
            salvarCargo(cargo_obj)

            st.success('CADASTRO REALIZADO COM SUCESSO')

            barCadastro.progress(90,text=f"BANCO DE DADOS OK - REDIRECIONAR")
            totalDirecionar = 90
            for totalDirecionar in range(30):
                time.sleep(0.1)
                barCadastro.progress(totalDirecionar + 1, text=f"BANCO DE DADOS OK - REDIRECIONAR")
            barCadastro.progress(100,text=f"REDIRECIONANDO")
            time.sleep(.300)
            st.session_state['pagina_atual'] = 'inicio'
            st.rerun()

def salvarCargo(cargo):
    cargo_id = CargoController.Incluir(cargo)
    #print(loja_id)
    pass
