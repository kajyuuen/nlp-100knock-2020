import random

def typo(string):
    if len(string) <= 4:
        return string
    return string[0] + "".join(random.sample(string[1:-1], len(string)-2)) + string[-1]
    

def main():
    string = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(" ".join([ typo(s) for s in string.split()]))

if __name__ == "__main__":
    main()