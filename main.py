import base64
import json

import pandas as pd
import streamlit as st

from scrapegraph_py import (
    ScrapeGraphAI,
    FetchConfig,
    MarkdownFormatConfig,
    HtmlFormatConfig,
    LinksFormatConfig,
    ImagesFormatConfig,
    SummaryFormatConfig,
)

st.set_page_config(page_title="ScrapeGraphAI demo", page_icon="🕷️")


def parse_schema(raw: str) -> dict | None:
    """Parse an optional JSON schema entered by the user."""
    raw = (raw or "").strip()
    if not raw:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        st.warning(f"Schema is not valid JSON, ignoring it: {exc}")
        return None


def render_download_buttons(payload, key: str) -> None:
    """Offer JSON (always) and CSV (when tabular) downloads for a result."""
    st.download_button(
        label="Download JSON",
        data=json.dumps(payload, indent=2, ensure_ascii=False),
        file_name="scrapegraph_result.json",
        mime="application/json",
        key=f"json-{key}",
    )
    rows = payload if isinstance(payload, list) else [payload]
    if rows and all(isinstance(r, dict) for r in rows):
        try:
            csv = pd.DataFrame(rows).to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="scrapegraph_result.csv",
                mime="text/csv",
                key=f"csv-{key}",
            )
        except Exception:
            pass


with st.sidebar:
    st.write(
        "Official demo for the [scrapegraph-py]"
        "(https://github.com/ScrapeGraphAI/scrapegraph-py) SDK."
    )
    st.markdown("""---""")
    st.write("# How it works")
    st.write(
        "This app calls the [ScrapeGraphAI API](https://scrapegraphai.com) "
        "through the official Python SDK. Pick a service, paste your API key, "
        "and run it:"
    )
    st.write("- **Extract** — AI-structured data from a URL via a prompt")
    st.write("- **Scrape** — clean markdown / html / links / images / summary")
    st.write("- **Search** — search the web and optionally extract data")
    st.markdown("""---""")
    st.write("Grab an API key on the [dashboard](https://dashboard.scrapegraphai.com).")
    st.markdown("""---""")
    st.write("Follow us on [GitHub](https://github.com/ScrapeGraphAI)")


st.title("ScrapeGraphAI")
left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("assets/scrapegraphai_logo.png")
st.write("### Powered by the [scrapegraph-py](https://github.com/ScrapeGraphAI/scrapegraph-py) SDK")

api_key = st.text_input("Enter your API key:", type="password")
service = st.radio("Service", ["Extract", "Scrape", "Search"], horizontal=True)


def get_client(key: str) -> ScrapeGraphAI:
    return ScrapeGraphAI(api_key=key)


def show_result(result, *, download_key: str, primary=None) -> None:
    """Render an ApiResult: error, primary payload, raw JSON, downloads, timing."""
    if result.status != "success":
        st.error(result.error or "Request failed")
        return
    if primary is not None:
        st.write(primary)
        render_download_buttons(primary, download_key)
    with st.expander("Raw response"):
        st.json(result.data.model_dump(mode="json", by_alias=True))
    st.caption(f"Completed in {result.elapsed_ms} ms")


# --- Extract -----------------------------------------------------------------
if service == "Extract":
    url = st.text_input("URL to extract from:")
    prompt = st.text_input("What do you want to extract?")
    schema_raw = st.text_input("Optional JSON schema (leave blank if not needed):")

    if st.button("Extract"):
        if not (api_key or "").startswith("sgai-"):
            st.error("Invalid API key format. API key must start with 'sgai-'")
        elif not url:
            st.error("Please enter a URL")
        elif not prompt:
            st.error("Please enter a prompt")
        else:
            with st.spinner("Extracting…"):
                with get_client(api_key) as sgai:
                    result = sgai.extract(
                        prompt=prompt,
                        url=url,
                        schema=parse_schema(schema_raw),
                    )
            primary = None
            if result.status == "success":
                primary = result.data.json_data or result.data.raw
            show_result(result, download_key="extract", primary=primary)

# --- Scrape ------------------------------------------------------------------
elif service == "Scrape":
    url = st.text_input("URL to scrape:")
    fmt_choice = st.selectbox(
        "Format",
        ["markdown", "html", "links", "images", "summary"],
        index=0,
    )
    render_js = st.checkbox("Render JavaScript (slower, for dynamic pages)")

    if st.button("Scrape"):
        if not (api_key or "").startswith("sgai-"):
            st.error("Invalid API key format. API key must start with 'sgai-'")
        elif not url:
            st.error("Please enter a URL")
        else:
            fmt_map = {
                "markdown": MarkdownFormatConfig(),
                "html": HtmlFormatConfig(),
                "links": LinksFormatConfig(),
                "images": ImagesFormatConfig(),
                "summary": SummaryFormatConfig(),
            }
            fetch_config = FetchConfig(mode="js") if render_js else None
            with st.spinner("Scraping…"):
                with get_client(api_key) as sgai:
                    result = sgai.scrape(
                        url,
                        formats=[fmt_map[fmt_choice]],
                        fetch_config=fetch_config,
                    )
            primary = None
            if result.status == "success":
                entry = result.data.results.get(fmt_choice)
                # markdown/html come back as {"data": ...}; links/images as lists
                if isinstance(entry, dict) and "data" in entry:
                    primary = entry["data"]
                else:
                    primary = entry
                if isinstance(primary, list) and primary and isinstance(primary[0], str):
                    primary = "\n".join(primary)
            show_result(result, download_key="scrape", primary=primary)

# --- Search ------------------------------------------------------------------
else:
    query = st.text_input("Search query:")
    num_results = st.slider("Number of results", min_value=1, max_value=20, value=3)
    prompt = st.text_input("Optional extraction prompt (leave blank for raw results):")

    if st.button("Search"):
        if not (api_key or "").startswith("sgai-"):
            st.error("Invalid API key format. API key must start with 'sgai-'")
        elif not query:
            st.error("Please enter a search query")
        else:
            with st.spinner("Searching…"):
                with get_client(api_key) as sgai:
                    result = sgai.search(
                        query,
                        num_results=num_results,
                        prompt=(prompt or None),
                    )
            if result.status == "success":
                if result.data.json_data:
                    st.write(result.data.json_data)
                results = [r.model_dump(mode="json") for r in result.data.results]
                for item in results:
                    st.markdown(f"**[{item['title']}]({item['url']})**")
                    st.write(item["content"][:500])
                    st.markdown("---")
                render_download_buttons(results, "search")
                with st.expander("Raw response"):
                    st.json(result.data.model_dump(mode="json", by_alias=True))
                st.caption(f"Completed in {result.elapsed_ms} ms")
            else:
                st.error(result.error or "Request failed")


# --- Footer: social links ----------------------------------------------------
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
    github_link = "https://github.com/ScrapeGraphAI/scrapegraph-py"
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
