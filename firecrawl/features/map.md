Map

Input a website and get all the urls on the website - extremly fast
​
Introducing /map (Alpha)

The easiest way to go from a single url to a map of the entire website. This is extremely useful for:

    When you need to prompt the end-user to choose which links to scrape
    Need to quickly know the links on a website
    Need to scrape pages of a website that are related to a specific topic (use the search parameter)
    Only need to scrape specific pages of a website

​
Alpha Considerations

This endpoint prioritizes speed, so it may not capture all website links. We are working on improvements. Feedback and suggestions are very welcome.
​
Mapping
​
/map endpoint

Used to map a URL and get urls of the website. This returns most links present on the website.
​
Installation

pip install firecrawl-py

​
Usage

from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Map a website:
map_result = app.map_url('https://firecrawl.dev')
print(map_result)

​
Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

{
  "status": "success",
  "links": [
    "https://firecrawl.dev",
    "https://www.firecrawl.dev/pricing",
    "https://www.firecrawl.dev/blog",
    "https://www.firecrawl.dev/playground",
    "https://www.firecrawl.dev/smart-crawl",
    ...
  ]
}

​
Map with search

Map with search param allows you to search for specific urls inside a website.
cURL

curl -X POST https://api.firecrawl.dev/v1/map \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://firecrawl.dev",
      "search": "docs"
    }'

Response will be an ordered list from the most relevant to the least relevant.

{
  "status": "success",
  "links": [
    "https://docs.firecrawl.dev",
    "https://docs.firecrawl.dev/sdks/python",
    "https://docs.firecrawl.dev/learn/rag-llama3",
  ]
}
