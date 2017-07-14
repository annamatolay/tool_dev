import os
import git
import requests


def run_scanner(name):
    # for name in repo_names:
        # os.system("cd example/" + name + "/")
        with open(name + "/sonar-project.properties", "w") as text_file:
            text_file.write("sonar.projectKey=" + name + "\nsonar.sources=src\nsonar.sourceEncoding=UTF-8")
        os.chdir(name + "/")
        # os.system("ls")
        os.system("/etc/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner")
        # os.system("cd "+name+"/")
        os.chdir("../")
        # os.system("ls")


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
# git_repos_names = []
for i in resp.json():
    n = i['name']
    try:
        git.Git().clone(i['git_url'])
        print(n + " cloned successfully!")
        # git_repos_names.append(n)
        # print(git_repos_names)
    except git.exc.GitCommandError:
        print(n + " already cloned!")
    finally:
        run_scanner(n)

# run_scanner(['java-codecov-example-master', "some_scripts"])
# temp = git_clone.start()
# print(temp)
# run_scanner(git_clone.start())
