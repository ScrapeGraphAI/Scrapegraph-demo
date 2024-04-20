from scrapegraphai.graphs import SpeechGraph

def text_to_speech(api_key: str, prompt: str, url: str):
    """Reads text after the prompt from a given URL.

    Args:
        - api_key (str): OpenAI API key
        - prompt (str): Prompt to use
        - url (str): URL to scrape
    Returns:
        - str: Path to the generated audio file
    """
    llm_config = {"api_key": api_key}
    
    # Define the name of the audio file
    audio_file = "audio_result.mp3"

    # Create and run the speech summary graph
    speech_summary_graph = SpeechGraph(prompt, url, llm_config, audio_file)
    return speech_summary_graph.run()