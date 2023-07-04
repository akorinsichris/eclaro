import streamlit as st
import pandas as pd

# read csv from a github repo
df = pd.read_csv("https://raw.githubusercontent.com/akorinsichris/eclaro/main/resource_account.csv")

st.sidebar.header("Filter By:")

account=st.sidebar.multiselect("Filter By Account:",
                            options=df["ACCT_NAME"].unique(),
                            default=df["ACCT_NAME"].unique())

selection_query=df.query("ACCT_NAME==@account")

#st.dataframe(selection_query)
st.title("GSD Dashboard")

total_count=(selection_query["ACCT_NAME"].count())
total_resource=(selection_query["EID"].count())

col1,col2=st.columns(2)

with col1:
  st.markdown("### Account Count:")
  st.subheader(f'{total_count}')
with col2:
  st.markdown("### Resource Count:")
  st.subheader(f'{total_resource}')








