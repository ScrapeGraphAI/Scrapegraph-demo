r"""
Bedrock Scrapper with ScrapeGraphAI
 /\ \  / /\
//\\ .. //\\
//\((  ))/\\
/  < `' >  \
"""

import os
import boto3

import streamlit as st

from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.helpers import models_tokens

from langchain_core.exceptions import OutputParserException

from helper import playwright_install

SUPPORTED_AWS_REGIONS = [
    "us-east-1",
    "us-east-2",
    "us-west-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-northeast-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-3"
]

if 'AWS_DEFAULT_REGION' not in os.environ:
    os.environ['AWS_DEFAULT_REGION'] = SUPPORTED_AWS_REGIONS[0]

st.set_page_config(page_title="Bedrock Scraper", page_icon="🕷️")
st.title("Bedrock Scraper 🕷️")

# -1. Install playwright browsers
playwright_install()

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
        aws_access_key_id = st.text_input("AWS Access Key ID", type="password")
        aws_secret_access_key = st.text_input("AWS Secret Access Key", type="password")
        aws_session_token = st.text_input("AWS Session Token", type="password")
        region_name = st.selectbox(
            "Region",
            options=SUPPORTED_AWS_REGIONS
        )
        submitted = st.form_submit_button("Submit")
        if submitted:
            session = boto3.Session(
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                aws_session_token=aws_session_token,
                region_name=region_name
            )
            st.session_state.client = session.client("bedrock-runtime")
            st.info("AWS credentials updated!")

source = st.text_input(
    label="Link to scrape"
)

prompt = st.text_area(
    label="Write the prompt"
)

# 1. Define graph configuration
if 'client' not in st.session_state:
    st.session_state.client = None

config = {
    "llm": {
        "client": st.session_state.client,
        "model": f"bedrock/{llm}",
        "temperature": temperature,
        "format": "json"
    },
    "embeddings": {
        "client": st.session_state.client,
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
