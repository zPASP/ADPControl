import streamlit as st

def buscarCep(cep):
    pass

def inicio():
    st.title('CADASTRAR')

    with st.form("my_form", clear_on_submit=False):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")