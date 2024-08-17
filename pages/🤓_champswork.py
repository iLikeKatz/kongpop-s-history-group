import streamlit as st

st.set_page_config(
    page_title="champ's questions and links",
    page_icon="🤓"
)

def champ():
    st.markdown("# not finished yet")
    if st.button("กลับไปหน้าแรก"):
        st.session_state = "page1"
    
champ()