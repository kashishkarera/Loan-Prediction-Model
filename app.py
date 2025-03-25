import pandas as pd
import streamlit as st
import pickle as pk

model=pk.load(open('model', 'rb'))
scaler=pk.load(open('scaler','rb'))
st.header("Loan Prediction Model")


Dependents= st.slider('No. of Dependents ',0,10)
Education= st.selectbox('Education',['Graduated', 'Not Graduated'])
Employment=st.selectbox('self_employed',['Yes', 'No'])
App_Income=st.number_input("Chooose Annual Income", 0,100000000)
Loan=st.number_input("Loan Amount",0,10000000000)
Duration=st.slider("Loan Amount Term" , 0,20)
Cibil=st.slider('Cibil Score',0, 1000)
Assets=st.number_input('Asset value',0,100000000)

if Education== 'Graduated':
    edu=0
else:
    edu=1

if Employment== 'Yes':
    emp=1
else:
    emp=0
if st.button("Predict"):
    pred_data=pd.DataFrame([[Dependents,	edu,	emp,	App_Income,	Loan,	Duration,	Cibil,	Assets]], columns=[	'no_of_dependents',	'education',	'self_employed',	'income_annum',	'loan_amount',	'loan_term',	'cibil_score',	'Assets'])
    pred_data=scaler.transform(pred_data)
    predict=model.predict(pred_data)

    if predict[0] == 0:
        st.markdown('Loan Approved')
    else:
        st.markdown('Loan DisApproved')







