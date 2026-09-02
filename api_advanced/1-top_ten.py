#!/usr/bin/python3
"""Queries the Reddit API and prints the first ten hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first ten hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (ALCHE API Advanced)"
    }

    response = requests.get(
        url,
        headers=headers,
        params={"limit": 10},
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))
        