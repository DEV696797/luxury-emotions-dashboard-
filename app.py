import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="Luxury Purchase Intention Dashboard",
    layout="wide"
)

# Purple theme styling
st.markdown("""
<style>
.main {
    background-color: #1a1033;
}
h1,h2,h3 {
    color:#c59cff;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("💎 Effect of Emotions on Purchase Intention of Luxury Products")

# Quote
st.markdown("""
*"Luxury must be comfortable, otherwise it is not luxury."*  
— **Coco Chanel**
""")

st.divider()

# Load dataset
df = pd.read_excel("dataset.xlsx")

# KPI cards
col1,col2,col3,col4 = st.columns(4)

col1.metric("Respondents", "105")
col2.metric("R² Value", "0.641")
col3.metric("Strongest Predictor", "Emotional Response")
col4.metric("Significance", "p < 0.001")

st.divider()

# Dataset preview
st.subheader("Survey Dataset")
st.dataframe(df)

st.divider()

# Gender chart
if "Gender" in df.columns:

    st.subheader("Gender Distribution")

    fig = px.pie(
        df,
        names="Gender",
        color_discrete_sequence=["#8a2be2","#c59cff"]
    )

    st.plotly_chart(fig,use_container_width=True)

# Age chart
if "Age" in df.columns:

    st.subheader("Age Distribution")

    fig2 = px.histogram(
        df,
        x="Age",
        color_discrete_sequence=["#8a2be2"]
    )

    st.plotly_chart(fig2,use_container_width=True)

st.divider()

# Regression results
st.subheader("Regression Model Results")

reg_data = {
    "Factor":["Emotional Response","FOMO","Celebrity Influence"],
    "Beta":[0.631,0.263,0.158]
}

reg_df = pd.DataFrame(reg_data)

fig3 = px.bar(
    reg_df,
    x="Factor",
    y="Beta",
    color="Factor",
    title="Predictors of Luxury Purchase Intention",
    color_discrete_sequence=["#8a2be2","#b57aff","#e2c6ff"]
)

st.plotly_chart(fig3,use_container_width=True)

st.divider()

# Correlation heatmap
st.subheader("Variable Relationship Heatmap")

numeric_df = df.select_dtypes(include=['int64','float64'])

if len(numeric_df.columns) > 2:

    fig, ax = plt.subplots()

    sns.heatmap(
        numeric_df.corr(),
        cmap="Purples",
        annot=True,
        ax=ax
    )

    st.pyplot(fig)

st.divider()

# Insights
st.subheader("Key Insights")

st.success("""
✔ Emotional Response is the strongest driver of luxury purchase intention.

✔ Fear of Missing Out significantly influences aspirational consumption.

✔ Celebrity influence increases perceived prestige of luxury brands.

✔ Emotional marketing strategies are essential for luxury brand success.
""")

st.divider()

# Managerial implications
st.subheader("Managerial Implications")

st.info("""
Luxury brands should focus on:

• Emotional storytelling in branding  
• Limited edition releases to trigger FOMO  
• Celebrity endorsements and influencers  
• Experiential luxury marketing campaigns
""")