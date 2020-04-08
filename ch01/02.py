def main():
    string_one = "パトカー"
    string_two = "タクシー"
    print("".join([ i+j for i, j in zip(string_one, string_two)]))

if __name__ == "__main__":
    main()