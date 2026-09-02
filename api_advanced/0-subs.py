#!/usr/bin/python3
"""Queries the Reddit API and returns a subreddit's subscriber count."""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ALCHE API Advanced"}

    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if response.status_code != 200:
        return 0

    data = response.json()

    return data.get("data", {}).get("subscribers", 0)
