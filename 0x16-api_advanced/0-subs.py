#!/usr/bin/python3
"""
number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that takes in a subreddit and retyrns no of users
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'android:alx_func:v1.0 (by /u/almiviolad)'}
    response = requests.get(url, headers=headers)
    r_json = response.json()
    try:
        return (r_json['data']['subscribers'])
    except Exception:
        return 0
