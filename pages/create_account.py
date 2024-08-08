import streamlit as st
from utils import *

def create_user(username, name, email, password, confirm_password):
    loader('Logando...')
    if username != '' and name != '' and email != and password != '' and confirm_password != '':
        return True
    else: 
        return False

def main():
    st.set_page_config(
        page_title="Criar Conta", 
        page_icon="🙃",
        layout="centered", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()

    st.title("Criar Conta")
    username = st.text_input("Usuário:")
    name = st.text_input("Nome Completo:")
    email = st.text_input("Email:")
    password = st.text_input("Senha:", type="password")
    confirm_password = st.text_input("Confirmar Senha:", type="password")

    if st.button("Criar Conta", use_container_width=True, type='primary', help="Clique para criar uma nova conta"):
        
    elif st.session_state['authentication_status'] is False:
        st.error('Erro ao criar conta')
    elif st.session_state['authentication_status'] is None:
        st.warning('Por favor, preencha os campos')
    
    st.caption("Opções:")
    st.button("Já tenho uma conta", use_container_width=False, help="Clique para fazer login")

if __name__ == "__main__":
    main()
