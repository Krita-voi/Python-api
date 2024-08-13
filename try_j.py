import requests
import json 

url='https://notetaker-f5lt.onrender.com/notes'
response=requests.get(url)

if response.status_code == 200:
    response_content = response.content.decode('utf-8')


    data= json.loads(response_content)


    format_json = json.dump(data, indent= 2)

    print(format_json) 


else:
    print(f"Error in the HTTP requests{response.status_code}")