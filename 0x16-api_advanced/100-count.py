#!/usr/bin/python3
"""
counting words in hot posts
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    recursive func to get the title of all hot posts and print count of given key words
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    children = data["data"]["children"]

    for post in children:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
