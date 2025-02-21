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
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # If subreddit does not exist or request fails, print "None"
    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])

        # If no posts are found, print "None"
        if not children:
            print("None")
            return

        # Print the titles of the first 10 posts
        for post in children:
            print(post["data"]["title"])

    except (KeyError, ValueError):
        print("None")
