#!/usr/bin/python3
"""Recursively counts keywords in subreddit hot article titles."""

import re
import requests


def count_words(subreddit, word_list):
    """Print a sorted count of keywords in hot article titles."""
    words = {}

    for word in word_list:
        word = word.lower()
        words[word] = words.get(word, 0) + 1

    counts = {}
    _count_words(subreddit, words, counts)

    sorted_counts = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    for word, count in sorted_counts:
        print("{}: {}".format(word, count))


def _count_words(subreddit, words, counts, after=None):
    """Recursively retrieve hot posts and count keyword occurrences."""
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
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()

        for word, multiplier in words.items():
            pattern = r"(?<!\w){}(?!\w)".format(re.escape(word))
            matches = re.findall(pattern, title)

            if matches:
                counts[word] = (
                    counts.get(word, 0) +
                    len(matches) * multiplier
                )

    after = data.get("after")

    if after is not None:
        _count_words(subreddit, words, counts, after)
