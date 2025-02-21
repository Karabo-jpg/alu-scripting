#!/usr/bin/python3
"""
This script fetches and prints the titles of the 10 hottest posts from a given subreddit.
It handles both existing and non-existent subreddits by printing appropriate messages.
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

    # Check if the subreddit exists (status code 404 indicates non-existent subreddit)
    if response.status_code == 404:
        print("None")
        return
    
    # Check if the response contains valid JSON
    if response.status_code != 200:
        print("None")
        return

    try:
        results = response.json().get("data", {})
        children = results.get("children", [])
        
        if not children:
            print("None")
            return
        
        # Print the titles of the 10 hottest posts
        for post in children:
            print(post.get("data", {}).get("title", "No Title"))
    
    except ValueError:
        print("None")
