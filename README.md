# Welcome!

## Scripts Contents 
### codacy
###### Requirements
1. GitHub username
2. API token from [Codacy](https://www.codacy.com/)

Get all public repository data from the given Github user and compare with analysed projects on Codacy. 
Then send all not analyzed repo url from the api and you can see your resault on your Codacy dashboard.

### codacy_json
###### Requirements
1. API token from [Codacy](https://www.codacy.com/)

Get analysed projects from Codacy, then write it in a json file (next to the script location).

### job_search
Get number of open positions from 26 european countries via [GitHub Jobs](https://jobs.github.com/) API.

Separated by the following language: python, java, C#. Then write the data in job_res.csv file (next to script location).

### sonar
###### Requirements
1. Running [SonarQube](https://www.sonarqube.org/) server (or docker)
2. Github username

Get all public repository url from the given Github user, then clone this projects (next to script location). 
After that, step in every cloned folder, create unique properties file for the SonarQube scanner and run it.

### stackjobs
Get number of open positions from 26 european countries via [Stackoverflow Jobs](https://stackoverflow.com/jobs) RSS feeds.
(The others are same like job_search script.)

## Notes
- __Codacy api token:__ _Open your account, then click to the API Tokens menu._
- __(All scripts are runnable in standalone.)__  

