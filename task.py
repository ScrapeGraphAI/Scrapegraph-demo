from scrapegraphai.graphs import SmartScraperGraph

def task(key:str, url:str, prompt:str, model:str, base_url=None):
    """ 
    Task that execute the scraping:
        Arguments:
        - key (str): key of the model
        - url (str): url to scrape 
        - prompt (str): prompt
        - model (str): name of the model
        Return:
        - results_df["output"] (dict): result as a dictionary
        - results_df (pd.Dataframe()): result as padnas df
    """ 
    if base_url is not None:
        graph_config = {
            "llm": {
                "api_key": key,
                "model": model,
            },
        }
    else: 
        graph_config = {
        "llm": {
            "api_key": key,
            "model": "openai/gpt-4",
        },
}

    print(prompt)
    print(url)
    print(graph_config)
    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt,
        source=url,
        config=graph_config
    )

    result = smart_scraper_graph.run()
    return result