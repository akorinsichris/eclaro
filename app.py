import streamlit as st
import snowflake.connector as sf
import pandas as pd
from datetime import date

conn = sf.connect(**streamlit.secrets["snowflake"])
my_data_rows = conn.query('Select * from resource_account')
st.dataframe(my_data_rows)





