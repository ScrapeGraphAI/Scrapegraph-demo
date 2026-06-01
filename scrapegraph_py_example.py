"""Minimal, runnable tour of the scrapegraph-py SDK.

Install the SDK and set your API key, then run this file:

    pip install scrapegraph-py
    export SGAI_API_KEY="sgai-..."   # or pass api_key=... to ScrapeGraphAI()
    python scrapegraph_py_example.py

Every SDK method returns an ``ApiResult`` with ``.status`` ("success" | "error"),
``.data``, ``.error`` and ``.elapsed_ms`` — so there are no exceptions to catch.
Docs: https://github.com/ScrapeGraphAI/scrapegraph-py
"""

import os

from scrapegraph_py import ScrapeGraphAI, MarkdownFormatConfig


def main() -> None:
    # Reads SGAI_API_KEY from the environment, or pass api_key="sgai-..." here.
    api_key = os.environ.get("SGAI_API_KEY")
    sgai = ScrapeGraphAI(api_key=api_key)

    # 1. Credits — check your remaining balance.
    credits = sgai.credits()
    if credits.status == "success":
        print(f"Credits remaining: {credits.data.remaining}")

    # 2. Extract — pull structured data from a URL with a natural-language prompt.
    extract = sgai.extract(
        prompt="Extract the page title and a one-sentence summary",
        url="https://example.com",
    )
    if extract.status == "success":
        print("Extract:", extract.data.json_data or extract.data.raw)
    else:
        print("Extract error:", extract.error)

    # 3. Scrape — get clean markdown for a page.
    scrape = sgai.scrape("https://example.com", formats=[MarkdownFormatConfig()])
    if scrape.status == "success":
        markdown = scrape.data.results.get("markdown", {}).get("data")
        if isinstance(markdown, list):
            markdown = "\n".join(markdown)
        print("Scrape markdown:\n", (markdown or "")[:300])
    else:
        print("Scrape error:", scrape.error)

    # 4. Search — search the web and optionally extract data from the results.
    search = sgai.search("what is web scraping", num_results=3)
    if search.status == "success":
        for result in search.data.results:
            print(f"- {result.title} — {result.url}")
    else:
        print("Search error:", search.error)

    sgai.close()


if __name__ == "__main__":
    main()
