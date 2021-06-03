from newspaper import Config
from newspaper import Article
import stanza
import time

def parse_paper(passed_article):
    start_time = time.time()

    passed_article.download()
    print(time.time() - start_time)


    passed_article.parse()
    print(time.time() - start_time)

    upper_words = []

    #takes uppercase starting
    for word in passed_article.text.split():
        if word[0].isupper():
            upper_words.append(word)

    return "".join(word + " " for word in upper_words)





def nlp_paper(document):
    start_time = time.time()

    locs = []

    nlp = stanza.Pipeline(lang='en', processors='tokenize,ner')
    print(time.time() - start_time)

    doc = nlp(document)

    print(doc)
    for element in doc.ents:
        if element.type == "LOC":
            locs.append(element.text)

    print(time.time() - start_time)

    return locs





if __name__ == '__main__':
    config = Config()
    config.memoize_articles = False
    config.fetch_images = False


    # print(parse_paper(Article("http://cnn.com/2021/05/31/sport/australia-softball-olympics-spt-intl/index.html", config=config)))

    nlp_paper("The Aussie Spirit, Australian Japan Tokyo Olympics Sydney Monday. The Ota City Japan July Olympic Having February Aussie Spirit, Olympic Japan, Japanese Olympics Japanese Jade Wall. Read More ")


