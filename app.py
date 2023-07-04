import streamlit as st
import pandas as pd

# read csv from a github repo
df = pd.read_csv("https://raw.githubusercontent.com/akorinsichris/eclaro/main/resource.csv")

st.title("GSD Dashboard")

total_count=df.count()
total_resource=df["ACCT_NAME"].count()
total_manager=df["ROLE==Manager"].count()

col1,col2,col3=st.columns(3)

with col1:
  st.markdown("### Account Count:")
  st.subheader(f'{total_count}')
with col2:
  st.markdown("### Resource Count:")
  st.subheader(f'{total_resource}')
with col3:
  st.markdown("### Manager Count:")
  st.subheader(f'{total_manager}')


st.markdown("---")


st.sidebar.header("Filter By:")

account=st.sidebar.multiselect("Filter By Account:",
                            options=df["ACCT_NAME"].unique(),
                            default=df["ACCT_NAME"].unique())

selection_query=df.query("ACCT_NAME==@account")

# --st.dataframe(selection_query)









