import streamlit as st

sys.path.append("fsdl_deforestation_detection/dashboard/")
from dashboard_utils import load_css
import layouts

PAGES = dict(Playground=layouts.playground, Overview=layouts.overview)
load_css("style.css")

st.sidebar.title("About")
st.sidebar.markdown(
    "Full Stack Deep Learning course project on detecting deforestation through satellite imagery."
)
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page()