#!/usr/bin/python3
"""Recursively retrieves all hot post titles from a subreddit."""

import requests

def recurse(subreddit, hot_list=None, after=None):
"""Return a list containing all hot article titles recursively."""
if hot_list is None:
hot_list = []

```
url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
headers = {"User-Agent": "ALCHE API Advanced"}
params = {"limit": 100}

if after is not None:
    params["after"] = after

response = requests.get(
    url,
    headers=headers,
    params=params,
    allow_redirects=False
)

if response.status_code != 200:
    return None

data = response.json().get("data", {})
posts = data.get("children", [])

for post in posts:
    title = post.get("data", {}).get("title")
    hot_list.append(title)

after = data.get("after")

if after is None:
    return hot_list

return recurse(subreddit, hot_list, after)
```
