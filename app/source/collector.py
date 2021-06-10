import datetime

import newspaper
import stanza
from newspaper import news_pool, Config
import time

# sources
"""
CNN: Use /year/month/day for articles
CBS: /news
AP: /article
NYT: /year/month/day
WSJ: /news
WP: / *Hard to filter
BBC: /news
ABC: .go.com/SECTION/SECTION || TITLE *Hard to filter
The Atlantic: latest/SECTION/archive/year/month
NBC: /SECTION


"""

# list of sources to map
paper_list = [
    # 'https://cnn.com',  # CNN / Separate finder
    # 'https://www.wsj.com/',  # WSJ // Not extracting
    'https://www.cbsnews.com/',  # CBS
    'https://apnews.com/',  # AP
    'https://www.nytimes.com/',  # NYT
    'https://www.washingtonpost.com/',  # WP
    'https://www.bbc.com/news',  # BBC
    'https://abcnews.go.com/',  # ABC
    'https://www.theatlantic.com/',  # The Atlantic
    'https://www.nbcnews.com/latest-stories',  # NBC
    'https://www.usatoday.com/',  # USA Today
    'https://www.theguardian.com/us',  # The Guardian
    'https://time.com/',  # TIME
    'https://www.npr.org/',  # NPR

]


# config for newspaper build
def get_config():
    config = Config()
    config.memoize_articles = True
    config.fetch_images = False

    return config


# collects newspapers into newspaper Article objects
def collect():
    start_time = time.time()

    # builds paper from news source list. constant build time of articles
    papers = [newspaper.build(paper, config=get_config()) for paper in paper_list]
    # separate CNN collect
    cnn_articles = source_cnn_collect("http://cnn.com")

    news_pool.set(papers, threads_per_source=10)
    news_pool.join()

    article_list = []

    for paper in papers:
        for article in paper.articles:
            article_list.append(article)

    for article in cnn_articles:
        article_list.append(article)

    return article_list


# CNN special collect to filter out other languages and only take today's articles
def source_cnn_collect(cnn_link):
    source_paper = newspaper.build(cnn_link, config=get_config())
    articles = []
    d = datetime.date.today()
    date_format = "/" + str(d.year) + "/" + '{:02d}'.format(d.month) + "/" + '{:02d}'.format(d.day)

    for article in source_paper.articles:
        if cnn_link + date_format in article.url:
            articles.append(article)
            article.download()

    return articles
