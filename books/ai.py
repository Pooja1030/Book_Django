import requests
import json

url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyBegq5rtBhzoJ-nonsLktnH5cxcfIgPHVM'

headers = {
    'Content-Type': 'application/json'
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explain the impact of climate change on agriculture."
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

# Print the response JSON
print(json.dumps(response.json(), indent=4))
