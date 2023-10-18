import requests


api_key = 'if3r105uacv7'

url = f"https://api.ebird.org/v2/product/spplist/US-NC"

payload={}
headers = {
      'X-eBirdApiToken': api_key
}

response = set(requests.request("GET", url, headers=headers, data=payload).json())

print(len(response))
