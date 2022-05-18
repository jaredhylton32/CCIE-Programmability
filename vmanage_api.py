import requests
import json
from pprint import pprint

url = "https://192.168.9.14:443/dataservice/system/device/management/systemip"

payload='='
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4=',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'JSESSIONID=d9V7LCWU1VZUj6t1j4QBvy7quk7eq0dANhmadap4.226c5b57-2208-4c8f-8109-10ff1db9e21d'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

# print(response.text)

response_out = json.loads(response.text)['data']
pprint(response_out)




# for i in response_out:
#   pprint(i)
