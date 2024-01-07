import streamlit as st
import Controllers.cepValidador as Cep
import models.endereco as endereco
import models.funcionario as funcionario
import Controllers.EnderecoController as EnderecoController
import Controllers.FuncionarioController as FuncionarioController


def inicio():
    validador = True

    col_voltar, col_titulo, col_top_vazio = st.columns((.6,2,0.1), gap= "large")

    if col_voltar.button("◀ **VOLTAR**"):
        st.session_state['pagina_atual'] = 'inicio'
        st.rerun()
    col_titulo.title('CADASTRAR FUNCIONARIO')


    st.subheader("Informações do Funcionario:")
    
    #INFORMAÇÕES FUNCIONARIO
    nome = st.text_input('Nome:', placeholder='Falano da silva')
    
    
    col_cpf, col_ddd, col_telefone  = st.columns((2,0.6,2))
    cpf = col_cpf.text_input('CPF :', max_chars=11)
    ddd = col_ddd.text_input('DDD:', max_chars=2)
    telefone = col_telefone.text_input('Celular:', max_chars=9, help='INSIRA O NUMERO DO FUNCIONARIO')
    
    col_salario, col_cargo ,  col_loja = st.columns(3)
    salario = col_salario.number_input('Salario:')
    cargo = col_cargo._selectbox('Cargo:', ('cargo1', 'cargo2'), help='Informe a qual cargo do funcionario')
    loja = col_loja._selectbox('Loja:', ('loja1', 'loja2'), help='Informe a qual loja o funcionario pertence')
    
    
    #INFORMAÇÕES ENDERECO
    st.write('')
    st.write("""
    - __Endereço:__
    """)
    
    col_cep, col_cidade, col_estado = st.columns(3)
    cep = col_cep.text_input('CEP', max_chars=8)

    if cep:
        cepValidado = Cep.validarcep(cep)
        #st.write(cepValidado)
        if not cepValidado:
            st.warning('DIGITE UM CEP VALIDO')
            validador = False
        else:
            
            col_rua, col_numero, col_bairro = st.columns((2,0.6,1.9))
            rua = col_rua.text_input('Rua:',cepValidado['logradouro'], disabled=True)
            numero = col_numero.text_input('Número:')
            bairro = col_bairro.text_input('Bairro:',cepValidado['bairro'], disabled=True)
            cidade = col_cidade.text_input('Cidade:',cepValidado['localidade'], disabled=True)
            estado = col_estado.text_input('Estado:',cepValidado['uf'], disabled=True)

    #verificador
    st.write("""
    """)
    col_voltar2, col_enviar, col_limpar, col_2 = st.columns((1,2,2,1))
    #voltar2 = col_voltar2.button("◀ **VOLTAR**")
    enviar = col_enviar.button("CADASTRAR FUNCIONARIO", type='primary')
    limpar = col_limpar.button("LIMPAR CADASTRO", type='secondary')

    if enviar:
        #validador do nome
        if nome == "":
            st.warning('NOME - não pode ficar em branco')
            validador = False

        #validador do cpf
        if cpf == "":
            st.warning('CPF - Não pode ficar em branco')
            validador = False
        elif len(cpf) < 11:
            st.warning('CPF - Invalido')
            validador = False
        elif verificaFuncionario(cpf) == True:
            st.error('CPF JÁ CADASTRADO NO BANCO DE DADOS')
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
        
        #validador salario
        if salario == "":
            salario = 0

        #validador endereco
        if cep == "":
            st.warning('CEP - Não pode ficar em branco')
            validador = False
        elif cepValidado != False and numero == "":
            col_rua.warning('NUMERO - Digite o numero da casa')
            col_numero.error('🔺', icon='⬆')
            validador = False
        


        if validador:
            import time
            print ('-VALIDADOR-')
            barCadastro = st.progress(0, text="CADASTRO VALIDADO - Incluindo no banco de dados")
            endereco_final = endereco.Endereco(0, rua, numero, bairro, cidade, estado, cep)
            
            barCadastro.progress(20,text="BANCO DE DADOS - Salvar Endereço")
            id_endereco = salvarEndereco(endereco_final)

            barCadastro.progress(50,text=f"BANCO DE DADOS - Salvar Funcionario")
            salvarFuncionario(funcionario.Funcionario(cpf, nome, ddd, telefone, 1, salario, id_endereco, "11231231231231", 0, 0))
            st.success('CADASTRO REALIZADO COM SUCESSO')

            barCadastro.progress(90,text=f"BANCO DE DADOS OK - REDIRECIONAR")
            totalDirecionar = 90
            for totalDirecionar in range(30):
                time.sleep(0.1)
                barCadastro.progress(totalDirecionar + 1, text=f"BANCO DE DADOS OK - REDIRECIONAR")
            barCadastro.progress(100,text=f"REDIRECIONANDO")
            time.sleep(.300)
            # st.session_state['pagina_atual'] = 'inicio'
            # st.rerun()


def salvarEndereco(endereco):
    endereco_id = EnderecoController.Incluir(endereco)
    return endereco_id

def salvarFuncionario(funcionario):
    funcionario_id = FuncionarioController.Incluir(funcionario)
    pass

def verificaFuncionario(cpf):
    verificaFuncionario = FuncionarioController.existeFuncionario(cpf)
    if verificaFuncionario:
        if verificaFuncionario['cpf'] == cpf:
            print("Funcionario já cadastrado")
            return True
    return False

    # Every form must have a submit button.
    #submitted = st.form_submit_button("CADASTRAR")
    # if submitted:
    #     st.write("slider", slider_val, "checkbox", checkbox_val)