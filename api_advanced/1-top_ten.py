#!/usr/bin/python3
"""Queries the Reddit API and prints the first ten hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first ten hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALCHE API Advanced"}
    params = {"limit": 10}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    for post in posts:
        print(post.get("data", {}).get("title"))