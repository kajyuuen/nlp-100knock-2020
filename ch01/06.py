def n_gram(target_list, n):
    result = []
    for i in range(len(target_list)-n+1):
        result.append([target_list[j] for j in range(i, i+n)])
    return result

def main():
    string_one = "paraparaparadise"
    string_two = "paragraph"

    one_bi_gram = set([ "".join(l) for l in n_gram(string_one, 2)])
    two_bi_gram = set([ "".join(l) for l in n_gram(string_two, 2)])

    print(one_bi_gram | two_bi_gram)
    print(one_bi_gram & two_bi_gram)
    print(one_bi_gram - two_bi_gram)
    print("se" in (one_bi_gram | two_bi_gram))

if __name__ == "__main__":
    main()