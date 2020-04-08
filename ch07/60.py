from gensim.models import KeyedVectors

def main():
    path = "./GoogleNews-vectors-negative300.bin"
    model = KeyedVectors.load_word2vec_format(path, binary=True)
    print(model["United_States"])

if __name__ == "__main__":
    main()