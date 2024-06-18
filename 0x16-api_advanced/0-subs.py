#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscribers
for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number of
    subscribers for a given subreddit"""
    url = 'https://www.reddit.com/subreddit/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Cappu Agent 1.0'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data.get('data').get('subscribers')
        else:
            return 0
    except requests.RequestException:
        return 0
