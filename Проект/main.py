import numpy as np
text = open('che.txt', encoding='utf8').read()
corpus = text.split()
def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
pairs = make_pairs(corpus)