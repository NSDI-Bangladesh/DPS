import streamlit as st
import json
import datetime


with open('DPS.json', 'r', encoding="utf8") as f:
    data = f.read()
    data = json.loads(data)

hide_streamlit_style = """<style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                </style>"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

with st.sidebar:
    st.title('National Spatial Data Infrastructure')
    st.markdown('Use this siderbard to select the mode of DPS')
    drawing_mode = st.sidebar.selectbox("DPS Mode:", ("View", "Add", "Update", "Delete"))
    date = st.date_input("View Changes in DPS by Date:")
    dataset = st.radio("Select the Type of Data:", ['Shapefile', 'Raster', 'Orthophoto', 'Basemap'])


organization_names = [organization['Organization'] for organization in data]

st.title("NSDI Data Product Specification Catalog")
organization = st.selectbox("Name of the Organization", organization_names)

for org in data:
    if org["Organization"] == organization:
        st.subheader('Overview')
        st.markdown(f"**Last Updated:** {org['Overview']['Date']}")
        st.markdown(f"**Responsible Organization:** {org['Overview']['Responsible Organization']}")
        st.markdown(f"**Language:** {org['Overview']['Language']}")
        st.markdown(f"**Topic Category:** {org['Overview']['Topic Category']}")
        st.markdown(f"**Objectives:** {org['Overview']['Objectives']}")
        st.markdown(f"**Normative References:** {org['Overview']['Normative References']}")

        st.subheader('Scope')
        st.markdown(f"**Scope identification:** {org['Scope']['Scope identification']}")
        st.markdown(f"**Hierarchical level:** {org['Scope']['Hierarchical level']}")

        st.subheader('Data Product Identification')
        st.markdown(f"**Name:** {org['Data Product Identification']['Name']}")
        st.markdown(f"**Date of Data Creation:** {org['Data Product Identification']['Date of Data Creation']}")
        st.code(f"Contact information: {org['Data Product Identification']['Contact information']}")

        st.subheader("Reference System")
        st.code(f"{org['Reference System']['Spatial reference system']}")
        st.markdown(f"**Temporal Reference System:** {org['Reference System']['Temporal reference system']}")

        st.subheader("Data Product Delivery")
        st.markdown(f"**Name of Data Formats:** {org['Data Product Delivery']['Name of data formats']}")
        st.markdown(f"**Structure of Dataset:** {org['Data Product Delivery']['Structure of data set']}")
        st.markdown(f"**Encoding Rules:** {org['Data Product Delivery']['Encoding rules']}")
        st.markdown(f"**Language:** {org['Data Product Delivery']['Language']}")



# st.write(org)