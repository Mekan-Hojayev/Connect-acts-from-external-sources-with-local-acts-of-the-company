import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import spacy
nlp = spacy.load("ru_core_news_sm")

def text_similarity(text1: str, text2: str):
    text1_nlp = nlp(text1)
    text2_nlp = nlp(text2) 

    print('Similarity score of documents is:', text1_nlp.similarity(text2_nlp))