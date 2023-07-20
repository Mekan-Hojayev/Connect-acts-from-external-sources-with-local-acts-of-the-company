import re

def by_words(doc1: str, doc2: str):
    doc1_words = set(re.sub(r'[^\w\s]', '', doc1, flags=re.UNICODE).lower().split())
    doc2_words = set(re.sub(r'[^\w\s]', '', doc2, flags=re.UNICODE).lower().split())
    total_words = len(doc1_words.union(doc2_words))
    common_words = len(doc1_words.intersection(doc2_words))
    similarity_percentage = (common_words / total_words) * 100
    
    return similarity_percentage