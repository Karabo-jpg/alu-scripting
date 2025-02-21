#!/usr/bin/python3
"""
This script fetches and prints the titles of the 10 hottest posts from a given subreddit.
If the subreddit exists, the titles of the 10 hottest posts are printed. If the subreddit doesn't exist, 'None' is printed.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        # Subreddit not found
        print("None")
        return
    
    if response.status_code != 200:
        # Handle other status codes, such as server errors
        print("None")
        return
    
    try:
        results = response.json().get("data", {})
        children = results.get("children", [])

        if not children:
            # No posts found
            print("None")
            return

        for post in children:
            print(post.get("data", {}).get("title", "No Title"))

    except ValueError:
        # JSON parsing error
        print("None")
