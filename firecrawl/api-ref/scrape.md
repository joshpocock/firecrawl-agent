Endpoints
Scrape
POST
https://api.firecrawl.dev/v1/scrape



curl --request POST \
  --url https://api.firecrawl.dev/v1/scrape \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "formats": [
    "markdown"
  ],
  "onlyMainContent": true,
  "includeTags": [
    "<string>"
  ],
  "excludeTags": [
    "<string>"
  ],
  "headers": {},
  "waitFor": 123,
  "timeout": 123,
  "extract": {
    "schema": {},
    "systemPrompt": "<string>",
    "prompt": "<string>"
  },
  "actions": [
    {
      "type": "wait",
      "milliseconds": 2
    }
  ]
}'


import requests

url = "https://api.firecrawl.dev/v1/scrape"

payload = {
    "url": "<string>",
    "formats": ["markdown"],
    "onlyMainContent": True,
    "includeTags": ["<string>"],
    "excludeTags": ["<string>"],
    "headers": {},
    "waitFor": 123,
    "timeout": 123,
    "extract": {
        "schema": {},
        "systemPrompt": "<string>",
        "prompt": "<string>"
    },
    "actions": [
        {
            "type": "wait",
            "milliseconds": 2
        }
    ]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)




{
  "success": true,
  "data": {
    "markdown": "<string>",
    "html": "<string>",
    "rawHtml": "<string>",
    "screenshot": "<string>",
    "links": [
      "<string>"
    ],
    "actions": {
      "screenshots": [
        "<string>"
      ]
    },
    "metadata": {
      "title": "<string>",
      "description": "<string>",
      "language": "<string>",
      "sourceURL": "<string>",
      "<any other metadata> ": "<string>",
      "statusCode": 123,
      "error": "<string>"
    },
    "llm_extraction": {},
    "warning": "<string>"
  }
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

The URL to scrape
formats
enum<string>[]

Formats to include in the output.
Available options: markdown, 
html, 
rawHtml, 
links, 
screenshot, 
extract, 
screenshot@fullPage 
onlyMainContent
boolean
default: true

Only return the main content of the page excluding headers, navs, footers, etc.
includeTags
string[]

Tags to include in the output.
excludeTags
string[]

Tags to exclude from the output.
headers
object

Headers to send with the request. Can be used to send cookies, user-agent, etc.
waitFor
integer
default: 0

Specify a delay in milliseconds before fetching the content, allowing the page sufficient time to load.
timeout
integer
default: 30000

Timeout in milliseconds for the request
extract
object

Extract object
actions
object[]

Actions to perform on the page before grabbing the content

actions.type
enum<string>
required

Wait for a specified amount of milliseconds
Available options: wait 
actions.milliseconds
integer
required

Number of milliseconds to wait
Response
200 - application/json
success
boolean
data
object
data.markdown
string
data.html
string | null

HTML version of the content on page if html is in formats
data.rawHtml
string | null

Raw HTML content of the page if rawHtml is in formats
data.screenshot
string | null

Screenshot of the page if screenshot is in formats
data.links
string[]

List of links on the page if links is in formats
data.actions
object | null

Results of the actions specified in the actions parameter. Only present if the actions parameter was provided in the request
data.metadata
object
data.llm_extraction
object | null

Displayed when using LLM Extraction. Extracted data from the page following the schema defined.
data.warning
string | null

Can be displayed when using LLM Extraction. Warning message will let you know any issues with the extraction.