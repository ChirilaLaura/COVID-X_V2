import requests

url = "https://covid-19-data.p.rapidapi.com/totals"

querystring = {"format":"json"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "ef0772bc94msh90c8d83830ca946p12bc46jsn27979572d959"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text["confirmed"]) 
respone.text = dict(response.text)
value =	dict(response.text.values())
print(value)
