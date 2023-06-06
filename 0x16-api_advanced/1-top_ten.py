#!/usr/bin/python3
"""a function that queries the Reddit API and retñ tye title of he first ten hot poats. """
import requests


def top_ten(subreddit):
    """Function that takes in a subreddit and prints the title offirst ten"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'android:alx_func:v1.0 (by /u/almiviolad)'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        r_json = response.json()
        for post in r_json['data']['children']:
            print(post['data']['title'])

    else:
        print("None")
