#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
If the subreddit is invalid, it prints "None".
"""
import requests
import sys

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
        print("None")
        return

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json()
        if 'data' not in data or 'children' not in data['data']:
            print("None")
            return

        children = data['data']['children']

        if not children:
            print("None")
            return

        for post in children:
            title = post.get('data', {}).get('title', 'No Title')
            print(title)

    except (ValueError, KeyError):
        print("None")


# Ensure that if the script is called directly, it receives a subreddit argument
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
