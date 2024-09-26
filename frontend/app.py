import streamlit as st
import pandas as pd
from transaction_class import Transaction
from process_file import process_transaction_file

#in app memory persistance
if 'accounts' not in st.session_state:
    st.session_state['accounts'] = {}
if 'bad_transaction' not in st.session_state:
    st.session_state['bad_transaction'] = []

#upload and process data file
data_file = st.file_uploader("Upload data file")

#eventually expand to use multiple different file types
if data_file is not None:
    transactions = pd.read_csv(data_file)

    for index, row in transactions.iterrows():
        st.session_state['accounts'], st.session_state['bad_transaction'] = process_transaction_file(
            row,
            st.session_state['accounts'],
            st.session_state['bad_transaction']
        )


st.write("Accounts")



st.button("Reset")