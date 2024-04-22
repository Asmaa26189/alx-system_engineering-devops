#!/usr/bin/python3
"""REST API """

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    url += "/" + str(employeeId)

    response = requests.get(url)
    username = response.json().get('username')

    url += "/todos"
    response = requests.get(url)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as f:
        for t in tasks:
            f.write('"{}","{}","{}","{}"\n'
                    .format(employeeId, username, t.get('completed'),
                               t.get('title')))
