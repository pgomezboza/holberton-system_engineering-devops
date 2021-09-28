#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

url = "https://www.reddit.com/r/{}/hot.json?limit=10"


def top_ten(subreddit):
    headers = {'User-Agent': 'agent-007'}
    res_url = url.format(subreddit)
    response = requests.get(res_url, headers=headers)
    if response.status_code == 200:
        top_titles = response.json().get('data').get('children')
        for title in top_titles:
            print(title.get('data').get('title'))
    else:
        print(None)
