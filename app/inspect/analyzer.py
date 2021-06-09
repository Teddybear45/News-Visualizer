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



