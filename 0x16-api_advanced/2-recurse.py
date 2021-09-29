#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit.
"""
import requests

url = "https://www.reddit.com/r/{}/hot.json"


def recurse(subreddit, hot_list=[]):
    headers = {'User-Agent': 'agent-007'}
    parameters = {'after': after}
    response = requests.get(
                           url.format(subreddit),
                           headers=headers,
                           params=params,
                           allow_redirects=False)

    if response.status_code == 200:
        key = response.json().get('data').get('after')
        if key is not None:
            after = key
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title in list_titles:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return (None)
