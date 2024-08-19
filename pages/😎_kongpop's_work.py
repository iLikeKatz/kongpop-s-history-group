import streamlit as st
import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Load the existing data
data = load_data('link.json')
name_list = load_data('name.json')

def fixname(index, variable, key):
    cols = st.columns(2)
    with cols[0]:
        st.markdown(f"## {index+1}. {name_list[index]}")
    if name_list[index] == "":
        variable = st.text_input("name your question : ", key=key)
        if variable:
            name_list[index] = variable
            save_data(name_list, 'name.json')
            st.success("successfully! ถ้าจะให้ข้อมูลอัพเดต ต้องรีหน้าเว้ปก่อน")
    else:
        with cols[1]:
            if st.button("reset", key=key):
                name_list[index] = ""
                save_data(name_list, 'name.json')
                st.success("successfully! ลบละ")
        
def fixlink(index, variable, key):
    cols = st.columns(2)
    try :
        name = data[index][9:15]
    except :
        name = data[index]
    links = str(key[1:])
    with cols[0]:
        st.markdown(f"""
        ### link {links} : <a href="{data[index]}" target="_blank">{name}</a>
        """, unsafe_allow_html=True)
    if data[index] == "":
        variable = st.text_input("your link", key=key)
        if variable:
            data[index] = variable
            save_data(data, 'link.json')
            st.success("successfully! ถ้าจะให้ข้อมูลอัพเดต ต้องรีหน้าเว้ปก่อน")
    else:
        with cols[1]:
            if st.button("reset", key=key):
                data[index] = ""
                save_data(data, 'link.json')
                st.success("successfully! ลบละ")
    st.text(" ")

def kongpop():
    st.title("kongpop's questions")
    text1 = None
    fixname(0, variable=text1, key="1")

    link1 = None
    fixlink(0, link1, key="l1")
    
    link2 = None
    fixlink(1, link2, key="l2")

    link3 = None
    fixlink(2, link3, key="l3")

    link4 = None
    fixlink(3, link4, key="l4")

    link5 = None
    fixlink(4, link5, key="l5")
    st.text(" ")
    st.text(" ")

##########################
    text2 = None
    fixname(1, variable=text2, key=2)

    link6 = None
    fixlink(5, link6, key="l6")
    
    link7 = None
    fixlink(6, link7, key="l7")

    link8 = None
    fixlink(7, link8, key="l8")

    link9 = None
    fixlink(8, link9, key="l9")

    link10 = None
    fixlink(9, link10, key="l10")

kongpop()
