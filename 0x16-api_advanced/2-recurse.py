#!/usr/bin/python3
"""Query file for task3 """
import requests


def recurse(subreddit, hot_list=[]):
    """A recursive function to query Reddit API and returns
    a list having the titles of all hot articles for a
    given subreddit, if no returns None"""

    url = "https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Cappu Agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    if not posts:
        return hot_list

    for post in posts:
        title = post.get('data', {}).get{'title')
        hot_list.append(title)

        if data.get('data', {}).get('after'):
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
