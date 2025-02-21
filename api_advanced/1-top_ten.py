#!/usr/bin/python3
"""
Function to print hot posts on a given Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    # Request subreddit data from Reddit with no redirects
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    # Handle non-existent subreddit (404 error)
    if response.status_code == 404:
        print("None")
        return

    # Handle unsuccessful request (non-200 status codes)
    if response.status_code != 200:
        print("None")
        return

    try:
        # Try to parse the JSON response
        data = response.json()

        # Check if the expected data and children are in the response
        if "data" not in data or "children" not in data["data"]:
            print("None")
            return

        children = data["data"]["children"]

        # If there are no posts, print None
        if not children:
            print("None")
            return

        # Print the titles of the 10 hottest posts
        for post in children:
            title = post.get("data", {}).get("title", "No Title")
            print(title)

    except ValueError:
        # Handle JSON parsing errors
        print("None")
