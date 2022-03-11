
encyclopedia = {"Dupa": "Część ciała."}

def menu():
    print("1. Dodaj definicję.")
    print("2. Wyświetl definicję.")
    print("3. Usuń definicj.")
    print("4. Zakończ.")
    choiceMenu = input("Prosze dokonać wyboru:")
    choice(choiceMenu)

def choice(choiceMenu):
    if choiceMenu == '1':
        keyAdd = input("Proszę podać słowo klucz do zdefinowania:\n")
        valueAdd = input("Proszę podać definicję:\n")
        encyclopedia[keyAdd] = valueAdd
        print("Definicja dodana pomyślnie")
        menu()
    elif choiceMenu == '2':
        keySearch = input("Proszę podaj słowo klucz którego definicji szukasz:\n")
        if keySearch in encyclopedia:
            print(encyclopedia[keySearch])
        else:
            print("Słowo nie jest jeszcze zdefiniowane!\n")
        menu()
    elif choiceMenu == '3':
        keyDel = input("Proszę podaj słowo klucz, które wraz z definicją zostanie usunięte:\n")
        if keyDel in encyclopedia:
            temporaryValue = encyclopedia.pop(keyDel)
            print('Defunicja usunięta prawidłowo')
        else:
            print("Słowo nie jest jeszcze zdefiniowane, nie można usunąć")
        menu()
    elif choiceMenu == '4':
        print("Program wyłączony")

def play():
    menu()

play()