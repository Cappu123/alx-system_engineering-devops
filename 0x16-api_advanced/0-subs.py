#!/usr/bin/python3

"""
for returning number of subscribers for the given subreddit
"""

"""Import the python request module to fetch http requests
"""
import requests

def number_of_subscribers(subreddit):
    """A function that queiries the Reddit API and
    returns the number of subscribers
    """
    url = f"https://reddit.com/{subreddit}/about.json()"
    """Define the header including User-Agent
    as per the Reddit API access rules
    """
    headers = {'User-Agent': 'cappu reddit 1.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data.get("data").get("subscribers")
        else:
            return 0
    except requests.RequestException:
        return 0
