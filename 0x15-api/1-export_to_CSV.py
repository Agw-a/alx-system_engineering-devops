#!/usr/bin/python3
"""Python script that using REST api return info on an employee"""
import csv
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    response = requests.get(url)
    if response.status_code == 200:
        username = response.json().get("username")
        todoUrl = 'https://jsonplaceholder.typicode.com/todos'
        resPonse = requests.get(todoUrl)
        fileName = sys.argv[1] + '.csv'
        with open(fileName, 'w') as i:
            wi = csv.writer(i, quoting=csv.QUOTE_ALL, delimiter=',')
            for n in resPonse.json():
                if n.get("userId") == int(sys.argv[1]):
                    outP = [n.get("userId"),
                            username,
                            str(n.get("completed")),
                            n.get('title')]
                    wi.writerow(outP)
