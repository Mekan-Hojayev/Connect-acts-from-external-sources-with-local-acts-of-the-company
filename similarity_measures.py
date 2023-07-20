from math import*
from decimal import Decimal
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import spacy
nlp = spacy.load("ru_core_news_sm")

def euclidean_distance(x,y):
    x = nlp(x).vector
    y = nlp(y).vector
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

def manhattan_distance(x,y):
    x = nlp(x).vector
    y = nlp(y).vector
    return sum(abs(a-b) for a,b in zip(x,y))

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

def minkowski_distance(x,y,p_value):
    x = nlp(x).vector
    y = nlp(y).vector
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)

def jaccard_similarity(x,y):

    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)

def square_rooted(x):

    return round(sqrt(sum([a*a for a in x])),3)

def cosine_similarity(x,y):
    x = nlp(x).vector
    y = nlp(y).vector
    numerator = sum(a*b for a,b in zip(x,y))
    denominator = square_rooted(x)*square_rooted(y)
    return round(numerator/float(denominator),3)