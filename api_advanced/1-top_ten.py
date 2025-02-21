#!/usr/bin/python3
"""
Function to print hot posts on a given Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": (
            "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
        )
    }
    params = {
        "limit": 10
    }

    # Send the GET request to Reddit API
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    # Check if the subreddit exists by checking status code
    if response.status_code == 404:
        print("None")
        return

    # Check for successful response
    if response.status_code != 200:
        print("None")
        return

    try:
        # Parse the JSON response
        data = response.json()

        # Ensure the expected structure is present
        if 'data' not in data or 'children' not in data['data']:
            print("None")
            return

        children = data['data']['children']

        # If there are no posts in the subreddit, print "None"
        if not children:
            print("None")
            return

        # Print the titles of the posts
        for post in children:
            title = post.get('data', {}).get('title', 'No Title')
            print(title)

    except (ValueError, KeyError):
        # If parsing or data extraction fails, print "None"
        print("None")


# Main guard to ensure it runs when called directly
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
