#!/usr/bin/python3

"""Returns a to-do list of an employee of the given employee ID """

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/todos/{}", params={"userId":sys.argv[1]}).json()
    
    for t in todos:
        if t.get("completed") is True:
            completed = t.get("title")

            print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
            print("/t{}".format(c) for c in completed)