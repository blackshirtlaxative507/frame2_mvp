import os
import sys
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import SETTINGS

st.set_page_config(page_title=SETTINGS.app_name, layout="wide")

st.title(SETTINGS.app_name)
st.caption("sports intelligence + content engine")
st.info("open pages from the left sidebar.")
