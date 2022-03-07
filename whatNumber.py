import random

def cpu_number(minNumber, maxNumber):
    cpuNumber = random.randint(minNumber, maxNumber)
    print("Komputer, wylosował liczbę, 01110000011011110111011101101111011001000111101001100101011011100110100101100001!")
    return cpuNumber

def player_number():
    inputNumber = int(input("Proszę podaj liczbę:\n"))
    return inputNumber

def play():
    minNumber = int(input("Proszę podaj wartość minimalną szukanej liczby:\n"))
    maxNumber = int(input("Prosze podaj wartość maksymalną szukajnej liczby:\n"))
    cpuChoise = cpu_number(minNumber, maxNumber)
    playerChoise = player_number()
    while playerChoise != cpuChoise:
        if playerChoise > cpuChoise:
            print("Twoj liczba jest za duża.")
            playerChoise = player_number()

        else:
            print("Twoja liczba jest za mała.")
            playerChoise = player_number()

    print(f"Brawo trafiłeś, komputer wybrał {cpuChoise}.")

play()