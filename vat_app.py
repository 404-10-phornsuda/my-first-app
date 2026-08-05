import streamlit as st
st.title("🛒 แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%")
# รับราคาสินค้า
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0, value=0.0)
# คำนวณ VAT และราคารวม
vat = price * 0.07
net_price = price + vat
# แสดงผล
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): {vat:.2f} บาท")
st.header(f"• ราคาสุทธิรวม VAT: {net_price:.2f} บาท")
st.write("นางสาวพรสุดา ทมิฬทร เลขที่ 10 ม.4/4")
