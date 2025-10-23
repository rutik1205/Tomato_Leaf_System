import streamlit as st
from streamlit_option_menu import option_menu
from home import Home
from planty import Planty
from shop import Shop
from contact import Contact
from google_translate import translations

# Set up page configuration
st.set_page_config(page_title="Tomato Leaf Detection System", page_icon="🍅", layout="wide")

# Language Selection
languages = {"English": "en", "हिन्दी": "hi", "मराठी": "mr"}

selected_lang = st.sidebar.selectbox("🌐 Select Language | भाषा निवडा", list(languages.keys()))
lang_code = languages[selected_lang]

menu_labels = translations[lang_code]

select = option_menu(
    menu_title='',
    options=[menu_labels["home"], menu_labels["planty_ai"], menu_labels["shop"], menu_labels["contact"]],
    icons=['house', 'robot', 'shop', 'envelope'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"},
        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

# Pass the selected language to each page
if select == menu_labels["home"]:
    Home(lang_code)
elif select == menu_labels["planty_ai"]:
    Planty(lang_code)
elif select == menu_labels["shop"]:
    Shop(lang_code)
elif select == menu_labels["contact"]:
    Contact(lang_code)