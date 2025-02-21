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
    try:
        results = response.json().get("data")
    except ValueError:
        print("None")
        return
    
    # Check if there are any posts
    if not results or 'children' not in results:
        print("None")
        return

    # Print the titles of the 10 hottest posts
    for post in results.get("children", []):
        print(post.get("data", {}).get("title", "No Title"))
