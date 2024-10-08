Get Started
Welcome to V1

Firecrawl allows you to turn entire websites into LLM-ready markdown

Firecrawl V1 is here! With that we introduce a more reliable and developer friendly API.

Here is what’s new:

    Output Formats for /scrape. Choose what formats you want your output in.
    New /map endpoint for getting most of the URLs of a webpage.
    Developer friendly API for /crawl/{id} status.
    2x Rate Limits for all plans.
    Go SDK and Rust SDK
    Teams support
    API Key Management in the dashboard.
    onlyMainContent is now default to true.
    /crawl webhooks and websocket support.

​
Scrape Formats

You can now choose what formats you want your output in. You can specify multiple output formats. Supported formats are:

    Markdown (markdown)
    HTML (html)
    Raw HTML (rawHtml) (with no modifications)
    Screenshot (screenshot or screenshot@fullPage)
    Links (links)

Output keys will match the format you choose.

from firecrawl import FirecrawlApp

app = FirecrawlApp(api_key="fc-YOUR_API_KEY")

# Scrape a website:
scrape_result = app.scrape_url('firecrawl.dev', params={'formats': ['markdown', 'html']})
print(scrape_result)

​
Response

SDKs will return the data object directly. cURL will return the payload exactly as shown below.

{
  "success": true,
  "data" : {
    "markdown": "Launch Week I is here! [See our Day 2 Release 🚀](https://www.firecrawl.dev/blog/launch-week-i-day-2-doubled-rate-limits)[💥 Get 2 months free...",
    "html": "<!DOCTYPE html><html lang=\"en\" class=\"light\" style=\"color-scheme: light;\"><body class=\"__variable_36bd41 __variable_d7dc5d font-inter ...",
    "metadata": {
      "title": "Home - Firecrawl",
      "description": "Firecrawl crawls and converts any website into clean markdown.",
      "language": "en",
      "keywords": "Firecrawl,Markdown,Data,Mendable,Langchain",
      "robots": "follow, index",
      "ogTitle": "Firecrawl",
      "ogDescription": "Turn any website into LLM-ready data.",
      "ogUrl": "https://www.firecrawl.dev/",
      "ogImage": "https://www.firecrawl.dev/og.png?123",
      "ogLocaleAlternate": [],
      "ogSiteName": "Firecrawl",
      "sourceURL": "https://firecrawl.dev",
      "statusCode": 200
    }
  }
}

​
Introducing /map (Alpha)

The easiest way to go from a single url to a map of the entire website.
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
WebSockets

To crawl a website with WebSockets, use the Crawl URL and Watch method.

# inside an async function...
nest_asyncio.apply()

# Define event handlers
def on_document(detail):
    print("DOC", detail)

def on_error(detail):
    print("ERR", detail['error'])

def on_done(detail):
    print("DONE", detail['status'])

    # Function to start the crawl and watch process
async def start_crawl_and_watch():
    # Initiate the crawl job and get the watcher
    watcher = app.crawl_url_and_watch('firecrawl.dev', { 'excludePaths': ['blog/*'], 'limit': 5 })

    # Add event listeners
    watcher.add_event_listener("document", on_document)
    watcher.add_event_listener("error", on_error)
    watcher.add_event_listener("done", on_done)

    # Start the watcher
    await watcher.connect()

# Run the event loop
await start_crawl_and_watch()

​
Extract format

LLM extraction is now available in v1 under the extract format. To extract structured from a page, you can pass a schema to the endpoint or just provide a prompt.

from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field

# Initialize the FirecrawlApp with your API key
app = FirecrawlApp(api_key='your_api_key')

class ExtractSchema(BaseModel):
    company_mission: str
    supports_sso: bool
    is_open_source: bool
    is_in_yc: bool

data = app.scrape_url('https://docs.firecrawl.dev/', {
    'formats': ['extract'],
    'extract': {
        'schema': ExtractSchema.model_json_schema(),
    }
})
print(data["extract"])

Output:
JSON

{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
        "supports_sso": true,
        "is_open_source": false,
        "is_in_yc": true
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}

​
Extracting without schema (New)

You can now extract without a schema by just passing a prompt to the endpoint. The llm chooses the structure of the data.

curl -X POST https://api.firecrawl.dev/v1/scrape \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev/",
      "formats": ["extract"],
      "extract": {
        "prompt": "Extract the company mission from the page."
      }
    }'

Output:
JSON

{
    "success": true,
    "data": {
      "extract": {
        "company_mission": "Train a secure AI on your technical resources that answers customer and employee questions so your team doesn't have to",
      },
      "metadata": {
        "title": "Mendable",
        "description": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "robots": "follow, index",
        "ogTitle": "Mendable",
        "ogDescription": "Mendable allows you to easily build AI chat applications. Ingest, customize, then deploy with one line of code anywhere you want. Brought to you by SideGuide",
        "ogUrl": "https://docs.firecrawl.dev/",
        "ogImage": "https://docs.firecrawl.dev/mendable_new_og1.png",
        "ogLocaleAlternate": [],
        "ogSiteName": "Mendable",
        "sourceURL": "https://docs.firecrawl.dev/"
      },
    }
}

​
New Crawl Webhook

You can now pass a webhook parameter to the /crawl endpoint. This will send a POST request to the URL you specify when the crawl is started, updated and completed.

The webhook will now trigger for every page crawled and not just the whole result at the end.
cURL

curl -X POST https://api.firecrawl.dev/v1/crawl \
    -H 'Content-Type: application/json' \
    -H 'Authorization: Bearer YOUR_API_KEY' \
    -d '{
      "url": "https://docs.firecrawl.dev",
      "limit": 100,
      "webhook": "https://example.com/webhook"
    }'

​
Webhook Events

There are now 4 types of events:

    crawl.started - Triggered when the crawl is started.
    crawl.page - Triggered for every page crawled.
    crawl.completed - Triggered when the crawl is completed to let you know it’s done.
    crawl.failed - Triggered when the crawl fails.

​
Webhook Response

    success - If the webhook was successful in crawling the page correctly.
    type - The type of event that occurred.
    id - The ID of the crawl.
    data - The data that was scraped (Array). This will only be non empty on crawl.page and will contain 1 item if the page was scraped successfully. The response is the same as the /scrape endpoint.
    error - If the webhook failed, this will contain the error message.
