from newspaper import Article
import time

def parse_paper(passed_article):
    start_time = time.time()

    passed_article.download()
    passed_article.parse()
    print(passed_article.text)

    elapsed_time = time.time() - start_time

    print(elapsed_time)

