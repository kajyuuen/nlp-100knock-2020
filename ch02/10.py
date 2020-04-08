def main():
    path = "./popular-names.txt"
    with open(path) as f:
        s = f.read()
    print(len(s.split("\n")))

if __name__ == "__main__":
    main()