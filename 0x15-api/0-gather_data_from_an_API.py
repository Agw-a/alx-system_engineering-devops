#!/usr/bin/python3
""""""
import requests
import sys


if __name__=='__main__':
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    response = requests.get(url)
    name = response.json().get("name")
    todosUrl = 'https://jsonplaceholder.typicode.com/todos'
    responseTodo = requests.get(todosUrl)
    taskName = []
    task = 0
    done = 0
    for i in responseTodo.json():
        if i.get("userId") == int(sys.argv[1]):
            task += 1
            if i.get("completed") is True:
                done += 1
                taskName.append(i.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                         done,
                                                         task))
    for n in taskName:
        print("\t {}".format(n))
