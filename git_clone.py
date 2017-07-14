import git
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
git_repos_names = []
for i in resp.json():
    n = i['name']
    try:
        git.Git().clone(i['git_url'])
        print(n + " cloned successfully!")
        # git_repos_names.append(n)
        # print(git_repos_names)
    except git.exc.GitCommandError:
        print(n + " already cloned!")
