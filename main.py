import os
import base64
import streamlit as st
import requests
import json
import pandas as pd
from helper import (
    playwright_install,
    add_download_options
)

st.set_page_config(page_title="Scrapegraph-ai demo", page_icon="🕷️")

# Install playwright browsers
playwright_install()

def save_email(email):
    with open("mails.txt", "a") as file:
        file.write(email + "\n")

with st.sidebar:
    st.write("Official demo for [Scrapegraph-ai](https://github.com/VinciGit00/Scrapegraph-ai) library")
    st.markdown("""---""")
    st.write("# Usage Examples")
    st.write("## Prompt 1")
    st.write("- Give me all the news with their abstracts")
    st.write("## Prompt 2")
    st.write("- Create a voice summary of the webpage")
    st.write("## Prompt 3")
    st.write("- List me all the images with their visual description")
    st.write("## Prompt 4")
    st.write("- Read me the summary of the news")
    st.markdown("""---""")
    st.write("You want to suggest tips or improvements? Contact me through email to mvincig11@gmail.com")
    st.markdown("""---""")
    st.write("Follow our [Github page](https://github.com/ScrapeGraphAI)")


st.title("Scrapegraph-ai")
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("assets/scrapegraphai_logo.png")
st.title('Scrapegraph-api')
st.write("### Refill at this page [Github page](https://scrapegraphai.com)")

# Get the API key, URL, prompt, and optional schema from the user
api_key = st.text_input('Enter your API key:')
url = st.text_input('Enter the URL to scrape:')
prompt = st.text_input('Enter your prompt:')
schema = st.text_input('Enter your optional schema (leave blank if not needed):')

# When the user clicks the 'Scrape' button
if st.button('Scrape'):
    if not api_key.startswith('sgai-'):
        st.error("Invalid API key format. API key must start with 'sgai-'")
    elif not url:
        st.error("Please enter a URL to scrape")
    elif not prompt:
        st.error("Please enter a prompt")
    else:
        # Set up the headers and payload for the API request
        headers = {
            'accept': 'application/json',
            'SGAI-APIKEY': api_key,
            'Content-Type': 'application/json'
        }
        
        payload = {
            'website_url': url,
            'user_prompt': prompt,
            'type': 'object'
        }
        
        # Add schema to payload if provided
        if schema:
            payload['schema'] = schema

        try:
            response = requests.post(
                'https://api.scrapegraphai.com/v1/smartscraper',
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                data = response.json()
                st.write("Result:", data)
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
                
        except Exception as e:
            st.error(f"Error: {str(e)}")


left_co2, *_, cent_co2, last_co2, last_c3 = st.columns([1] * 18)

with cent_co2:
    discord_link = "https://discord.com/invite/gkxQDAjfeX"
    discord_logo = base64.b64encode(open("assets/discord.png", "rb").read()).decode()
    st.markdown(
        f"""<a href="{discord_link}" target="_blank">
        <img src="data:image/png;base64,{discord_logo}" width="25">
        </a>""",
        unsafe_allow_html=True,
    )

with last_co2:
    github_link = "https://github.com/VinciGit00/Scrapegraph-ai"
    github_logo = base64.b64encode(open("assets/github.png", "rb").read()).decode()
    st.markdown(
        f"""<a href="{github_link}" target="_blank">
        <img src="data:image/png;base64,{github_logo}" width="25">
        </a>""",
        unsafe_allow_html=True,
    )

with last_c3:
    twitter_link = "https://twitter.com/scrapegraphai"
    twitter_logo = base64.b64encode(open("assets/twitter.png", "rb").read()).decode()
    st.markdown(
        f"""<a href="{twitter_link}" target="_blank">
        <img src="data:image/png;base64,{twitter_logo}" width="25">
        </a>""",
        unsafe_allow_html=True,
    )
