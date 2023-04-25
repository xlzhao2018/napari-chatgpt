# Code vendored from: https://github.com/Nv7-GitHub/googlesearch/blob/master/googlesearch/__init__.py
from langchain.llms import BaseLLM

from napari_chatgpt.utils.duckduckgo import summary_ddg, search_ddg
from napari_chatgpt.utils.google import search_google
from napari_chatgpt.utils.scrapper import text_from_url
from napari_chatgpt.utils.summarizer import summarize


def search_wikipedia(query: str,
                     num_results: int = 3,
                     max_text_length: int = 4000,
                     do_summarize: bool = False,
                     llm: BaseLLM = None) -> str:


    # Run a google search specifically on wikipedia:
    results = search_ddg(query=f"{query} site:wikipedia.org", num_results=max(10, num_results))

    # keep the top k results:
    results = results[0: num_results]

    # Get pages summaries:
    text = '\n\n'.join([r['body'] for r in results])

    # Limit text length:
    text = text[:max_text_length]

    if do_summarize:
        text = summarize(text, llm=llm)

    return text
