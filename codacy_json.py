import requests, json


def check_status(resp):
    status = resp.status_code
    if status != 200:
        print("URL: " + resp.url)
        print("Status: " + str(status))
        print("Response message: " + resp.text)
        exit()

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

url = "https://api.codacy.com/2.0/project/list"
token = input("Enter your Codacy api token: ")
headers['api_token'] = token

resp = requests.get(url, headers=headers)
check_status(resp)

with open("codacy.json", "w") as f:
    json.dump(json.loads(resp.text), f)
