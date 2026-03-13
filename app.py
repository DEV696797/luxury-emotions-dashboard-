import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Luxury Purchase Intention Research", layout="wide")

# Title
st.title("💎 Effect of Emotions on Purchase Intention of Luxury Products")

st.markdown("""
*"Luxury must be comfortable, otherwise it is not luxury."*  
— **Coco Chanel**
""")

st.divider()

# Project overview
st.header("Research Overview")

st.write("""
This website presents the Phase III Major Research Project examining the
impact of emotional factors on consumer purchase intention toward luxury products.

The study focuses on three primary determinants:

• Emotional Response  
• Celebrity Influence  
• Fear of Missing Out (FOMO)

The research was conducted using survey responses and analyzed using
multiple linear regression to understand how emotional factors influence
luxury purchase intention.
""")

# Key metrics
col1, col2, col3 = st.columns(3)

col1.metric("Respondents", "105")
col2.metric("R² Value", "0.641")
col3.metric("Strongest Predictor", "Emotional Response")

st.divider()

# Embedded report
st.header("Phase III Research Report")

with open("Phase_III_Report.pdf", "rb") as file:
    pdf_bytes = file.read()

base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')

pdf_display = f"""
<iframe src="data:application/pdf;base64,{base64_pdf}"
width="100%" height="900" type="application/pdf"></iframe>
"""

st.markdown(pdf_display, unsafe_allow_html=True)

st.download_button(
    label="Download Full Report",
    data=pdf_bytes,
    file_name="Phase_III_Report.pdf",
    mime="application/pdf"
)

st.divider()

# Dataset preview
st.header("Survey Dataset")

try:
    df = pd.read_excel("dataset.xlsx")
    st.dataframe(df)
except:
    st.info("Dataset file not found.")