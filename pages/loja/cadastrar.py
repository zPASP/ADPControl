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
    col_titulo.title('CADASTRAR LOJA')

    st.subheader('Informações da Loja:')

    #informações da loja
    ## CNPJ, nome, dd, telefone

    nome = st.text_input('Nome:', placeholder= 'Loja principal LTDA.' )
    col_cnpj, col_ddd, col_telefone  = st.columns((2,0.6,2))
    cnpj = col_cnpj.text_input('CNPJ:', max_chars=14)
    ddd = col_ddd.text_input('DDD:', max_chars=2, help='Somente Numeros')
    telefone = col_telefone.text_input('Celular:', max_chars=9, help='INSIRA O NUMERO DO FUNCIONARIO')
    

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


    col_voltar2, col_enviar, col_limpar, col_2 = st.columns((1,2,2,1))
    #voltar2 = col_voltar2.button("◀ **VOLTAR**")
    enviar = col_enviar.button("CADASTRAR LOJA", type='primary', use_container_width=True, key='btnCadastrar', )
    limpar = col_limpar.button("LIMPAR CADASTRO", type='secondary', use_container_width=True)
    
    if enviar:
        #validador do nome
        if nome == "":
            st.warning('NOME - não pode ficar em branco')
            validador = False

        #validador do CNPJ
        if cnpj == "":
            st.warning('CNPJ - Não pode ficar em branco')
            validador = False
        elif len(cnpj) < 14:
            st.warning('CNPJ - Invalido')
            validador = False
        elif len(cnpj) == 14:
            existe = LojaController.lojaExiste(cnpj)
            if existe != None:
                st.warning(f'Já existe uma Loja com o CNPJ {cnpj}')
                print('Já existe uma loja com o cnpj informado')
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

        #validador endereco
        if cep == "":
            st.warning('CEP - Não pode ficar em branco')
            validador = False
        elif cepValidado != False and numero == "":
            col_rua.warning('NUMERO - Digite o numero da casa')
            col_numero.error('🔺', icon='⬆')
            validador = False

        

        if validador:
            # .button("REALIZANDO CADASTRO", key='btnCadastrar', disabled=True)
            print ('-VALIDADOR-')
            endereco_final = endereco.Endereco(0, rua, numero, bairro, cidade, estado, cep)
            
            id_endereco = salvarEndereco(endereco_final)
            
            salvarLoja(loja.Loja(cnpj,nome, ddd, telefone,0 ,id_endereco))
            st.success('CADASTRO REALIZADO COM SUCESSO')

def salvarEndereco(endereco):
    endereco_id = EnderecoController.Incluir(endereco)
    #print(endereco_id)
    return endereco_id

def salvarLoja(loja):
    loja_id = LojaController.Incluir(loja)
    #print(loja_id)
    pass
