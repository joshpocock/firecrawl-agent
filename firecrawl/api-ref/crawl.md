Endpoints
Crawl
POST
https://api.firecrawl.dev/v1/crawl


curl --request POST \
  --url https://api.firecrawl.dev/v1/crawl \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "excludePaths": [
    "<string>"
  ],
  "includePaths": [
    "<string>"
  ],
  "maxDepth": 123,
  "ignoreSitemap": true,
  "limit": 123,
  "allowBackwardLinks": true,
  "allowExternalLinks": true,
  "webhook": "<string>",
  "scrapeOptions": {
    "formats": [
      "markdown"
    ],
    "headers": {},
    "includeTags": [
      "<string>"
    ],
    "excludeTags": [
      "<string>"
    ],
    "onlyMainContent": true,
    "waitFor": 123
  }
}'


import requests

url = "https://api.firecrawl.dev/v1/crawl"

payload = {
    "url": "<string>",
    "excludePaths": ["<string>"],
    "includePaths": ["<string>"],
    "maxDepth": 123,
    "ignoreSitemap": True,
    "limit": 123,
    "allowBackwardLinks": True,
    "allowExternalLinks": True,
    "webhook": "<string>",
    "scrapeOptions": {
        "formats": ["markdown"],
        "headers": {},
        "includeTags": ["<string>"],
        "excludeTags": ["<string>"],
        "onlyMainContent": True,
        "waitFor": 123
    }
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)






{
  "success": true,
  "id": "<string>",
  "url": "<string>"
}


Authorizations
Authorization
string
headerrequired

Bearer authentication header of the form Bearer <token>, where <token> is your auth token.
Body
application/json
url
string
required

The base URL to start crawling from
excludePaths
string[]

URL patterns to exclude
includePaths
string[]

URL patterns to include
maxDepth
integer
default: 2

Maximum depth to crawl relative to the entered URL.
ignoreSitemap
boolean
default: true

Ignore the website sitemap when crawling
limit
integer
default: 10

Maximum number of pages to crawl. Default limit is 10000.
allowBackwardLinks
boolean
default: false

Enables the crawler to navigate from a specific URL to previously linked pages.
allowExternalLinks
boolean
default: false

Allows the crawler to follow links to external websites.
webhook
string

The URL to send the webhook to. This will trigger for crawl started (crawl.started) ,every page crawled (crawl.page) and when the crawl is completed (crawl.completed or crawl.failed). The response will be the same as the /scrape endpoint.
scrapeOptions
object
scrapeOptions.formats
enum<string>[]

Formats to include in the output.
Available options: markdown, 
html, 
rawHtml, 
links, 
screenshot 
scrapeOptions.headers
object

Headers to send with the request. Can be used to send cookies, user-agent, etc.
scrapeOptions.includeTags
string[]

Tags to include in the output.
scrapeOptions.excludeTags
string[]

Tags to exclude from the output.
scrapeOptions.onlyMainContent
boolean
default: true

Only return the main content of the page excluding headers, navs, footers, etc.
scrapeOptions.waitFor
integer
default: 123

Wait x amount of milliseconds for the page to load to fetch content