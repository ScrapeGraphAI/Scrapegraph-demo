from scrapegraphai.graphs import SmartScraperGraph


def task(key:str, url:str, prompt:str, model:str):
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

    graph_config = {
        "llm": {
            "api_key": key,
            "model": model,
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