#!/usr/bin/python3
"""
Function to print the titles of the first 10 hot posts on a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    if not isinstance(subreddit, str) or subreddit == "":
        print("None")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=5)

        if response.status_code != 200:
            print("None")
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            print("None")
            return

        for post in children:
            print(post["data"].get("title", "None"))

    except (requests.RequestException, KeyError, ValueError):
        print("None")
