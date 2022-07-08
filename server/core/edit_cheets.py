import os
import subprocess
import tempfile
import sys
import yaml

args = sys.argv

class Cheet:
    name = "test cheet"
    key = "k"
    context = "no context"
    description = None
    note = "None"
    tags = None

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


test_cheet = Cheet()

test_cheet.edit()

print('successfully edited cheet')
