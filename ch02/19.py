import csv
from collections import Counter

def main():
    path = "./popular-names.txt"

    with open(path, "r") as f:
        rows = csv.reader(f, delimiter = "\t")
        l = [ row[0] for row in rows ]
    
    c = Counter(l)
    for name, cnt in c.most_common():
        print(name)

if __name__ == "__main__":
    main()