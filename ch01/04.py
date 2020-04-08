def main():
    string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

    first_char_idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    first_char_idx = [ i - 1 for i in first_char_idx]
    
    result = {}
    for idx, s in enumerate(string.split(" ")):
        if idx in first_char_idx:
            result[s[0]] = idx+1
        else:
            result[s[:2]] = idx+1

    print(result)


if __name__ == "__main__":
    main()