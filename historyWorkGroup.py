import streamlit as st
from kongpopwork import kongpop
from champwork import champ
from krittapakwork import krittapak

def page1():
    st.markdown("# งานกลุ่มประวัติ")
    st.markdown("##(กดปุ่ม2ที)")
    st.text(" ")
    st.markdown("## justwho's k")
    if st.button("enter to see your links:)", key="jk"):
        st.session_state = "page2"
    st.markdown("## Champ")
    if st.button("enter to see your links:)", key="champ"):
        st.session_state = "page3"
    st.markdown("## Krittapak")
    if st.button("enter to see your links:)", key="lui"):
        st.session_state = "page4"


if "page" not in st.session_state:
    st.session_state = "page1"

if st.session_state == "page1":
    page1()
elif st.session_state == "page2":
    kongpop()
elif st.session_state == "page3":
    champ()
elif st.session_state == "page4":
    krittapak()
