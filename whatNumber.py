import random

def cpu_number(minNumber, maxNumber):
    cpuNumber = random.randint(minNumber, maxNumber)
    print("Komputer, wylosował liczbę, 01110000011011110111011101101111011001000111101001100101011011100110100101100001!")
    return cpuNumber

def player_number():
    inputNumber = int(input("Proszę podaj liczbę:\n"))
    return inputNumber

def game_difficulty_level(gameMode):
    if gameMode.lower() == "easy":
        print(gameMode)
        count = 10
        return count
    else:
        count = 5
        return count

def play():
    minNumber = int(input("Proszę podaj wartość minimalną szukanej liczby:\n"))
    maxNumber = int(input("Proszę podaj wartość maksymalną szukajnej liczby:\n"))
    gameMode = input("Wybierz poziom trudności, 'easy' lub 'hard':\n")
    count = game_difficulty_level(gameMode)
    cpuChoise = cpu_number(minNumber, maxNumber)
    playerChoise = player_number()

    while playerChoise != cpuChoise:
        count -= 1
        if count == 0:
            break

        if playerChoise > cpuChoise:
            print(f"Twoj liczba jest za duża, ilość prób {count}.")
            playerChoise = player_number()

        else:
            print(f"Twoja liczba jest za mała, ilość prób {count}.")
            playerChoise = player_number()

    if count > 0:
        print(f"Brawo trafiłeś, komputer wybrał {cpuChoise}.")
    else:
        print("GAME OVER")

play()