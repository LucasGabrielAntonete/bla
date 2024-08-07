import streamlit as st
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader
from manager.app_manager import AppManager
from utils import *

def main():
    st.set_page_config(
        page_title="Perfil", 
        page_icon="👾", 
        layout="wide", 
        initial_sidebar_state="collapsed"
    )
    add_custom_css()
    app_manager = AppManager()

    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    name, authentication_status, username = authenticator.login('main')

    if not authentication_status:
        st.error("Você precisa estar logado para acessar essa página")
        st.stop()

    col1, col2, col3 = st.columns([1, .2, 5])

    with col1:
        create_navbar()
    with col3:
        name = st.session_state['name']
        username = st.session_state['username']
        email = st.session_state['email']
        st.write("")
        st.write("## Perfil do Usuário")

        st.write("Nome de Usuário:")
        st.text_input("Nome de Usuário:", username, disabled=True, label_visibility='collapsed')

        st.write("Nome Completo:")
        row_name = st.columns([5, 1])
        new_name = row_name[0].text_input("Nome Completo:", name, label_visibility='collapsed')
        if row_name[1].button("Alterar Nome", use_container_width=True, help="Clique para alterar o nome", disabled=False):
            try:
                authenticator.update_user_details(new_name, username, 'name')
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.success("Nome alterado com sucesso!")
                name = new_name
            except Exception as e:
                st.error(e)

        st.write("Email:")
        row_email = st.columns([5, 1])
        new_email = row_email[0].text_input("Email:", email, label_visibility='collapsed')
        if row_email[1].button("Alterar Email", use_container_width=True, help="Clique para alterar o email", disabled=False):
            try:
                authenticator.update_user_details(new_email, username, 'email')
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.success("Email alterado com sucesso!")
                email = new_email
            except Exception as e:
                st.error(e)

        if st.button("Sair", use_container_width=True, type='primary', help="Clique para sair da sua conta"):
            authenticator.logout('Login')
            for key in ['authentication_status', 'username', 'name', 'email']:
                if key in st.session_state:
                    del st.session_state[key]
            st.switch_page("pages/login.py")

if __name__ == "__main__":
    main()
