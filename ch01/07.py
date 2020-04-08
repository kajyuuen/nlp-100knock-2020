def template(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

def main():
    print(template(12, "気温", 22.4))

if __name__ == "__main__":
    main()