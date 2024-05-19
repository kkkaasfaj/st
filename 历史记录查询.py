import streamlit as st
date = st.date_input('日期')
st.write('您选择的日期是：', date)
search_query = st.text_input("请输入您的ID")
if search_query:
    st.write("搜索结果：", search_query)


