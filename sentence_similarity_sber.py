from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('ai-forever/sbert_large_nlu_ru')

def sentence_similarity_sber(text1, text2):
    sentences = [text1, text2]
    
    embedding_1= model.encode(sentences[0], convert_to_tensor=True)
    embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

    return util.pytorch_cos_sim(embedding_1, embedding_2)[0][0].item()