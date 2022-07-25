# Contents of ~/my_app/pages/page_3.py
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GreatSchools Analysis Tool",
    page_icon="./icon.png",
)

st.markdown("# Performance Summary")


st.header("Experiment on GreatSchools and two public datasets")
st.subheader("GreatSchools.org (only evaluate on three specific aspects)")
data = [["End2end-CNN", 0.8534],
        ["End2end-LSTM", 0.8667],
        ["GCAE", 0.8674],
        ["CapsNet", 0.8687],
        ["DSPN", 0.8581]]
df = pd.DataFrame(data, columns=['Method', 'Accuracy (0-1)'])
hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Tripadvisor.com")
    data = [["End2end-CNN", 0.566],
            ["End2end-LSTM", 0.559],
            ["GCAE", 0.544],
            ["CapsNet", 0.540],
            ["DSPN", 0.503]]
    df = pd.DataFrame(data, columns=['Method', 'Accuracy (0-1)'])
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(df)

with col2:
    st.subheader("Meituan.com")
    data = [["End2end-CNN", 0.619],
            ["End2end-LSTM", 0.639],
            ["GCAE", 0.753],
            ["CapsNet", 0.759],
            ["DSPN", 0.607]]
    df = pd.DataFrame(data, columns=['Method', 'Accuracy (0-1)'])
    hide_table_row_index = """
                        <style>
                        thead tr th:first-child {display:none}
                        tbody th {display:none}
                        </style>
                        """
    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(df)

st.write("ℹ️ - The reason why our method is not the best:")
st.image("./balance.png", width=700)

