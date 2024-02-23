from scrapegraphai.evaluators import TrulensEvaluator

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

    llm_config = {
            "api_key": key,
            "model_name": model,
    }

    trulens_evaluator = TrulensEvaluator(key)

    list_of_inputs = [
        (prompt, url, llm_config),
    ]

    return trulens_evaluator.evaluate(list_of_inputs, dashboard=False)
