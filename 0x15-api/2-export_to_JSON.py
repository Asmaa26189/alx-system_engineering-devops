#!/usr/bin/python3
"""REST API """

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = str(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users"
    url += "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    url += url "/todos"
    response = requests.get(url)
    tasks = response.json()

    dic = {employeeId: []}
    for t in tasks:
        dic[employeeId].append({
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": username
        })
    with open('{}.json'.format(str(employeeId)), 'w') as f:
        json.dump(dic, f)
