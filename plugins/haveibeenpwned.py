# -*- coding: utf-8 -*-

import requests

class haveibeenpwned():
    def check(self,email):
        url = 'https://haveibeenpwned.com/api/v2/breachedaccount/%s' % email
        r = requests.get(url)
        if r.content:
            a = [leak['Title'] for leak in r.json()]
            return a
        else:
            return False
