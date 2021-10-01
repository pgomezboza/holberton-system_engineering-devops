#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json?after={}"
    headers = {'user-agent': 'agent'}
    params = {'limit': after}

    response = requests.get(
                           url.format(subreddit, after),
                           headers=headers,
                           params=params,
                           allow_redirects=False)

    if response.status_code == 200:
        res_json = response.json()
        key = res_json['data']['after']
        body = res_json['data']['children']
        for n in body:
            hot_list.append(n['data']['title'])
        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    else:
        return None
