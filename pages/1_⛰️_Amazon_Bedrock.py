r"""
Bedrock Scrapper with ScrapeGraphAI
 /\ \  / /\
//\\ .. //\\
//\((  ))/\\
/  < `' >  \
"""

import os

import streamlit as st

from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.helpers import models_tokens

from langchain_core.exceptions import OutputParserException

st.set_page_config(page_title="Bedrock Scraper", page_icon="🕷️")
st.title("Bedrock Scraper 🕷️")

# 0a. Check supported models
supported_models = list(models_tokens['bedrock'].keys())
embed_models = [model for model in supported_models if "embed" in model]
text_models = list(set(supported_models) - set(embed_models))

# 0b. Get user input

llm = st.selectbox(
    label="Select model",
    options=text_models
)

temperature = st.sidebar.slider(
    label="> Temperature",
    min_value=0.0,
    max_value=1.0
)

model_tokens = st.sidebar.slider(
    label="> Model Tokens",
    min_value=0,
    max_value=models_tokens['bedrock'][llm],
    value=models_tokens['bedrock'][llm]
)

embedder = st.selectbox(
    label="Select embedder",
    options=embed_models
)

with st.expander("Set up AWS credentials 🔑", expanded=False):
    st.markdown("❗ Use [temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) whenever possible")
    with st.form("AWS Credentials", clear_on_submit=True):
        os.environ['AWS_ACCESS_KEY_ID'] = st.text_input("AWS Access Key ID", type="password")
        os.environ['AWS_SECRET_ACCESS_KEY'] = st.text_input("AWS Secret Access Key", type="password")
        os.environ['AWS_SESSION_TOKEN'] = st.text_input("AWS Session Token", type="password")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.info("AWS credentials updated!")

source = st.text_input(
    label="Link to scrape"
)

prompt = st.text_area(
    label="Write the prompt"
)

# 1. Define graph configuration
config = {
    "llm": {
        "model": f"bedrock/{llm}",
        "temperature": temperature,
        "format": "json"
    },
    "embeddings": {
        "model": f"bedrock/{embedder}"
    },
}

# 2. Create graph instance
graph = SmartScraperGraph(
    prompt=prompt,
    source=source,
    config=config
)

# 3. Scrape away!
def run():
    """Execute graph and return result"""
    st.session_state.output = None
    try:
        st.session_state.output = graph.run()
    except OutputParserException as ex:
        st.error(ex)

run = st.button(
    label="Run",
    on_click=run
)

if st.session_state.get('output', None):
    st.json(st.session_state.output)
