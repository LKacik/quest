import random
from enum import Enum
from time import sleep


def movement():
    game_lenght = 5
    counterNo = 0
    golds = 0
    print("""
    Budzisz się w zimnej, mokrej komnacie - myślisz nawet nie taki brzydki wystrój kamień + drewno.
    Na wprost masz stare zbutwiałe drzwi, wciąż są na tyle twarde, że ich nie wyważysz,
    pewnie dębowe - myślisz. Słyszysz jakieś odgłosy, narastają, brzmią jak 'brrrr brrr - chrapiący smok?'.
    Ups to tylko w Twoim żołądku. Dostrzegasz luźne kamienie w wzdłuż wysokości drzwi. 
    Po Chwili...
    """)
    sleep(0)
    print("    Dłuższej chwili...")
    sleep(0)
    print("""
    Wreszcie udaje Ci się zrobić dziurę, na tyle dużą, że powinna pomieścić nawet Ciebie - w końcu
    całą noc oraz poranek nic nie jadłeś - chyba jest popołudnie, czy już noc?
    Dostrzegasz korytarz, długi, długi na 5 tur, co turę skrzynia, którą oświetla pochodnia. 
    Czas zebrać wszystkie skarby z tych skrzyń i uciec... 
    Czas ruszać w drogę...
    
    """)

    while game_lenght > 0:
        move = input("Idziesz? (odp. 'tak' lub 'nie')\n")
        if move == 'nie':
            counterNo += 1
            if counterNo == 2:
                print("Gdy zostaniesz jeszcze troszkę w tym miejscu, przytrafi się coś złego!")
            elif counterNo == 4:
                print("Przytrafiło się coś złego, dostałeś biegunki!\nGAME OVER")
                return
            else:
                print("Nie masz wyjścia musisz iść!")
        elif move == 'tak':
            event = events()
            if event > 0 :
                print(f"Natrafiłeś na skrzynię, {event} złota.")
                golds += event
            elif event == 0:
                print(f"Natrafiłeś na pustą skrzynie?! Koś był przed tobą?")
            elif event == -1:
                print(f"Natrafiłeś na szczura, gigantycznego, ledwo uszdłeś z życiem!")
            elif event == -2:
                print(f"Natrafiłeś na gluta, wygląda jak galaretka, ale to On Ciebie pożarł.\nGAME OVER")



            game_lenght -= 1

    return end_game(golds)


def events():
    Event = Enum('Event', ['Chest', 'Empty', 'Enemy'])
    eventDictionary = {
        Event.Chest: 0.70,
        Event.Empty: 0.15,
        Event.Enemy: 0.15
    }
    eventList = tuple(eventDictionary.keys())
    eventProbability = tuple(eventDictionary.values())
    drawEvent = random.choices(eventList, eventProbability)[0]
    if drawEvent == Event.Chest:
        Chests = Enum('Chests', ['Brown', 'Silver', 'Gold', 'Platinum'])
        ChestsDictionary = {
            Chests.Brown: 0.72,
            Chests.Silver: 0.19,
            Chests.Gold: 0.06,
            Chests.Platinum: 0.03
        }
        ChestsList = tuple(ChestsDictionary.keys())
        ChestsProbability = tuple(ChestsDictionary.values())
        drawChest = random.choices(ChestsList, ChestsProbability)[0]

        rewardsForChestDictionary = {
            Chests.Brown: random.randint(100, 500),
            Chests.Silver: random.randint(1000, 2000),
            Chests.Gold: random.randint(1000, 2000),
            Chests.Platinum: random.randint(10000, 20000)
        }

        if drawChest == Chests.Brown:
            return rewardsForChestDictionary.get(Chests.Brown)
        elif drawChest == Chests.Silver:
            return rewardsForChestDictionary.get(Chests.Silver)
        elif drawChest == Chests.Gold:
            return rewardsForChestDictionary.get(Chests.Gold)
        elif drawChest == Chests.Platnium:
            return rewardsForChestDictionary.get(Chests.Platinium)


    elif drawEvent == Event.Empty:
        return 0
    elif drawEvent == Event.Enemy:
        Enemy = Enum('Enemy', ['Rats', 'Blob'])
        EnemyDictionary = {
            Enemy.Rats: 0.72,
            Enemy.Blob: 0.19
        }
        EnemyList = tuple(EnemyDictionary.keys())
        EnemyProbability = tuple(EnemyDictionary.values())
        drawEnemy = random.choices(EnemyList, EnemyProbability)[0]
        if drawEnemy == Enemy.Rats:
            return -1
        elif drawEnemy == Enemy.Blob:
            return -2


def end_game(golds):
    print(f"GRATULACJE, dotrwałeś do końca, zdobyłeś {golds} mieszków złota.")


def play():
    movement()

play()


