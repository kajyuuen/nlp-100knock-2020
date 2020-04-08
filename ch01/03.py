def main():
    string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print([ len(s.strip(".,")) for s in string.split(" ")])

if __name__ == "__main__":
    main()