# Contents of ~/my_app/pages/page_2.py
import pandas as pd
import streamlit as st
import plotly.express as px
import joblib
from streamlit_text_annotation import text_annotation

st.set_page_config(
    page_title="GreatSchools Analysis Tool",
    page_icon="./icon.png",
)

st.markdown("# High-level Summary️")

c1 = st.container()
c2 = st.container()
c3 = st.container()

with c1:
    dic = joblib.load("./star_rating_dist.pkl")
    st.subheader("Rating distribution of six subitems")
    option = st.selectbox(
        'Choose a subitem:',
        ('Bullying policy', 'Character', 'Homework', 'LD Support', 'Leadership', 'Teachers'))
    fig = px.bar(x=[1, 2, 3, 4, 5], y=dic[option])
    fig.update_layout(
        xaxis_title=dict(text='Ratings'),  # xy轴label设置
        yaxis_title_text='Count',  # 默认聚合函数count
        bargap=0.3,  # 组间距离
        bargroupgap=0.3,  # 组内距离
        showlegend=False
    )
    st.plotly_chart(fig)

with c2:
    st.subheader("Text length distribution of reviews")
    fig = px.box(joblib.load("./review_length.pkl"))
    fig.update_layout(xaxis_title="None", yaxis_title="Length")
    st.plotly_chart(fig)


with c3:
    st.subheader("Topics analysis")
    st.write("Under the existing rating system, our method finds more topics (represented by blue color).This is the area that were discussed by parents but systematically missing from the current school quality information.")
    df = pd.read_excel(r"./topics_for_plot.xlsx")
    fig = px.treemap(df, path=['level1', 'level2', 'level3'], color='Type',
                     color_discrete_map={'(?)': 'lightgrey', 'old': 'lightgrey', 'new': 'darkblue'})
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25), uniformtext=dict(minsize=11))
    st.plotly_chart(fig, use_container_width=True)

