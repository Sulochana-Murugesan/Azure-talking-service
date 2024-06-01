import requests

url = "https://southeastasia.tts.speech.microsoft.com/cognitiveservices/avatar/relay/token/v1"
subscription_key = "9e841eaeb7974f339115f2e873f2ace7"

headers = {
    "Ocp-Apim-Subscription-Key": subscription_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    ice_info = response.json()
    print("ICE Information:", ice_info)
else:
    print(f"Failed to fetch ICE information. Status code: {response.status_code}")
    print("Response:", response.text)
