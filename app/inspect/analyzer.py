from newspaper import Config
from newspaper import Article
import stanza
import time

from app.source.collector import get_config

# pass in already downloaded
def parse_paper(passed_article):
    start_time = time.time()

    # passed_article.download()
    print(time.time() - start_time)

    passed_article.parse()
    print(time.time() - start_time)

    return passed_article.text


def process_paper(document, pipeline):
    start_time = time.time()

    locs = set()


    print(time.time() - start_time)

    doc = pipeline(document)

    # print(doc)
    for element in doc.ents:
        print(element)
        if element.type == "LOC" or element.type == "GPE":
            locs.add(element.text)

    print(time.time() - start_time)

    return locs




if __name__ == '__main__':


    nlp_pipline = stanza.Pipeline(lang='en', processors='tokenize,ner')

    print(process_paper(parse_paper(
        Article("http://cnn.com/2021/05/31/sport/australia-softball-olympics-spt-intl/index.html", config=get_config())), pipeline=nlp_pipline))

