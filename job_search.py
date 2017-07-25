import requests


# Check the request response status, if not 200, then exit (and write out infos)
def check_status(resp):
    status = resp.status_code
    if status != 200:
        print("URL: " + resp.url)
        print("Status: " + str(status))
        print("Response message: " + resp.text)
        exit()


# Sorted by population
# Resource: https://en.wikipedia.org/
cities = ["Istanbul", "Moscow", "London", "Saint Petersburg", "Berlin",
          "Madrid", "Kiev", "Rome", "Paris", "Bucharest", "Minsk", "Vienna", "Budapest",
          "Hamburg", "Warsaw", "Barcelona", "Munich", "Kharkiv", "Milan", "Prague",
          "Sofia", "Brussels", "Birmingham", "Odessa", "Naples"]
languages = ["python", "java", "C#"]

url = "https://jobs.github.com/positions.json?full_time=true"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

loc = "&location="
lang = "&description="
for city in cities:
    for l in languages:
        resp = requests.get(url + loc + city + lang + l, headers=headers)
        check_status(resp)
        with open("jobs_res.csv", "a") as text_file:
            text_file.write(l + ", " + str(len(resp.json())) + ", ")
    with open("jobs_res.csv", "a") as text_file:
        text_file.write(city + "\n")
    print(city + " done")
