import requests
import json
from datetime import datetime

url = "https://api.pushshift.io/reddit/comment/search/"
params = {"subreddit": "csgo"}

response = requests.get(url, params=params)

comments = {"data": []}

for text in response.json()["data"]:
    comments["data"].append(
        {
            "author": text["author"],
            "comment": text["body"],
            "date": datetime.utcfromtimestamp(int(text["created_utc"])).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }
    )

with open("comments.json", "w") as fp:
    json.dump(comments, fp, indent=4, ensure_ascii=False)
    fp.close()
