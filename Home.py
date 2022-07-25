# Contents of ~/my_app/main_page.py
import streamlit as st

st.set_page_config(
    page_title="GreatSchools Analysis Tool",
    page_icon="./icon.png",
)



st.image("logo.png", width=400)
st.markdown("# GreatSchools Review Analysis Tool")
st.write(
        """     
-   This *GreatSchools Analysis Tool* is used to analyze parent reviews on GreatSchools.
-   We first report a high-level summary for parent review data, then extract the topics and identify the corresponding sentiments for reviews. At last, we also report the performance of this tool.
	    """
)
with st.expander("ℹ️ - About this tool", expanded=True):
    st.write("For now, the data we use is the parent review data with subratings (updated in 2022.04.12)")
