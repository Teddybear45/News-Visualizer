from newspaper import Article
import stanza
import time


from app.source.collector import get_config


# pass in already downloaded Articles and returns text body
def parse_paper(passed_article):
    # passed_article.download() # download for test run

    passed_article.parse()

    return passed_article.text


# processes the paper with ner to get location names
def process_paper(document, pipeline):
    locs = set()
    doc = pipeline(document)

    for element in doc.ents:
        if element.type == "LOC" or element.type == "GPE":
            locs.add(element.text)
            print(element.text)


    return locs

def check_ner_res(type):
    pass


if __name__ == '__main__':
    nlp_pipline = stanza.Pipeline(lang='en', processors='tokenize,ner')

    print(process_paper(parse_paper(
        Article("http://cnn.com/2021/05/31/sport/australia-softball-olympics-spt-intl/index.html",
                config=get_config())), pipeline=nlp_pipline))

