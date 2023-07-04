import streamlit as st

# initialize connection
conn = st.experimental_connection('snowflake', type='sql')

#load the table as a dataframe using the snowpark session.
@st.cache_date
def load_table():
  with conn.safe_session() as session:
    return session.table('resource_account').to_pandas()
    
df = load_table()

st.dataframe(df)





