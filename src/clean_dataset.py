import json

with open("./../../data/raw/raw.txt", "r+") as f:
    data = f.read()
    data = data.replace("][", "]\n[")

    with open("./../../data/raw/raw.json", "w+") as fnew:

        fnew.write(data)
        # json.dump(data, fnew)

        fnew.close()
