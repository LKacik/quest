import random
from copy import deepcopy


# def lotto(amount, total_amount):
#     numbers = []
#     while len(numbers) < amount:
#         result = random.randint(0, total_amount)
#         if result not in numbers:
#             numbers.append(result)
#     return numbers
#
# print(lotto(6, 49))

def new_lotto(amount, total_amount):
    numbers = []
    listNumbers = [number for number in range(1, total_amount + 1)]
    newListNumber = deepcopy(listNumbers)
    while len(numbers) < amount:
        result = random.choice(newListNumber)
        numbers.append(result)
        newListNumber.remove(result)
    return numbers

print(new_lotto(6, 49))




