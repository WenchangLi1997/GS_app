# Contents of ~/my_app/pages/page_3.py
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_text_annotation import text_annotation

st.set_page_config(
    page_title="GreatSchools Analysis Tool",
    page_icon="./icon.png",
)

st.markdown("# Review Analysis")
# st.write("Sentiment Polarity Predicted by Our Method")
# review = st.text_area('Review')
# rating = st.selectbox("Rating", (1, 2, 3, 4, 5))

def f(review, rating):
    return [['2', '2'], ['1', '1']]


def analysis(df, id):
    def f(n):
        if n == -1:
            return ("Negative", '🙁')
        elif n == 1:
            return ("Positive", '😊')
        else:
            return ("Neutral", '😐')

    imp = [i for i in df.columns if "_imp" in i]
    senti = [i for i in df.columns if "_senti" in i]
    d = df[df['id'] == id]
    res = []
    for i in range(len(imp)):
        if d[imp[i]].values != 0:
            res.append([imp[i].replace("_imp", ""), d[imp[i]].values[0], d[senti[i]].values[0]])
    # table
    col1, col2, col3, col4 = st.columns(4)
    st.write(
        """
        <style>
        [data-testid="stMetricDelta"] svg {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    if len(res) == 1:
        col1.metric(res[0][0], f(res[0][2])[0], f(res[0][2])[1], delta_color="off")
    if len(res) == 2:
        col1.metric(res[0][0], f(res[0][2])[0], f(res[0][2])[1], delta_color="off")
        col2.metric(res[1][0], f(res[1][2])[0], f(res[1][2])[1], delta_color="off")
    if len(res) == 3:
        col1.metric(res[0][0], f(res[0][2])[0], f(res[0][2])[1], delta_color="off")
        col2.metric(res[1][0], f(res[1][2])[0], f(res[1][2])[1], delta_color="off")
        col3.metric(res[2][0], f(res[2][2])[0], f(res[2][2])[1], delta_color="off")
    if len(res) == 4:
        col1.metric(res[0][0], f(res[0][2])[0], f(res[0][2])[1], delta_color="off")
        col2.metric(res[1][0], f(res[1][2])[0], f(res[1][2])[1], delta_color="off")
        col3.metric(res[2][0], f(res[2][2])[0], f(res[2][2])[1], delta_color="off")
        col4.metric(res[3][0], f(res[3][2])[0], f(res[3][2])[1], delta_color="off")

    # pie chart
    names = [i[0] for i in res]
    values = [i[1] for i in res]
    # fig = px.pie(values=values, names=names, color_discrete_sequence=px.colors.sequential.Blues)
    fig = px.pie(values=values, names=names, color=names,
                 color_discrete_map={'Academics': 'red', 'Programs': 'blue',
                                     'Leadership': 'cyan', 'Teachers': 'black',
                                     'Character': 'pink', 'Bullying policy': 'grey'})
    fig.update_layout(autosize=False, height=300, width=400)
    st.plotly_chart(fig, use_container_width=True)


df = pd.read_excel("./review_analysis_for_plot.xlsx")

labels = [
    {"text": "Negative", "style": {"color": "black", "background-color": "yellow", "font-size": "8px", "border": "3px dashed yellow",}},
    {"text": "Positive", "style": {"color": "white", "background-color": "green", "font-size": "8px", "border": "3px dashed green",}},
    {"text": "Neutral", "style": {"color": "grey", "background-color": "white", "font-size": "8px",}},
    {"text": "Academics", "style": {"background-color": "red"}},
    {"text": "Programs", "style": {"background-color": "blue"}},
    {"text": "Leadership", "style": {"color":"black", "background-color": "cyan"}},
    {"text": "Teachers", "style": {"background-color": "black"}},
    {"text": "Character", "style": {"color":"black", "background-color": "pink"}},
    {"text": "Bullying policy", "style": {"background-color": "grey"}},
]

with st.expander("Review #1", expanded=True):
    st.write("*Despite the education my child got in the gifted program I do not recommend the school I could go on and on regarding issues we had with staff students and administration*")
    st.write("Post Time: 2022-03-26")
    st.write("Rating: ★☆☆☆☆")
    if st.button("Analysis", key="1"):
        data = {
            "tokens": [
                {"text": "Despite", "labels": ["Neutral"]}, {"text": "the", "labels": ["Neutral"]}, {"text": "education", "labels": ["Academics", "Neutral"]},
                {"text": "my", "labels": ["Neutral"]}, {"text": "child", "labels": ["Neutral"]}, {"text": "got", "labels": ["Neutral"]},
                {"text": "in", "labels": ["Neutral"]}, {"text": "the", "labels": ["Neutral"]}, {"text": "gifted", "labels": ["Programs", "Neutral"]},
                {"text": "program", "labels": ["Programs", "Neutral"]}, {"text": "I", "labels": ["Negative"]}, {"text": "do", "labels": ["Negative"]},
                {"text": "not", "labels": ["Negative"]}, {"text": "recommend", "labels": ["Negative"]}, {"text": "the", "labels": ["Negative"]},
                {"text": "school", "labels": ["Negative"]}, {"text": "I", "labels": ["Negative"]}, {"text": "could", "labels": ["Negative"]},
                {"text": "go", "labels": ["Negative"]}, {"text": "on", "labels": ["Negative"]}, {"text": "and", "labels": ["Negative"]},
                {"text": "on", "labels": ["Negative"]}, {"text": "regarding", "labels": ["Negative"]}, {"text": "issues", "labels": ["Negative"]},
                {"text": "we", "labels": ["Negative"]}, {"text": "had", "labels": ["Negative"]}, {"text": "with", "labels": ["Negative"]},
                {"text": "staff", "labels": ["Teachers", "Negative"]}, {"text": "students", "labels": ["Negative"]}, {"text": "and", "labels": ["Negative"]},
                {"text": "administration", "labels": ["Leadership", "Negative"]},
            ],
            "labels":labels
        }
        text_annotation(data)
        analysis(df, 1)

with st.expander("Review #2", expanded=True):
    st.write("*my daughter has been here since kindergarten, no issue with her teachers from then to now. My one issue is the principal and the way he goes about discipline on bullying. Doesn't seem to be bothered much by it, he says they are kids, which I did not like that response towards the situation. Im happy with the teachers and the way my daughter has grown on them and loves them, they are 10/10!*")
    st.write("Post Time: 2022-02-11")
    st.write("Rating: ★★★★★")
    if st.button("Analysis", key="2"):
        data = {
            "tokens": [
                {"text": "my", "labels": ["Neutral"]}, {"text": "daughter", "labels": ["Neutral"]}, {"text": "has", "labels": ["Neutral"]},
                {"text": "been", "labels": ["Neutral"]}, {"text": "here", "labels": ["Neutral"]}, {"text": "since", "labels": ["Neutral"]},
                {"text": "kindergarten", "labels": ["Neutral"]}, {"text": "no", "labels": ["Neutral"]}, {"text": "issue", "labels": ["Neutral"]},
                {"text": "with", "labels": ["Neutral"]}, {"text": "her", "labels": ["Neutral"]}, {"text": "teachers", "labels": ["Teachers", "Neutral"]},
                {"text": "from", "labels": ["Neutral"]}, {"text": "then", "labels": ["Neutral"]}, {"text": "to", "labels": ["Neutral"]},
                {"text": "now", "labels": ["Neutral"]}, {"text": "My", "labels": ["Neutral"]}, {"text": "one", "labels": ["Neutral"]},
                {"text": "issue", "labels": ["Negative"]}, {"text": "is", "labels": ["Negative"]}, {"text": "the", "labels": ["Negative"]},
                {"text": "principal", "labels": ["Leadership", "Negative"]}, {"text": "and", "labels": ["Negative"]}, {"text": "the", "labels": ["Negative"]},
                {"text": "way", "labels": ["Negative"]}, {"text": "he", "labels": ["Negative"]}, {"text": "goes", "labels": ["Negative"]},
                {"text": "about", "labels": ["Negative"]}, {"text": "discipline", "labels": ["Negative"]}, {"text": "on", "labels": ["Negative"]},
                {"text": "bullying", "labels": ["Bullying policy", "Negative"]}, {"text": "Doesn't", "labels": ["Negative"]}, {"text": "seem", "labels": ["Negative"]},
                {"text": "to", "labels": ["Negative"]}, {"text": "be", "labels": ["Negative"]}, {"text": "bothered", "labels": ["Negative"]},
                {"text": "much", "labels": ["Negative"]}, {"text": "by", "labels": ["Negative"]}, {"text": "it", "labels": ["Negative"]},
                {"text": "he", "labels": ["Neutral"]}, {"text": "says", "labels": ["Neutral"]}, {"text": "they", "labels": ["Neutral"]},
                {"text": "are", "labels": ["Neutral"]}, {"text": "kids", "labels": ["Neutral"]}, {"text": "which", "labels": ["Neutral"]},
                {"text": "I", "labels": ["Negative"]}, {"text": "did", "labels": ["Negative"]}, {"text": "not", "labels": ["Negative"]},
                {"text": "like", "labels": ["Negative"]}, {"text": "that", "labels": ["Negative"]}, {"text": "response", "labels": ["Negative"]},
                {"text": "towards", "labels": ["Negative"]}, {"text": "the", "labels": ["Negative"]}, {"text": "situation", "labels": ["Negative"]},
                {"text": "Im", "labels": ["Positive"]}, {"text": "happy", "labels": ["Positive"]}, {"text": "with", "labels": ["Positive"]},
                {"text": "the", "labels": ["Positive"]}, {"text": "teachers", "labels": ["Teachers", "Positive"]}, {"text": "and", "labels": ["Positive"]},
                {"text": "the", "labels": ["Positive"]}, {"text": "way", "labels": ["Positive"]}, {"text": "my", "labels": ["Positive"]},
                {"text": "daughter", "labels": ["Positive"]}, {"text": "has", "labels": ["Positive"]}, {"text": "grown", "labels": ["Positive"]},
                {"text": "on", "labels": ["Positive"]}, {"text": "them", "labels": ["Positive"]}, {"text": "and", "labels": ["Positive"]},
                {"text": "loves", "labels": ["Positive"]}, {"text": "them", "labels": ["Positive"]}, {"text": "they", "labels": ["Positive"]},
                {"text": "are", "labels": ["Positive"]}, {"text": "10/10", "labels": ["Positive"]}
            ],
            "labels": labels
        }
        text_annotation(data)
        analysis(df, 2)


with st.expander("Review #3", expanded=True):
    st.write("*Principal Tracy is amazing. School community is amazing. The school is big on teaching kindness and social/ emotional skills. Would’ve liked to see more homework, parent opportunities to volunteer especially in the older grades and in the special needs classroom.*")
    st.write("Post Time: 2021-05-30")
    st.write("Rating: ★★★★☆")
    if st.button("Analysis", key="3"):
        data = {
            "tokens": [
                {"text": "Principal", "labels": ["Leadership", "Positive"]}, {"text": "Tracy", "labels": ["Leadership", "Positive"]}, {"text": "is", "labels": ["Positive"]},
                {"text": "amazing", "labels": ["Positive"]}, {"text": "School", "labels": ["Positive"]}, {"text": "community", "labels": ["Positive"]},
                {"text": "is", "labels": ["Positive"]}, {"text": "amazing", "labels": ["Positive"]}, {"text": "The", "labels": ["Positive"]},
                {"text": "school", "labels": ["Positive"]}, {"text": "is", "labels": ["Positive"]}, {"text": "big", "labels": ["Positive"]},
                {"text": "on", "labels": ["Positive"]}, {"text": "teaching", "labels": ["Positive"]}, {"text": "kindness", "labels": ["Character", "Positive"]},
                {"text": "and", "labels": ["Positive"]}, {"text": "social/emotional", "labels": ["Character", "Positive"]}, {"text": "skills", "labels": ["Positive"]},
                {"text": "Would’ve", "labels": ["Neutral"]}, {"text": "liked", "labels": ["Neutral"]}, {"text": "to", "labels": ["Neutral"]},
                {"text": "see", "labels": ["Neutral"]}, {"text": "more", "labels": ["Neutral"]}, {"text": "homework", "labels": ["Neutral"]},
                {"text": "parent", "labels": ["Neutral"]}, {"text": "opportunities", "labels": ["Neutral"]}, {"text": "to", "labels": ["Neutral"]},
                {"text": "volunteer", "labels": ["Neutral"]}, {"text": "especially", "labels": ["Neutral"]}, {"text": "in", "labels": ["Neutral"]},
                {"text": "the", "labels": ["Neutral"]}, {"text": "older", "labels": ["Neutral"]}, {"text": "grades", "labels": ["Neutral"]},
                {"text": "and", "labels": ["Neutral"]}, {"text": "in", "labels": ["Neutral"]}, {"text": "the", "labels": ["Neutral"]},
                {"text": "special", "labels": ["Neutral"]}, {"text": "needs", "labels": ["Neutral"]}, {"text": "classroom", "labels": ["Neutral"]}
            ],
            "labels": labels
        }
        text_annotation(data)
        analysis(df, 3)

with st.expander("Review #4", expanded=True):
    st.write("*I do not recommend going to this school the teachers do very little to help with respect and responsibility and things like that my son is getting bullied and no one is doing anything about it the teachers do very little to help the students.*")
    st.write("Post Time: 2022-03-29")
    st.write("Rating: ★☆☆☆☆")
    if st.button("Analysis", key="4"):
        data = {
            "tokens": [
                {"text": "I", "labels": ["Negative"]}, {"text": "do", "labels": ["Negative"]}, {"text": "not", "labels": ["Negative"]},
                {"text": "recommend", "labels": ["Negative"]}, {"text": "going", "labels": ["Negative"]}, {"text": "to", "labels": ["Negative"]},
                {"text": "this", "labels": ["Negative"]}, {"text": "school", "labels": ["Negative"]}, {"text": "the", "labels": ["Negative"]},
                {"text": "teachers", "labels": ["Teachers", "Negative"]}, {"text": "do", "labels": ["Negative"]}, {"text": "very", "labels": ["Negative"]},
                {"text": "little", "labels": ["Negative"]}, {"text": "to", "labels": ["Negative"]}, {"text": "help", "labels": ["Negative"]},
                {"text": "with", "labels": ["Negative"]}, {"text": "respect", "labels": ["Character", "Negative"]}, {"text": "and", "labels": ["Negative"]},
                {"text": "responsibility", "labels": ["Character", "Negative"]}, {"text": "and", "labels": ["Negative"]}, {"text": "things", "labels": ["Negative"]},
                {"text": "like", "labels": ["Negative"]}, {"text": "that", "labels": ["Negative"]}, {"text": "my", "labels": ["Neutral"]},
                {"text": "son", "labels": ["Neutral"]}, {"text": "is", "labels": ["Neutral"]}, {"text": "getting", "labels": ["Negative"]},
                {"text": "bullied", "labels": ["Bullying policy", "Negative"]}, {"text": "and", "labels": ["Negative"]}, {"text": "no", "labels": ["Negative"]},
                {"text": "one", "labels": ["Negative"]}, {"text": "is", "labels": ["Negative"]}, {"text": "doing", "labels": ["Negative"]},
                {"text": "anything", "labels": ["Negative"]}, {"text": "about", "labels": ["Negative"]}, {"text": "it", "labels": ["Negative"]},
                {"text": "the", "labels": ["Negative"]}, {"text": "teachers", "labels": ["Teachers", "Negative"]}, {"text": "do", "labels": ["Negative"]},
                {"text": "very", "labels": ["Negative"]}, {"text": "little", "labels": ["Negative"]}, {"text": "to", "labels": ["Negative"]},
                {"text": "help", "labels": ["Negative"]}, {"text": "the", "labels": ["Negative"]}, {"text": "students", "labels": ["Negative"]}
            ],
            "labels": labels
        }
        text_annotation(data)
        analysis(df, 4)


with st.expander("Review #5", expanded=True):
    st.write("*I have two kids attending this school and would classify it as a little above average. There is no bullying and the teachers and office staff care about the students, but the classes are really crowded, there are no school trips even after parents donations and after school activities are also lacking.Not to mention the lack of diversity...*")
    st.write("Post Time: 2020-05-17")
    st.write("Rating: ★★★☆☆")
    if st.button("Analysis", key="5"):
        data = {
            "tokens": [
                {"text": "I", "labels": ["Neutral"]}, {"text": "have", "labels": ["Neutral"]}, {"text": "two", "labels": ["Neutral"]},
                {"text": "kids", "labels": ["Neutral"]}, {"text": "attending", "labels": ["Neutral"]}, {"text": "this", "labels": ["Neutral"]},
                {"text": "school", "labels": ["Neutral"]}, {"text": "and", "labels": ["Neutral"]}, {"text": "would", "labels": ["Neutral"]},
                {"text": "classify", "labels": ["Neutral"]}, {"text": "it", "labels": ["Neutral"]}, {"text": "as", "labels": ["Neutral"]},
                {"text": "a", "labels": ["Neutral"]}, {"text": "little", "labels": ["Neutral"]}, {"text": "above", "labels": ["Neutral"]},
                {"text": "average", "labels": ["Neutral"]}, {"text": "There", "labels": ["Positive"]}, {"text": "is", "labels": ["Positive"]},
                {"text": "no", "labels": ["Positive"]}, {"text": "bullying", "labels": ["Bullying policy", "Positive"]}, {"text": "and", "labels": ["Positive"]},
                {"text": "the", "labels": ["Positive"]}, {"text": "teachers", "labels": ["Teachers", "Positive"]}, {"text": "and", "labels": ["Positive"]},
                {"text": "office", "labels": ["Positive"]}, {"text": "staff", "labels": ["Positive"]}, {"text": "care", "labels": ["Positive"]},
                {"text": "about", "labels": ["Positive"]}, {"text": "the", "labels": ["Positive"]}, {"text": "students", "labels": ["Positive"]},
                {"text": "but", "labels": ["Negative"]}, {"text": "the", "labels": ["Negative"]}, {"text": "classes", "labels": ["Negative"]},
                {"text": "are", "labels": ["Negative"]}, {"text": "really", "labels": ["Negative"]}, {"text": "crowded", "labels": ["Negative"]},
                {"text": "there", "labels": ["Negative"]}, {"text": "are", "labels": ["Negative"]}, {"text": "no", "labels": ["Negative"]},
                {"text": "school", "labels": ["Negative"]}, {"text": "trips", "labels": ["Negative"]}, {"text": "even", "labels": ["Neutral"]},
                {"text": "after", "labels": ["Neutral"]}, {"text": "parents", "labels": ["Neutral"]}, {"text": "donations", "labels": ["Neutral"]},
                {"text": "and", "labels": ["Negative"]}, {"text": "after", "labels": ["Negative"]}, {"text": "school", "labels": ["Negative"]},
                {"text": "activities", "labels": ["Negative"]}, {"text": "are", "labels": ["Negative"]}, {"text": "also", "labels": ["Negative"]},
                {"text": "lacking", "labels": ["Negative"]}, {"text": "Not", "labels": ["Negative"]}, {"text": "to", "labels": ["Negative"]},
                {"text": "mention", "labels": ["Negative"]}, {"text": "the", "labels": ["Negative"]}, {"text": "lack", "labels": ["Negative"]},
                {"text": "of", "labels": ["Negative"]}, {"text": "diversity", "labels": ["Negative"]}
            ],
            "labels": labels
        }
        text_annotation(data)
        analysis(df, 5)