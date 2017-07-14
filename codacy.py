import requests


# Check the request response status, if not 200, then exit (and wite out infos)
def check_status(resp):
    status = resp.status_code
    if status!=200:
        print("URL: " + resp.url)
        print("Status: " + str(status))
        print("Response message: " + resp.text)
        exit()

# Get all GitHub repository from the given username,
# then order its name and url in a dict
git_usr = input("Enter your github username: ")
url = "https://api.github.com/users/"+git_usr+"/repos"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
resp = requests.get(url, headers=headers)
check_status(resp)
git_repos = {}
for i in resp.json():
    git_repos[i['name']] = i['html_url']

# Get all analysed repo from Codacy, if it possible
url = "https://api.codacy.com/2.0/project"
token = input("Enter your Codacy api token: ")
headers['api_token'] = token
analysed_rep = []
resp = requests.get(url + "/list", headers=headers)
check_status(resp)
list_with_json = resp.json()
if len(list_with_json)>0:
    for i in list_with_json:
        analysed_rep.append(i['name'])

# Analysed every new GitHub repository with Codacy
for i in git_repos:
    if i not in analysed_rep:
        data = '{"url":"'+ git_repos[i] +'", "name":"'+ i +'"}'
        resp = requests.post(url + "/create/public", headers=headers, data=data)
        check_status(resp)
        print(i + " send for Codacy.")
