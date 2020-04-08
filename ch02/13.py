import csv

def main():    
    with open("./col1.txt", "r") as f:
        col_ones = f.read().split()

    with open("./col2.txt", "r") as f:
        col_tows = f.read().split()

    with open("./col1-col2.txt", "w") as f:
        f.writelines([one_line + "\t" + two_line + "\n" for one_line, two_line in zip(col_ones, col_tows)])

if __name__ == "__main__":
    main()