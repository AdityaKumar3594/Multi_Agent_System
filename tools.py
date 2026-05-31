# This file defines two tools: `web_search_tool` and `web_scraping_tool`. The `web_search_tool` uses the Tavily API to perform a web search based on a given query and returns the titles, URLs, and snippets of the search results. The `web_scraping_tool` takes a URL as input, fetches the content of the page, and returns the text while removing unnecessary tags for cleaner output. Both tools are decorated with `@tool` from the `langchain_core` library, making them easily integrable into a larger system that utilizes these functionalities.


#import necessary libraries and load environment variables
from langchain_core.tools import tool
import requests
from tavily import TavilyClient
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
from rich import print
  

# Initialize the Tavily client with the API key from environment variables
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

#Web search tool to search the web for a given query and return the results. It uses the Tavily API to perform the search and returns the titles, URLs, and snippets of the search results.
@tool
def web_search_tool(query: str) -> str:
    """Search the web for the given query and return the results.Returns Titles,Urls and Snippets of the search results."""
    tavily_response = tavily.search(query,max_results=5)
    out=[]
    for item in tavily_response['results']:
        title = item['title']
        url = item['url']
        snippet = item['content']
        out.append(f"Title: {title}\nURL: {url}\nSnippet: {snippet}\n")
    return "\n".join(out)

#Web scraping tool to scrape the content of a given URL and return the text. It uses requests to fetch the page and BeautifulSoup to parse the HTML and extract the text content, while removing script, style, nav, and footer tags to get cleaner text. The result is limited to 3000 characters to avoid overwhelming the output.
@tool
def web_scraping_tool(url: str) -> str:
    """Scrape the content of the given URL and return the text."""
    try:
        response = requests.get(url, timeout=8, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup(['script', 'style', 'nav', 'footer']):
            tag.decompose()
        return soup.get_text(sep=" ", strip=True)[:3000] 
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"