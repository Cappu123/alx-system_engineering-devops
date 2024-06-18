#!/usr/bin/python3

"""File for task2 query """

import requests


def top_ten(subreddit):
    """A function that queries the Reddit API and prints
    the first 10 hot posts listed of a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "Cappu Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])

            for post in posts:
                title = post.get('data', {}).get('title', {})
                if title:
                    print(title)
        else:
            print('None')
    except Exception as e:
        print('None')
