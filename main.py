import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="RedditAPILearning by u/YOUR_USERNAME"
)

subreddit = reddit.subreddit("python")

print(f"Top posts from r/{subreddit.display_name}\n")

for post in subreddit.hot(limit=5):
    print("-" * 60)
    print(f"Title : {post.title}")
    print(f"Score : {post.score}")
    print(f"Author: {post.author}")
    print(f"URL   : {post.url}")
