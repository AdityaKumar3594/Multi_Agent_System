from langchain_core.tools import tool
import requests
from tavily import TavilyClient
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
  


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search_tool(query: str) -> str:
    """Search the web for the given query and return the results.Returns Titles,Urls and Snippets of the search results."""
    tavily_response = tavily.search(query,max_results=5)
    results = tavily_response['results']
    output = f"Web search results for: {query}\n"
    for result in results:
        output += f"Title: {result['title']}\nURL: {result['url']}\nSnippet: {result['snippet']}\n\n"
    return output