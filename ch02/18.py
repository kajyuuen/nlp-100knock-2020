import csv

def main():    
    path = "./popular-names.txt"
    with open(path, "r") as f:
        rows = csv.reader(f, delimiter = "\t")
        l = [ row for row in rows ]
    l.sort(key=lambda x: int(x[2]))
    print("\n".join([ "\t".join(li) for li in l]))


if __name__ == "__main__":
    main()