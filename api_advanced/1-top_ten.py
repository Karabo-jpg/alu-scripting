#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    # Construct the URL for the given subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    # Set headers to avoid being blocked by Reddit's API
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Parameters to limit the response to the top 10 posts
    params = {
        "limit": 10
    }

    # Make the GET request without following redirects
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Handle non-existent subreddit (404 status code)
    if response.status_code == 404:
        print("None")
        return

    # If the status code isn't 200 or there's an issue with the response, print None
    if response.status_code != 200:
        print("None")
        return

    try:
        # Parse the response JSON
        data = response.json()

        # Ensure 'data' and 'children' are in the response
        children = data.get('data', {}).get('children', [])

        # If there are no posts or children, print None
        if not children:
            print("None")
            return

        # Print the titles of the top 10 hot posts
        for post in children:
            title = post.get('data', {}).get('title', 'No Title')
            print(title)

    except ValueError:
        # Handle JSON decoding errors and print None
        print("None")
