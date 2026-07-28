# Reddit API

This project is a personal educational project for learning how to use the Reddit Data API with Python.

## Purpose

The application authenticates with the Reddit API and retrieves publicly available posts and comments from user-specified subreddits. The retrieved data is used locally to practice:

- API authentication
- Working with JSON data
- Data collection
- Data analysis using Python
- Data visualization

## Features

- Authenticate using Reddit OAuth
- Read public subreddit posts
- Read public comments
- Export retrieved data for local analysis
- Respect Reddit API rate limits and policies

## Technologies

- Python 3
- PRAW (Python Reddit API Wrapper)

## Usage

1. Create a Reddit application.
2. Obtain your Client ID and Client Secret.
3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Update your API credentials in `main.py`.
5. Run the script.

```bash
python main.py
```

## Disclaimer

This project is for educational purposes only.

The application is read-only. It does not submit posts, comments, votes, messages, or perform moderation actions.
