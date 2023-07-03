#虽然乱七八糟但勉强是一个主页面
import requests
import streamlit as st
from streamlit_lottie import st_lottie

#定义函数用于显示lottie动图
def load_lottieurl(url:str):
    r = requests.get (url)
    if r.status_code != 200:
        return None
    return r.json()

#网站主页面设置分区
col1,col2 = st.columns([1,2])
#左侧为动图
with col1:
    waterandsun_gif = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_IFhgWm6znY.json")
    st_lottie(waterandsun_gif, speed=1.5, height=300, width=200)
#右侧为文字
with col2:
    st.title("")
    st.title("")
    # 设置自定义CSS样式
    st.markdown(
        """
        <style>
        .title-font {
            font-family: cursive;
            font-size: 36px;
            font-weight: bold;
            color: #5EA7D0;  /* 设置字体颜色 */
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # 在指定位置使用自定义样式的标题
    st.markdown('<h1 class="title-font">Hi, welcome to this page!</h1>', unsafe_allow_html=True)

# 在指定位置使用自定义样式的标题
st.markdown('<h1 class="title-font">This is a website that makes your travel easier and more enjoyable.It  provides information about the crowd levels at your destination in advance.\nNow, please click on the sidebar and start planning your trip! </h1>', unsafe_allow_html=True)
# 在主页末尾添加一个可爱的会走路的香蕉
banana_gif = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_WPqksadnNs.json")
st_lottie(banana_gif, speed=1.5, height=200, width=200)
