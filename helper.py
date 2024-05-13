import os

import streamlit as st

def playwright_install():
	"""
	Install playwright browsers
	https://discuss.streamlit.io/t/using-playwright-with-streamlit/28380/11
	"""
	with st.spinner("Setting up playwright 🎭"):
		os.system("playwright install")
