def n_gram(target_list, n):
    result = []
    for i in range(len(target_list)-n+1):
        result.append([target_list[j] for j in range(i, i+n)])
    return result

def main():
    string = "I am an NLPer"
    print(n_gram(string.split(), 2))
    print(n_gram(string, 2))


if __name__ == "__main__":
    main()