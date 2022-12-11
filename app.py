import streamlit as st
from PIL import Image
import pandas as pd

st.title('Skin disease clasifier')

key = st.text_input('App key')

if key == '':
    st.warning('An app key has not been entered')