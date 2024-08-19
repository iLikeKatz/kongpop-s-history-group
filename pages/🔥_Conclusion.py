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
check = load_data('TrueFalse.json')

def fixname(index, variable, key):
    st.markdown(f"## {index+1}. {name_list[index]}")

def fixlink(index, variable, key, show_full_links=check[0]):
    if show_full_links == "True":
        show_full_links = True
    else :
        show_full_links = False
    cols = st.columns(2)
        
    if show_full_links:
        name = data[index]
    else :
        if len(data[index]) < 15:
            name = data[index][:3]
        else:
            name = data[index][9:15]
    
    links = str(key[1:])
    with cols[0]:
        st.markdown(f"""
        ### link {links} : <a href="{data[index]}" target="_blank">{"None" if data[index] == "" else name}</a>
        """, unsafe_allow_html=True)
    st.text(" ")

def conclusion():
    if check[0] != "True":
        if st.button("show full links"):
            check[0] = 'True'
            save_data(check, 'TrueFalse.json')
            st.success('done')
    else :
        if st.button("hide some texts links"):
            check[0] = 'False'
            save_data(check, 'TrueFalse.json')
            st.success('done')

    st.title("สรุปทั้ง 6 คำถาม")
    st.markdown("#### *ไปใส่ links ในช่องของตัวเอง เเล้วมันจะมาขึ้นในนี้ให้เอง*")
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

    ##########################
    text3 = None
    fixname(2, variable=text3, key="3")

    link11 = None
    fixlink(10, link11, key="l11")

    link12 = None
    fixlink(11, link12, key="l12")

    link13 = None
    fixlink(12, link13, key="l13")

    link14 = None
    fixlink(13, link14, key="l14")

    link15 = None
    fixlink(14, link15, key="l15")

    st.text(" ")
    st.text(" ")

###########################################
    text4 = None
    fixname(3, variable=text4, key="4")

    link16 = None
    fixlink(15, link16, key="l16")

    link17 = None
    fixlink(16, link17, key="l17")

    link18 = None
    fixlink(17, link18, key="l18")

    link19 = None
    fixlink(18, link19, key="l19")

    link20 = None
    fixlink(19, link20, key="l20")

    st.text(" ")
    st.text(" ")
#################################################################
    text5 = None
    fixname(4, variable=text5, key="5")

    link21 = None
    fixlink(20, link21, key="l21")

    link22 = None
    fixlink(21, link22, key="l22")

    link23 = None
    fixlink(22, link23, key="l23")

    link24 = None
    fixlink(23, link24, key="l24")

    link25 = None
    fixlink(24, link25, key="l25")

    st.text(" ")
    st.text(" ")
    text6 = None
    fixname(5, variable=text6, key="6")

    link26 = None
    fixlink(25, link26, key="l26")

    link27 = None
    fixlink(26, link27, key="l27")

    link28 = None
    fixlink(27, link28, key="l28")

    link29 = None
    fixlink(28, link29, key="l29")

    link30 = None
    fixlink(29, link30, key="l30")

conclusion()
