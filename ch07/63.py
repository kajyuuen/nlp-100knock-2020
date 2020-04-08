from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

def main():
    path = "./GoogleNews-vectors-negative300.bin"
    model = KeyedVectors.load_word2vec_format(path, binary=True)
    for word, sim in model.most_similar(positive=["Spain", "Athens"], negative=["Madrid"]):
        print(word, sim)

if __name__ == "__main__":
    main()