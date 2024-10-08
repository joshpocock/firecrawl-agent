Endpoints
Get Crawl Status
GET
/
crawl
https://api.firecrawl.dev/v1/crawl/{id}

curl --request GET \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'


import requests

url = "https://api.firecrawl.dev/v1/crawl/{id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.request("GET", url, headers=headers)

print(response.text)






{
  "status": "<string>",
  "total": 123,
  "completed": 123,
  "creditsUsed": 123,
  "expiresAt": "2023-11-07T05:31:56Z",
  "next": "<string>",
  "data": [
    {
      "markdown": "<string>",
      "html": "<string>",
      "rawHtml": "<string>",
      "links": [
        "<string>"
      ],
      "screenshot": "<string>",
      "metadata": {
        "title": "<string>",
        "description": "<string>",
        "language": "<string>",
        "sourceURL": "<string>",
        "<any other metadata> ": "<string>",
        "statusCode": 123,
        "error": "<string>"
      }
    }
  ]
}




Authorizations
Authorization
string
headerrequired

Bearer authentication header of the form Bearer <token>, where <token> is your auth token.
Path Parameters
id
string
required

The ID of the crawl job
Response
200 - application/json
status
string

The current status of the crawl. Can be scraping, completed, or failed.
total
integer

The total number of pages that were attempted to be crawled.
completed
integer

The number of pages that have been successfully crawled.
creditsUsed
integer

The number of credits used for the crawl.
expiresAt
string

The date and time when the crawl will expire.
next
string | null

The URL to retrieve the next 10MB of data. Returned if the crawl is not completed or if the response is larger than 10MB.
data
object[]

The data of the crawl.
data.markdown
string
data.html
string | null

HTML version of the content on page if includeHtml is true
data.rawHtml
string | null

Raw HTML content of the page if includeRawHtml is true
data.links
string[]

List of links on the page if includeLinks is true
data.screenshot
string | null

Screenshot of the page if includeScreenshot is true
data.metadata
object
data.metadata.title
string
data.metadata.description
string
data.metadata.language
string | null
data.metadata.sourceURL
string
data.metadata.<any other metadata>
string
data.metadata.statusCode
integer

The status code of the page
data.metadata.error
string | null

The error message of the page