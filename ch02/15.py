import argparse

def main(n):    
    with open("./popular-names.txt", "r") as f:
        line = f.readlines()
    
    print("".join(line[-n:]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()

    main(args.n)