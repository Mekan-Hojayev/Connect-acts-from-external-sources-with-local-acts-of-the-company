from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('sentence-transformers/all-roberta-large-v1')

def sentence_similarity(text1, text2):
    sentences = [text1, text2]
    
    embedding_1= model.encode(sentences[0], convert_to_tensor=True)
    embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

    return util.pytorch_cos_sim(embedding_1, embedding_2)[0][0].item()