#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
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

    # Requesting the subreddit data from Reddit
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the subreddit does not exist
    if response.status_code == 404:
        print("None")
        return

    # Check if the response is empty or invalid
    if response.status_code != 200 or not response.text.strip():
        print("None")
        return

    try:
        # Parse the response JSON
        results = response.json().get("data", {})
        children = results.get("children", [])

        # Check if there are no posts in the subreddit
        if not children:
            print("None")
            return

        # Print the titles of the 10 hottest posts
        for post in children:
            print(post.get("data", {}).get("title", "No Title"))

    except ValueError:
        # If the response is not a valid JSON, print "None"
        print("None")
