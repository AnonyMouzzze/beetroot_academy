import requests
import concurrent.futures
import json
from datetime import datetime


request = requests.Session()


def create_urls() -> list:
    subreddits = [
        "csgo",
        "batman",
        "travis",
        "nike",
        "audi",
        "nvidia",
        "tesla",
        "spacex",
        "bitcoin",
        "mask",
        "barcelona",
    ]
    urls = []

    for subreddit in subreddits:
        url = f"https://api.pushshift.io/reddit/comment/search/?subreddit={subreddit}"
        urls.append(url)
    return urls


def get_response(url: str) -> int:
    response = requests.get(url)

    if response.ok:
        create_json_file(response.json())
        return response.status_code
    return response.status_code


def create_json_file(data: dict) -> None:
    processed_comments = {"comments": []}
    subreddit = data["data"][0]["subreddit"]

    for comment in data["data"]:
        processed_comments["comments"].append(
            {
                "author": comment["author"],
                "comment": comment["body"],
                "date": datetime.utcfromtimestamp(int(comment["created_utc"])).strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
            }
        )

    with open(f"{subreddit}", "w") as fp:
        json.dump(processed_comments, fp, indent=4)
        fp.close()


urls = create_urls()

with concurrent.futures.ThreadPoolExecutor(3) as executor:
    workers = []
    for url in urls:
        workers.append(executor.submit(get_response, url))
    for worker in concurrent.futures.as_completed(workers):
        print(worker.result())
