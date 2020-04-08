import csv

def main():    
    path = "./popular-names.txt"
    with open(path, "r") as f:
        rows = csv.reader(f, delimiter = "\t")
        col_one = [ row[0] for row in rows ]
    print(set(col_one))


if __name__ == "__main__":
    main()