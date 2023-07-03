#展示整体的第二个网页
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
import folium
import pandas as pd
import requests
import streamlit as st
from streamlit_folium import st_folium

st.title("基于百度指数的各省旅游热度图")
st.subheader("点击以下省份获得具体旅游热度")

df=pd.read_excel(r"C:\Users\heduidui\Desktop\final\provinceinfo2022.xlsx")
#province_all = pd.read_excel(r"D:\gisfinal\provinceinfo.xlsx")
#df=pd.read_excel("provinceinfo2022.xlsx")

# 创建地图对象
m = folium.Map(location=[30, 105], tiles="Stamenterrain", zoom_start=3, width=600, height=400)

# 发送请求并获取JSON数据
response = requests.get("https://geo.datav.aliyun.com/areas_v2/bound/100000_full.json")
data = response.json()

# 读取Excel文件数据


# 用字典保存每个省份对应的popup内容
popup_content_dict = {}

for feature in data['features']:
    # 获取几何数据和属性
    properties = feature['properties']
    # 从Excel文件中查找匹配的数据
    for i in range(len(df)):
        if df.省份[i][0:2] == properties['name'][0:2]:
            df.省份[i] = properties['name']
            # 保存每个省份对应的popup内容
            popup_content = f"{properties['name']}<br>"
            popup_content += f"基于百度指数的旅游热度为 {df.旅游热度[i]}"
            popup_content_dict[properties['name']] = popup_content

folium.Choropleth(
    geo_data=data,
    name='choropleth',
    data=df,
    columns=["省份", "旅游热度"],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Data'
).add_to(m)

# 遍历JSON数据的features
for feature in data['features']:
    # 获取几何数据和属性
    geometry = feature['geometry']
    properties = feature['properties']

    # 创建GeoJson对象并添加到地图上

    geojson = folium.GeoJson(geometry, name=properties['name'],
                             style_function=lambda x: {'fillColor': 'transparent', 'fillOpacity': 0,
                                                       'color': 'transparent',
                                                       'opacity': 0})

    # 从字典中获取对应省份的popup内容
    if properties['name'] in popup_content_dict:
        popup_content = popup_content_dict[properties['name']]
    else:
        popup_content = ""

    # 创建popup对象
    popup = folium.Popup(popup_content, max_width=300)

    # 将popup对象添加到GeoJson对象
    geojson.add_child(popup)

    # 将GeoJson对象添加到地图上
    geojson.add_to(m)
output = st_folium(m, width=700, height=500)
st.text("可以得出旅游热度较高的省份主要集中在我国西部，特别是西南部地区")
st.subheader("\n")
st.subheader("各省份旅游热度表")
col1,col2,col3 = st.columns([1.5,4,1.5])


with col2:
    AgGrid(df)

df.columns = df.columns.astype(str)

chart_data = df.set_index('省份')['旅游热度']
st.subheader("\t")
st.subheader("各省份旅游热度条形图")
st.bar_chart(chart_data)


