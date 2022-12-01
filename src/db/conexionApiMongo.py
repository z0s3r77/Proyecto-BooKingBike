import requests
import json
url = "https://data.mongodb-api.com/app/data-cozpc/endpoint/data/v1/action/find"
payload = json.dumps({
    "collection": "bikes",
    "database": "BookingBike",
    "dataSource": "Sandbox",
    "filter": {"Brand":"shimano"},
    "projection":{
      "_id":1,
      "Brand":1,
      "Model":1,
      "Price":1,
      "Status":1
      }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'yvkotEFnlbULNH9Zm14y8LSGZMYcbuA26YF5P9nZlXDpG4LEcEhlJYI3tALDVh5q',
  'Accept': 'application/ejson' 
}
response = requests.request("POST", url, headers=headers, data=payload)
result = (response.text)
result = result.replace('{"documents":',"")
result = result.replace('}',"",-1)
print (result)