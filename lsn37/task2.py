import asyncio
import aiohttp
import json
from datetime import datetime


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


async def get_response(url: str) -> int:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if 200 <= response.status < 300:
                await create_json_file(await response.json())
                return response.status
            return response.status


async def create_json_file(data: dict) -> None:
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


async def main():
    for url in urls:
        await asyncio.create_task(get_response(url))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
