import streamlit as st
st.little( "แอพพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ." )

bh__year=st.number_input( "กรอกปี พ.ศ. ที่ต้องการแปลง" , value=2569 )
ce_year=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
