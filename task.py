from scrapegraphai.graphs import SmartScraperGraph

def task(key:str, url:str, prompt:str, model:str):
    """ 
    Task that execute the scraping:
        - key (str): key of the model
        - url (str): url to scrape 
        - prompt (str): prompt
        - model (str): name of the model
    """ 
    openai_key = key
    llm_config = {
        "api_key": openai_key,
        "model_name": model,
    }

    smart_scraper_graph = SmartScraperGraph(prompt, url, llm_config)

    return smart_scraper_graph.run()
