import json

def load_england_text():
    path = "./jawiki-country.json"
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        json_data = json.loads(line)
        if json_data["title"] == "イギリス":
            return json_data["text"]

def main():
    text = load_england_text()
    print(text)

if __name__ == "__main__":
    main()