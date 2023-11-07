#!/usr/bin/python3
"""returning a list containing titles of all articles"""

from requests import get
after = None


def recurse(subreddit, hot_list=[]):
    """to ten post recursively"""

    global after
    headers = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'after': after}

    results = get(url, headers=headers, params=params, allow_redirects=False)

    if results.status_code == 200:
        afterData = results.json().get("data").get("after")

