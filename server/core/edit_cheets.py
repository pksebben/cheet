import os
import subprocess
import tempfile
import sys
import requests
from cheet import Cheet

"""
This is an interface for the API provided by the server.
"""


args = sys.argv
APP_URL = 'http://localhost:8765'

class CheetEditor:
    def edit(self, cheet = None):
        """edit this cheet using a vim subprocess"""
        # TODO: accept cheet and return it as json?
        # TODO: cheet validation
        cheet_template ="""Edit your cheet here. Ensure you do not mangle the format.
name: %s
key: %s
context: %s
description: %s
note: %s
tags: [%s]""" % (self.name or '',
            self.key or '',
            self.context or '',
            self.description or '',
            self.note or '',
            self.tags or '')

        with tempfile.NamedTemporaryFile(suffix='temp') as temp:
            with open(temp.name, "w") as t:
                t.write(cheet_template)
            subprocess.call(['/usr/bin/vim', temp.name])
            text = open(temp.name, 'r').read()
            print('')
            print(text)


def prompt_input(options, prompt=None):
    if prompt:
        print(prompt)
    cmd = input("\n" + str(options) + ":")
    if any(opt in cmd for opt in options):
        return cmd
    else:
        print("sorry, I didn't understand that")
        return prompt_input(options, prompt)

def search_cheets(searchfor = None):
    if searchfor is not None:
        cheets = requests.get(APP_URL + '/get').json()
        cheetlist = []

        contexts = set([x['context'] for x in cheets])
        tags = set([tag for tags in [cheet['tags'] for cheet
                                 in cheets] for tag in tags])
        cheets = Cheet.schema.load(cheets, many=True)

        if searchfor in tags:
            for cheet in cheets:
                if searchfor in cheet.tags:
                    cheetlist.append(cheet)
        if searchfor in contexts:
            for cheet in cheets:
                if cheet.context == searchfor:
                    cheetlist.append(cheet)
    else:
        cheetlist = Cheet.schema.loads(requests.get(APP_URL + '/get').text,
                                            many=True)
    return cheetlist

def list_cheets():
    return Cheet.schema.loads(requests.get(APP_URL + '/get').text, many=True)

def ls(cmd):
    if len(cmd[2:]) > 0:
        print(f"listing cheets that mention \"{cmd[3:]}\"")
        cheetlist = search_cheets(cmd[3:])
    else:
        cheetlist = search_cheets()
    for i in cheetlist:
        print(f"{i.name} [{i.context}] <{i.key}> {i.id}")


if __name__ == "__main__":
    print("Welcome to the cheet cli.")
    cmd = '?'
    list_cheets()
    while cmd != 'q':
        cmd = prompt_input(['ls', 'q', 'vi', 'rm'])
        tlc = cmd[:2]

        # if cmd[:2] == 'ls':
        #     """list cheets, treating context and tag like directories"""

        # elif cmd[:2] == 'vi':
        #     """edit cheets, or create new ones"""
        #     pass
        # elif cmd[:2] == 'rm':
        #     """remove cheets"""
        #     pass



# test_cheet = Cheet()

# test_cheet.edit()

# print('successfully edited cheet')
