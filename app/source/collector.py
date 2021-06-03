import newspaper
from datetime import datetime

from app.inspect.analyzer import parse_paper

"""
CNN: Use /year/month/day for articles
CBS: /news
AP: /article
NYT: /year/month/day
WSJ: /news
WP: / *Hard to filter
BBC: /news


"""

#list of sources to map
paper_list = [
    'http://cnn.com', #CNN
    # 'https://www.cbsnews.com/', #CBS
    # 'https://apnews.com/', #AP
    # 'https://www.nytimes.com/', #NYT
    # 'https://www.wsj.com/', #WSJ
    # 'https://www.washingtonpost.com/', #WP
    # 'https://www.bbc.com/news', #BBC




]


def collect():
    for paper in paper_list:
        if paper == "http://cnn.com":
            source_cnn_build(paper)
        elif paper == "https://www.cbsnews.com/":
            pass


def source_cnn_build(paper):
    current_build = newspaper.build(paper, memoize_articles=False)

    d = datetime.now().today()
    date_format = "/" + str(d.year) + "/" + '{:02d}'.format(d.month) + "/" + '{:02d}'.format(d.day)

    for article in current_build.articles:
        if "http://cnn.com" + date_format in article.url:
            print(article.url)
            parse_paper(article)
            break







if __name__ == '__main__':
    collect()

