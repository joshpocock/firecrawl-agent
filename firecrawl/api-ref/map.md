Endpoints
Map
POST
https://api.firecrawl.dev/v1/map


curl --request POST \
  --url https://api.firecrawl.dev/v1/map \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "<string>",
  "search": "<string>",
  "ignoreSitemap": true,
  "includeSubdomains": true,
  "limit": 123
}'


import requests

url = "https://api.firecrawl.dev/v1/map"

payload = {
    "url": "<string>",
    "search": "<string>",
    "ignoreSitemap": True,
    "includeSubdomains": True,
    "limit": 123
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)


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
search
string

Search query to use for mapping. During the Alpha phase, the 'smart' part of the search functionality is limited to 1000 search results. However, if map finds more results, there is no limit applied.
ignoreSitemap
boolean
default: true

Ignore the website sitemap when crawling
includeSubdomains
boolean
default: false

Include subdomains of the website
limit
integer
default: 5000

Maximum number of links to return
Response
200 - application/json
success
boolean
links
string[]