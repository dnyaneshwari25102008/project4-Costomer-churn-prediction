import pandas as pd
import numpy as np
import pickle
import streamlit as st

pipe = pickle.load(open("pipe.pkl","rb"))


st.markdown("""
<style>
.stApp {
    background-color:#D0D5EE;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.subheader("**🔍 Customer Churn Analysis**")
st.sidebar.image("p6.jpg")
st.sidebar.write("Predict whether a customer is likely to leave the telecom service based on customer information and subscription details.")
st.sidebar.image("p11.png")
st.sidebar.write("Supporting customer retention strategies with machine learning insights.")

st.title(' 📊 Customer Churn Predictor')
st.markdown("__________")

col1,col2,col3 = st.columns(3,gap="large")

with col1:
    gender = st.selectbox('Select Gender:',['Female', 'Male'])
    SeniorCitizen = st.selectbox('Senior citizen ?',['Yes', 'No'])
    Partner = st.selectbox('Partner ?',['Yes', 'No'])
    Dependents = st.selectbox('Dependents ?',['Yes', 'No'])
    tenure = st.number_input('Tenure (in months) :',value = 1,min_value = 1, max_value = 200, step = 50)
    PhoneService = st.selectbox('Phone Service ?',['Yes', 'No'])
     
    MultipleLines = st.selectbox('Multiple Lines ?',['Yes', 'No'])
with col2:   
    InternetService = st.selectbox('Internet Service :',sorted(df['InternetService'].unique()))
    OnlineSecurity = st.selectbox('Security Service ?',['Yes', 'No'])
    OnlineBackup = st.selectbox("Online Backup ?",['Yes','No'])

    DeviceProtection = st.selectbox('Device Protection Service ?',['Yes', 'No'])    
    TechSupport = st.selectbox('Tech Support Service ?',['Yes', 'No'])
    StreamingTV = st.selectbox('Streaming TV Subscription ?',['Yes', 'No'])
with col3:
    StreamingMovies = st.selectbox('Streaming Movies subscription ',['Yes', 'No'])
    Contract = st.selectbox('Contract Type:',sorted(df['Contract'].unique()))
    PaperlessBilling = st.selectbox('Paperless Billing ?',['Yes', 'No'])
    PaymentMethod = st.selectbox('Payment Method:',sorted(df['PaymentMethod'].unique()))
    MonthlyCharges = st.number_input("Monthly Charges:",value = 1, min_value = 1, max_value = 5000)
    TotalCharges = st.number_input("Total Charges:",value = 1, min_value = 1, max_value = 10000)



st.markdown("__________")

Press = st.button('predict result')
if Press:
    gender1 = 0 if gender=='Female' else 1
    SeniorCitizen1 = 1 if SeniorCitizen=='Yes' else 0
    Partner1 = 1 if Partner=='Yes' else 0
    Dependents1 =  1 if Dependents=='Yes' else 0
    PhoneService1 = 1 if PhoneService=='Yes' else 0

    MultipleLines1 = 1 if MultipleLines=='Yes' else 0
    OnlineSecurity1 = 1 if OnlineSecurity=='Yes' else 0
    OnlineBackup1 =  1 if OnlineBackup=='Yes' else 0
    DeviceProtection1 =  1 if DeviceProtection=='Yes' else 0
    TechSupport1 =  1 if TechSupport=='Yes' else 0
    StreamingTV1 =  1 if StreamingTV=='Yes' else 0
    StreamingMovies1 =  1 if StreamingMovies=='Yes' else 0
    PaperlessBilling1 =  1 if PaperlessBilling=='Yes' else 0


    myip = [[gender1, SeniorCitizen1, Partner1, Dependents1,
       tenure, PhoneService1, MultipleLines1, InternetService,
       OnlineSecurity1, OnlineBackup1, DeviceProtection1, TechSupport1,
       StreamingTV1, StreamingMovies1, Contract, PaperlessBilling1,
       PaymentMethod, MonthlyCharges, TotalCharges]]
    col = ['gender', 'SeniorCitizen', 'Partner', 'Dependents',
       'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
       'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
       'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
       'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
    table = pd.DataFrame(data = myip, columns = col)
    result = pipe.predict(table)
    if result[0] == 1:
        st.error(" ⚠️ Customer may churn")
    else:
        st.success(" ✅ Customer may not churn")
        
    
    data = pd.DataFrame(data=[
            ["gender", gender],
            ["SeniorCitizen", SeniorCitizen],
            ["Partner", Partner],
            ["Dependents", Dependents],
            
            ["tenure", tenure],
            ["PhoneService", PhoneService],
            ["MonthlyCharges", MonthlyCharges],
            ["TotalCharges", TotalCharges]
        ],
    columns=["Feature", "Value"]
    )
    
    st.subheader("You have selected")
    st.write(data)
    
    st.subheader("📊 Patient graph")         
    st.bar_chart(data.set_index("Feature"),color="#8993CC")
    st.write(" ")
    st.image("p0.png")
    st.write("📈 Helps businesses identify at-risk customers before they churn.Supports targeted retention efforts and improves customer loyalty.")








