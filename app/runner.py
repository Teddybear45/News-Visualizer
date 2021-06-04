import stanza

from app.inspect.analyzer import parse_paper, process_paper
from app.source.collector import collect, get_config

if __name__ == '__main__':
    article_list = collect()
    nlp_pipline = stanza.Pipeline(lang='en', processors='tokenize,ner')

    loc_collection = dict()
    for article in article_list:
        article_txt = parse_paper(article)
        locs = process_paper(article_txt, nlp_pipline)
        for loc in locs:
            if loc in loc_collection:
                loc_collection[loc].append(article.url)
            else:
                loc_collection[loc] = [article.url]




    print(loc_collection)
