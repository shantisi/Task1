import requests
import json
import io
url='https://shantisingh.atlassian.net/rest/api/3/issue/SINGH-54/transitions'
header={
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload=json.dumps({
    "transition":{
        "id":"31"
    }
}
    )
response=requests.get(url,headers=header,data=payload,auth=("shantisingh22@navgurukul.org","CMuKNofdfGFvrg6Rimr599E0"))
print(response.text)