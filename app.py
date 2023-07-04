import streamlit as st
import pandas as pd

# read csv from a github repo
df = pd.read_csv("https://raw.githubusercontent.com/akorinsichris/eclaro/main/resource_account.csv")


st.sidebar.header("Filter By:")

account=st.sidebar.multiselect("Filter By Account:",
                            options=df["ACCT_NAME"].unique(),
                            default=df["ACCT_NAME"].unique())

selection_query=df.query("ACCT_NAME==@account")

st.dataframe(selection_query)







