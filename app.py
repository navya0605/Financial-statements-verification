from ai_verification.verify import verify_financial_statement
from blockchain.blockchain import Blockchain
import streamlit as st
import pandas as pd

st.title("AI + Blockchain Financial Statement Verification")

uploaded_file = st.file_uploader("Upload Financial Statement CSV", type="csv")

if uploaded_file:
    # Step 1: AI Verification
    verified_df = verify_financial_statement(uploaded_file)
    st.subheader("Verification Results")
    st.dataframe(verified_df[['Company','Revenue','Profit','Verification_Status']])
    
    # Step 2: Blockchain Logging
    blockchain = Blockchain()
    for idx, row in verified_df.iterrows():
        blockchain.add_block({"Document_Hash": row['Document_Hash'], "Verification_Status": row['Verification_Status']})
    
    st.subheader("Blockchain Ledger")
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            "Index": block.index,
            "Timestamp": block.timestamp,
            "Data": block.data,
            "Hash": block.hash,
            "Prev_Hash": block.previous_hash
        })
    st.dataframe(pd.DataFrame(chain_data))
