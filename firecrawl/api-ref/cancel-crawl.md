Endpoints
Cancel Crawl
DELETE
/
https://api.firecrawl.dev/v1/crawl/{id}


curl --request DELETE \
  --url https://api.firecrawl.dev/v1/crawl/{id} \
  --header 'Authorization: Bearer <token>'



import requests

url = "https://api.firecrawl.dev/v1/crawl/{id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.request("DELETE", url, headers=headers)

print(response.text)


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
success
boolean
message
string