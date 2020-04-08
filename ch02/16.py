import argparse
import math

def main(n):    
    with open("./popular-names.txt", "r") as f:
        line = f.readlines()
    
    line_num = math.ceil(len(line)/n)

    for i in range(n):
        with open("./split-popular-names-{}.txt".format(i+1), "w") as f:
            f.writelines(line[i*line_num:(i+1)*line_num])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()

    main(args.n)