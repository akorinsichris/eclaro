import streamlit as st
import pandas as pd
import plotly.express as px

# read csv from a github repo
df = pd.read_csv("https://raw.githubusercontent.com/akorinsichris/eclaro/main/resource.csv")

st.title("GSD Dashboard")

total_count=df["EID"].count()
total_resource=df["ACCT_NAME"].count()
total_manager=len(df[df["ROLE"] == 'Manager'])

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

# st.dataframe(selection_query)

account_per_cnt = (selection_query.groupby(by=['ACCT_NAME']).count()['EID'])

account_per_cnt_barchart=px.bar(account_per_cnt,
                                x=account_per_cnt.index,
                                y='EID',
                                title='Count per Account',
                                color_discrete_sequence=["#17f50c"],
                               )
account_per_cnt_barchart.update_layout(plot_bgcolor = "rgba(0,0,0,0)",xaxis=(dict(showgrid=False)))

account_per_cnt_piechart = px.pie(account_per_cnt, 
                                  names= account_per_cnt.index,
                                  values ="EID",
                                  title="Count per Account",
                                  hole=.3,
                                  color=account_per_cnt.index,
                                  color_discrete_sequence=px.colors.sequential.RdPu_r
                                 )

left_column,right_column=st.columns(2)
left_column.plotly_chart(account_per_cnt_barchart,use_container_width=True)
right_column.plotly_chart(account_per_cnt_piechart,use_container_width=True)









