#!/usr/bin/python3
"""
first ten title from reddit
"""

from requests import get


def top_ten(subreddit):
    """
    Function that takes in a subreddit and prints the title offirst ten
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'android:alx_func:v1.0 (by /u/almiviolad)'}
    response = get(url, headers=headers)

    if response.status_code == 200:
        r_json = response.json()
        for post in r_json['data']['children']:
            print(post['data']['title'])

    else:
        print("None")
