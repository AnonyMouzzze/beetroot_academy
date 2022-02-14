import requests


url = "https://twitter.com/robots.txt"
response = requests.get(url)

with open("robots.txt", "w") as fp:
    fp.write(response.text)
