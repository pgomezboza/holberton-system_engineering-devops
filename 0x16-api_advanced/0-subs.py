#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests

url = "https://www.reddit.com/r/{}/about.json"


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'agent-007'}
    res_url = url.format(subreddit)
    response = requests.get(res_url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        subscribers = response.json().get('data').get('subscribers')
        return (subscribers)
    return (0)
