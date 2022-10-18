import requests

"""ЗАДАНИЕ № 1"""

hero = ["Hulk", "Captain America", "Thanos"]


def get_intell():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resp = requests.get(url)
    rez = {}
    for i in resp.json():
        if i['name'] in hero:
            rez[i['name']] = i['powerstats']['intelligence']

    max_int = max(rez.values())
    for key, value in rez.items():
        if value == max_int:
            result = f"Name: {key} | Intelligence: {value}"
            print(result)


if __name__ == "__main__":
    get_intell()
