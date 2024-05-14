import os
import json

import pandas as pd
import streamlit as st

def playwright_install():
    """
    Install playwright browsers
    https://discuss.streamlit.io/t/using-playwright-with-streamlit/28380/11
    """
    with st.spinner("Setting up playwright 🎭"):
        os.system("playwright install")


def add_download_options(result: str):
    """
    Adds download buttons for graph result.
    """
    st.download_button(
        label="Download JSON",
        data=json.dumps(result, indent=4),
        file_name="scraped_data.json",
        mime="application/json"
    )

    df = pd.DataFrame(result)
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="scraped_data.csv",
        mime="text/csv"
    )
