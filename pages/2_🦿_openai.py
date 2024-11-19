import streamlit as st
from task import task
from text_to_speech import text_to_speech

key = st.text_input("Openai API key", type="password")
url = st.text_input("base url (optional)")
link_to_scrape = st.text_input("Link to scrape")
prompt = st.text_input("Write the prompt")

def add_download_options(result):
    """
    Adds download options for the results
    Args:
        result: The result dataframe to make downloadable
    """
    if result:
        # Convert result to CSV
        csv = result.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="scraping_results.csv",
            mime="text/csv"
        )
        
        # Optionally, also add JSON option
        json_str = result.to_json(orient="records")
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="scraping_results.json",
            mime="application/json"
        )

if st.button("Run the program", type="primary"):
    if not key or not link_to_scrape or not prompt:
        st.error("Please fill in all fields except the base URL, which is optional.")
    else:
        st.write("Scraping phase started ...")

        if url:
            graph_result = task(key, link_to_scrape, prompt, base_url=url)
        else:
            graph_result = task(key, link_to_scrape, prompt)

        print(graph_result)
        st.write("# Answer")
        st.write(graph_result)

        if graph_result:
            add_download_options(graph_result)
