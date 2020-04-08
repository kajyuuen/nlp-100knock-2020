import csv

def main():
    path = "./popular-names.txt"
    with open(path, "r") as f:
        rows = csv.reader(f, delimiter = "\t")
        l = [ row for row in rows ]
        col_one = [ l[0] + "\n" for l in l ]
        col_two = [ l[1] + "\n" for l in l ]
    
    with open("./col1.txt", "w") as f:
        f.writelines(col_one)

    with open("./col2.txt", "w") as f:
        f.writelines(col_two)

if __name__ == "__main__":
    main()