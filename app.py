import streamlit as st
import pickle as pkl

model = pkl.load(open('pipe.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_mail = st.text_area("Enter the message")

if st.button('Predict'):

    result = model.predict([input_mail])
    if result == 1:
        st.header("Spam")
    elif result==0:
        st.header("Not Spam")