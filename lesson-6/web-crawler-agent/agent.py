from scraper import web_scrape

def agent(query):
    if "crawl this url:" in query.lower():
        url = query.split(":", 1)[1].strip()
        print("[Agent] Using tool: web_scrape")
        return web_scrape(url)

    return "Please provide a valid crawl request like: Crawl this URL: https://example.com"