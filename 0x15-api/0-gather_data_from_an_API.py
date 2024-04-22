#!/usr/bin/python3
"""REST API """

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    url += "/" + str(employeeId)

    response = requests.get(url)
    employeeName = response.json().get('name')

    url += "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    doneTasks = []

    for t in tasks:
        if t.get('completed'):
            doneTasks.append(t)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for t in doneTasks:
        print("\t {}".format(t.get('title')))
