import base64
import streamlit as st
import json
import pandas as pd
from task import task
from text_to_speech import text_to_speech

st.set_page_config(page_title="Scrapegraph-ai demo",
    page_icon="🕷️")

with st.sidebar:
    st.write("# Usage Examples")
    st.write("## Prompt 1")
    st.write("- Give me all the news with their abstracts")
    st.write("## Prompt 2")
    st.write("- Create a voice summary of the webpage")
    st.write("## Prompt 3")
    st.write("- List me all the images with their visual description")
    st.write("## Prompt 4")
    st.write("- Read me the summary of the news")

st.title("Scrapegraph-ai")
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("assets/scrapegraphai_logo.png")

key = st.text_input("API key", type="password")
model = st.radio(
    "Select the model",
    ["gpt-3.5-turbo", "gpt-3.5-turbo-0125", "gpt-4", "text-to-speech"],
    index=0,
)

link_to_scrape = st.text_input("Link to scrape")
prompt = st.text_input("Write the prompt")

if st.button("Run the program", type="primary"):
    if not key or not model or not link_to_scrape or not prompt:
        st.error("Please fill in all fields.")
    else:
        st.write("Scraping phase started ...")

        if model ==  "text-to-speech":
            res = text_to_speech(key, prompt, link_to_scrape)
            st.write(res["answer"])
            st.audio(res["audio"])
        else:
            (true_lens_result, graph_result) = task(key, link_to_scrape, prompt, model)

            st.write("# Answer")
            st.write(graph_result[0]) 

            if graph_result[0]:
                json_str = json.dumps(graph_result[0], indent=4)
                df =  pd.DataFrame(graph_result[0])

                st.download_button(
                    label="Download JSON",
                    data=json_str,
                    file_name="scraped_data.json",
                    mime="application/json"
                )

                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="scraped_data.csv",
                    mime="text/csv"
                )

left_co2, *_, cent_co2, last_co2 = st.columns([1]*18)

with cent_co2:
    discord_link = "https://discord.gg/DujC7HG8"
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
