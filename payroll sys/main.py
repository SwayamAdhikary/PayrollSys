import streamlit as st

# Set page configuration
st.set_page_config(layout="wide")

# Set background image
background_image = "D:/payroll sys/images/login_image.png"
page_bg_img = f"""
<style>
body {{
    background-image: url("{background_image}");
    background-size: cover;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the layout for the login form
col_width = 400

# Add empty space for alignment
st.empty()

# Add login form to the middle column
col1, col2, col3 = st.columns(3)
col2.markdown("<h1 style='text-align: center;'>Login</h1>", unsafe_allow_html=True)

# EmpID text input field
empid = col2.text_input("EmpID", value="", max_chars=10)

# Password text input field
password = col2.text_input("Password", value="", type="password")

# Submit button
submit_button = col2.button("Submit")

# Add empty space for alignment
st.empty()

# Set the CSS styling to center the login form
total_width = col_width + col1.width + col3.width
col1.markdown(
    f"""
    <style>
        .main .block-container {{
            display: flex;
            justify-content: center;
            width: {col1.width / total_width * 100}% !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
col3.markdown(
    f"""
    <style>
        .main .block-container {{
            display: flex;
            justify-content: center;
            width: {col3.width / total_width * 100}% !important;
        }}
    </style>
    """,
    unsafe_allow_html=True
)
