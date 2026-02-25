import feedparser

def get_google_news(query, max_results=5):
    query = query.replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

    feed = feedparser.parse(url)

    news_list = []
    for entry in feed.entries[:max_results]:
        news_list.append({
            "title": entry.title,
            "link": entry.link
        })

    return news_list