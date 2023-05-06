import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header("The Best Company")

company_details = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam , quis nostrud 
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit essecillum dolore eu fugiat nulla pariostur.
Excepteur sint occaecat cupidatat bib proident, sunt in culpa qui officia deserunt anim id est laborum.
"""
st.write(company_details)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

# Create dataframe of csv file
df = pd.read_csv("C:\\Manish\\Python\\2023\\app1\\projects\\project01\\data.csv", sep=",")

# Add content to the first column
with col1:
    for index, row in df[:4].iterrows():
        # Add member's first name and last name
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        # Add member's role in company
        st.write(row["role"])
        # Add member's photo
        st.image(f"images/{row['image']}")

# Add content to the second column
with col2:
    for index, row in df[4:8].iterrows():
        # Add member's first name and last name
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        # Add member's role in company
        st.write(row["role"])
        # Add member's photo
        st.image(f"images/{row['image']}")

# Add content to the third column
with col3:
    for index, row in df[8:].iterrows():
        # Add member's first name and last name
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        # Add member's role in company
        st.write(row["role"])
        # Add member's photo
        st.image(f"images/{row['image']}")