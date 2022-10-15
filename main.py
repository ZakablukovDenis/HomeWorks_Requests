import requests
import json
from pprint import pprint

"""ЗАДАНИЕ № 1"""

hero = ["Hulk", "Captain America", "Thanos"]


def get_intell():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    resp = requests.get(url)
    # print(resp.content)
    # print(resp.text)
    # pprint(resp.json())
    rez = {}
    for i in resp.json():
        if i['name'] in hero:
            # pprint(f"{i['name']}: Intelligence - {i['powerstats']['intelligence']}")
            rez[i['name']] = i['powerstats']['intelligence']

    max_int = max(rez.values())
    for key, value in rez.items():
        if value == max_int:
            print(f"Name: {key} | Intelligence: {value}")


if __name__ == "__main__":
    get_intell()
