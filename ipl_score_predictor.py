import streamlit as st

# Set page wide
st.set_page_config(page_title='My Streamlit App')

# Apply background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: green;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Overlay text elements
st.markdown(
    """
    <h1 style='text-align: center; color: white;'>Title Text</h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align: center; color: white;'>Description Text</p>
    """,
    unsafe_allow_html=True
)
