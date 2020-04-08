def main():
    path = "./popular-names.txt"
    with open(path) as f:
        s = f.read()
    print(s.replace("\t", " "))

if __name__ == "__main__":
    main()