"""
Basic example of scraping pipeline using SpeechSummaryGraph
"""

from scrapegraphai.graphs import SpeechSummaryGraph

def text_to_speech(key:str, prompt:str, url:str):
    """ 
    Given a text it reads after the prompt
    Args:
        - url (str): url to scrape
        - prompt(str): prompt to do
        - key(str) openaikey
    """


    llm_config = {
        "api_key": key
    }

    # Save the audio to a file
    audio_file = "audio_result.mp3"
    speech_summary_graph = SpeechSummaryGraph(prompt,
                                url, llm_config,
                                    audio_file)

    return speech_summary_graph.run()
    