from gensim.models import KeyedVectors
import numpy as np

def cos_sim(v1, v2): 
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def main():
    path = "./GoogleNews-vectors-negative300.bin"
    model = KeyedVectors.load_word2vec_format(path, binary=True)
    print(cos_sim(model["United_States"], model["U.S."]))

if __name__ == "__main__":
    main()