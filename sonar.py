import os
import git
import requests


# Check the request response status, if not 200, then exit (and wite out infos)
def check_status(resp):
    status = resp.status_code
    if status != 200:
        print("URL: " + resp.url)
        print("Status: " + str(status))
        print("Response message: " + resp.text)
        exit()


# Initialize properties file for scanner
# Start analysing a project
# (name params is the repo name)
def run_scanner(name):
    with open(name + "/sonar-project.properties", "w") as text_file:
        text_file.write("sonar.projectKey=" + name + "\nsonar.sources=src\nsonar.sourceEncoding=UTF-8")
    os.chdir(name + "/")
    os.system("/etc/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner")
    os.chdir("../")

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
for i in resp.json():
    n = i['name']
    try:
        git.Git().clone(i['git_url'])
        print(n + " cloned successfully!")
    except git.exc.GitCommandError:
        print(n + " already cloned!")
    finally:
        run_scanner(n)
