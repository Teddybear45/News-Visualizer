import datetime

import newspaper
from newspaper import news_pool, Config
import time

"""
CNN: Use /year/month/day for articles
CBS: /news
AP: /article
NYT: /year/month/day
WSJ: /news
WP: / *Hard to filter
BBC: /news


"""

# list of sources to map
paper_list = [
    # 'https://cnn.com',  # CNN
    'https://www.cbsnews.com/',  # CBS
    'https://apnews.com/',  # AP
    'https://www.nytimes.com/',  # NYT
    'https://www.wsj.com/',  # WSJ
    'https://www.washingtonpost.com/',  # WP
    'https://www.bbc.com/news',  # BBC

]

config = Config()
config.memoize_articles = False
config.fetch_images = False


def collect():
    start_time = time.time()

    # builds paper from news source list. constant build time of articles
    papers = [newspaper.build(paper, config=config) for paper in paper_list]

    print(time.time() - start_time)

    cnn_articles = source_cnn_collect("http://cnn.com")

    print(time.time() - start_time)

    news_pool.set(papers, threads_per_source=10)
    news_pool.join()

    print(time.time() - start_time)

    for paper in papers:
        for article in paper.articles:
            print(article.url)

    for article in cnn_articles:
        print(article.url)

    print(time.time() - start_time)


def source_cnn_collect(cnn_link):
    source_paper = newspaper.build(cnn_link, config=config)
    articles = []
    d = datetime.date.today()
    date_format = "/" + str(d.year) + "/" + '{:02d}'.format(d.month) + "/" + '{:02d}'.format(d.day)

    for article in source_paper.articles:
        if cnn_link + date_format in article.url:
            articles.append(article)
            article.download()

    return articles


if __name__ == '__main__':
    collect()
