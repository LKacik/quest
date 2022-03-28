import requests
import json
from pprint import pprint
from enum import IntEnum


def get_facts(animal, amount):
    params = {
        "amount": amount,
        "animal_type": animal
    }

    r = requests.get("https://cat-fact.herokuapp.com/facts/random", params)

    try:
        animalFacts = r.json()

    except json.decoder.JSONDecodeError:
        print("Nieprawidłowy foramt")
    else:
        if amount == 1:
            pprint(animalFacts["text"])
        elif amount == 0:
            return
        else:
            for animal in animalFacts:
                pprint(animal["text"])
                print('')


def choice_animal_and_amount_facts():
    animalEnum = IntEnum("animalEnum", "cat dog")
    animalChoice = int(input("""Fakty jakiego zwierzaka chcesz zobaczyć:
    1. Kot
    2. Pies
    """))
    amountFacts = int(input("Ile faktów chcesz przeczytać?"))

    if animalChoice == animalEnum.cat:
        get_facts("cat", amountFacts)

    elif animalChoice == animalEnum.dog:
        get_facts("dog", amountFacts)

choice_animal_and_amount_facts()