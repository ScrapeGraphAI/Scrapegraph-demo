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
            "model": model,
            "openai_api_base": base_url,
        },
}

    # ************************************************
    # Create the SmartScraperGraph instance and run it
    # ************************************************

    smart_scraper_graph = SmartScraperGraph(
        prompt=prompt,
        # also accepts a string with the already downloaded HTML code
        source=url,
        config=graph_config
    )

    result = smart_scraper_graph.run()
    return result