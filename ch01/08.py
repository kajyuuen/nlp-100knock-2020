def cipher(string):
    return "".join([ chr(219 - ord(c)) if c.islower() else c for c in string])

def main():
    print(cipher("エービーシーはabc"))
    print(cipher(cipher("エービーシーはabc")))

if __name__ == "__main__":
    main()