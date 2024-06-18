#!/usr/bin/python3
""" Task zero of Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ A function that queries for number of
    subscribers of the reddit API subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Cappu123"}
    response = requests.get(url,  headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers", 0)
    else:
        return 0
