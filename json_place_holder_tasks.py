import requests
import json

def count_taks_completed(tasks):
    idAndNumbersCompletedTasks = dict()
    for task in tasks:
        if task['completed'] == True:
            try:
                idAndNumbersCompletedTasks[task['userId']] += 1
            except KeyError:
                idAndNumbersCompletedTasks[task['userId']] = 1
    return idAndNumbersCompletedTasks


def get_users_with_max_completed_tasks(idAndNumbersCompletedTasks):
    usersWithMaxCompletedTasks = []
    maxCompletedTasks = (max(idAndNumbersCompletedTasks.values()))
    for userId, completedTasks in idAndNumbersCompletedTasks.items():
        if completedTasks == maxCompletedTasks:
            usersWithMaxCompletedTasks.append(userId)
    return usersWithMaxCompletedTasks

def checks_users_names(users, list):
    usersNamesList = []
    for user in users:
        if user['id'] in list:
            usersNamesList.append(user['name'])
    return usersNamesList


jsonMessage = requests.get("https://jsonplaceholder.typicode.com/todos")
jsonMessage2 = requests.get('https://jsonplaceholder.typicode.com/users')
try:
    tasks = jsonMessage.json()
    users = jsonMessage2.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    idAndCompletedTasks = count_taks_completed(tasks)
    result = get_users_with_max_completed_tasks(idAndCompletedTasks)
    print(result)
    usersNames = checks_users_names(users, result)
    print(usersNames)





