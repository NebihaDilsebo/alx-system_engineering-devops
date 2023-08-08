import requests

def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    headers = {'User-Agent': 'MyBot/1.0'}  # Set a user agent header
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100}
    
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        posts = data['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                word = word.lower()
                if word in title:
                    counts[word] = counts.get(word, 0) + title.count(word)

        after = data['after']

        if after:
            count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print("Invalid subreddit or error occurred")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)

