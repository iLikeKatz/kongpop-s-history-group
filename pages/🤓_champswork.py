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
        st.markdown(f"## {index+1-5}. {name_list[index]}")
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

def champ():
    st.title("champ's questions")
    text1 = None
    fixname(5, variable=text1, key="1")

    link1 = None
    fixlink(25, link1, key="l1")
    
    link2 = None
    fixlink(26, link2, key="l2")

    link3 = None
    fixlink(27, link3, key="l3")

    link4 = None
    fixlink(28, link4, key="l4")

    link5 = None
    fixlink(29, link5, key="l5")
    st.text(" ")
    st.text(" ")

##########################
    text2 = None
    fixname(6, variable=text2, key=2)

    link6 = None
    fixlink(30, link6, key="l6")
    
    link7 = None
    fixlink(31, link7, key="l7")

    link8 = None
    fixlink(32, link8, key="l8")

    link9 = None
    fixlink(33, link9, key="l9")

    link10 = None
    fixlink(34, link10, key="l10")

    ##########################
    text3 = None
    fixname(7, variable=text3, key="3")

    link11 = None
    fixlink(35, link11, key="l11")

    link12 = None
    fixlink(36, link12, key="l12")

    link13 = None
    fixlink(37, link13, key="l13")

    link14 = None
    fixlink(38, link14, key="l14")

    link15 = None
    fixlink(39, link15, key="l15")

    st.text(" ")
    st.text(" ")

###########################################
    text4 = None
    fixname(8, variable=text4, key="4")

    link16 = None
    fixlink(40, link16, key="l16")

    link17 = None
    fixlink(41, link17, key="l17")

    link18 = None
    fixlink(42, link18, key="l18")

    link19 = None
    fixlink(43, link19, key="l19")

    link20 = None
    fixlink(44, link20, key="l20")

    st.text(" ")
    st.text(" ")
#################################################################
    text5 = None
    fixname(9, variable=text5, key="5")

    link21 = None
    fixlink(45, link21, key="l21")

    link22 = None
    fixlink(46, link22, key="l22")

    link23 = None
    fixlink(47, link23, key="l23")

    link24 = None
    fixlink(48, link24, key="l24")

    link25 = None
    fixlink(49, link25, key="l25")

    st.text(" ")
    st.text(" ")

champ()
