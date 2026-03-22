import os
from ddgs import DDGS

def _search_ddgs(query):
    results = DDGS().text(query, max_results=5)
    return "\n\n".join([f"Source: {r['href']}\n{r['body']}" for r in results])

def _search_tavily(query):
    from tavily import TavilyClient
    client = TavilyClient()
    response = client.search(query=query, max_results=5)
    return "\n\n".join([f"Source: {r['url']}\n{r['content']}" for r in response["results"]])

def web_search(query):
    provider = os.environ.get("SEARCH_PROVIDER", "ddgs").lower()
    if provider == "tavily":
        return _search_tavily(query)
    return _search_ddgs(query)
