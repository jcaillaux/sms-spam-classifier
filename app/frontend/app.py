import streamlit as st
import requests as rq

# Application name
APP_NAME = 'SpamSIFT'

# Set page title
st.set_page_config(page_title=APP_NAME)

# State Initialization
if "text_input" not in st.session_state:
    st.session_state.text_input = ""


def inference():
    """  """
    if len(st.session_state.text_input) == 0 : return
    print(st.session_state.text_input)
    st.session_state.history.loc[st.session_state.history.shape[0]+1] = [st.session_state.text_input, 'ham', 'SVM']

css = """ <style>
    [data-testid='stHeaderActionElements'] {
        display : none;
    }
    h1 {
        text-align:center;
    }
</style> """

st.html(css)


st.title(APP_NAME)


with st.form(key="text_form"):
    st.markdown("*Entrer un message pour detecter s'il sagit d'un spam ou d'un message légitime:*")

    text_input = st.text_area(
        label="**SMS Text**",
        placeholder="Entrer votre text ici",
        value=st.session_state.text_input,
        max_chars=256,
        key="text_area"
    )
    submit_button = st.form_submit_button(label="Vérifier")
    
    if submit_button:
        st.write("Analyzing text:", text_input)
        st.session_state.text_input = text_input
        inference()

if st.session_state.history.shape[0] > 0 :
    st.markdown('Historique')
    st.session_state.history