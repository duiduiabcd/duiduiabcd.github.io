import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
plt.rcParams["font.family"] = "SimHei"
x = [1,2,3,4,5,6,7,8,9,10,11,12]
fig, ax = plt.subplots()
frame = pd.read_excel(r"C:\Users\heduidui\Desktop\giswork\premonth.xlsx")
names = list(frame["省份"])
st.title("旅游时间查询")
name = st.selectbox('选择旅游目的地',names)
exp = frame["省份"]==name
records = frame[exp]
record_fields = records[["一月","二月","三月","四月","五月","六月",
                         "七月","八月","九月","十月","十一月","十二月"]].iloc[0]
y = list(record_fields)
a=y.index(min(y))
st.subheader(f"建议选择{a+1}月出行，避开旅游旺季")



ax.plot(x,y,label=name)
plt.xlabel("月份")
plt.ylabel("旅游热度")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],
           ["一月","二月","三月","四月","五月","六月",
                         "七月","八月","九月","十月","十一月","十二月"])
plt.legend(loc=3)
st.pyplot(fig)


x = [1,2,3,4,5,6,7,8,9,10,11,12]
fig, ax = plt.subplots()

names = list(frame["省份"])
names = st.multiselect('选择待比较省份',names)
for name in names:
    exp = frame["省份"]==name
    records = frame[exp]
    record_fields = records[["一月","二月","三月","四月","五月","六月",
                         "七月","八月","九月","十月","十一月","十二月"]].iloc[0]
    y = list(record_fields)
    ax.plot(x,y,label=name)
plt.xlabel("月份")
plt.ylabel("旅游热度")
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],
           ["一月","二月","三月","四月","五月","六月",
                         "七月","八月","九月","十月","十一月","十二月"])
plt.legend(loc=3)
st.pyplot(fig)