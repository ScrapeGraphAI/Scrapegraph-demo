import streamlit as st
from task import task
from text_to_speech import text_to_speech

key = st.text_input("Openai API key", type="password")
model = st.radio(
    "Select the model",
    ["gpt-3.5-turbo", "gpt-3.5-turbo-0125", "gpt-4", "text-to-speech", "gpt-4o", "gpt-4o-mini"],
    index=0,
)

url = st.text_input("base url (optional)")
link_to_scrape = st.text_input("Link to scrape")
prompt = st.text_input("Write the prompt")

if st.button("Run the program", type="primary"):
    if not key or not model or not link_to_scrape or not prompt:
        st.error("Please fill in all fields except the base URL, which is optional.")
    else:
        st.write("Scraping phase started ...")

        if model == "text-to-speech":
            res = text_to_speech(key, prompt, link_to_scrape)
            st.write(res["answer"])
            st.audio(res["audio"])
        else:
            # Pass url only if it's provided
            if url:
                graph_result = task(key, link_to_scrape, prompt, model, base_url=url)
            else:
                graph_result = task(key, link_to_scrape, prompt, model)

            print(graph_result)
            st.write("# Answer")
            st.write(graph_result)

            if graph_result:
                add_download_options(graph_result)