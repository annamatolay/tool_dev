import os


def run_scanner(repo_names=[]):
    for name in repo_names:
        # os.system("cd example/" + name + "/")
        with open(name + "/sonar-project.properties", "w") as text_file:
            text_file.write("sonar.projectKey=" + name + "\nsonar.sources=src\nsonar.sourceEncoding=UTF-8")
        os.chdir(name + "/")
        # os.system("ls")
        os.system("/etc/sonar-scanner-3.0.3.778-linux/bin/sonar-scanner")
        # os.system("cd "+name+"/")
        os.chdir("../")
        # os.system("ls")

run_scanner(['java-codecov-example-master', "some_scripts"])
# temp = git_clone.start()
# print(temp)
# run_scanner(git_clone.start())
