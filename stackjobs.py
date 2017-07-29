import feedparser

# Sorted by population
# Resource: https://en.wikipedia.org/
cities = ["Istanbul", "Moscow", "London", "Saint Petersburg", "Berlin",
        "Madrid", "Kiev", "Rome", "Paris", "Bucharest", "Minsk", "Vienna", "Budapest",
        "Hamburg", "Warsaw", "Barcelona", "Munich", "Kharkiv", "Milan", "Prague",
        "Sofia", "Brussels", "Birmingham", "Odessa", "Naples"]

languages = ["python", "java", "C#"]

for c in cities:
    for l in languages:
        rss_url = "https://stackoverflow.com/jobs/feed?q="+l+"&l="+c
        f = feedparser.parse(rss_url)
        n = 0
        for i in f.entries:
            n += 1
        with open("jobs_res.csv", "a") as text_file:
            text_file.write(l + ", " + str(n) + ", ")
    with open("jobs_res.csv", "a") as text_file:
        text_file.write(c+"\n")
    print(c + " done")
