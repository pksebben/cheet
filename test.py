import unittest
import models
import cheet
import json
import copy

print("Initializing test suite...")

# fixtures

# don't add to this; some tests rely on it's size
test_cheetsheet = models.CheetSheet(
    [
        models.Cheet(
            "test cheet 0",
            "C-h cheet",
            "cheet.py",
            "this is a test",
            "no notes",
            ['testcase', 'module']),
         models.Cheet(
            "test cheet 1",
            "C-h cheet",
            "cheet.py",
            "this is a test",
            "no notes",
             ['testcase', 'module']),
         models.Cheet(
            "test cheet 2",
            "C-h cheet",
            "cheet.py",
            "this is a test",
            "no notes",
            ['testcase',]) 
        ]
)


class TestModels(unittest.TestCase):

    def test_cheet_repr(self):
        cheet = models.Cheet(
            "test cheet",
            "C-h cheet",
            "cheet.py",
            "this is a test of the cheet repr system",
            "no notes",
            ['testcase', 'module']
        )
        self.assertEqual(
            repr(cheet),
            """
---
name: test cheet
key:  C-h cheet
desc: this is a test of the cheet repr system
note: no notes
tags: testcase, module
---
"""
        )

    def test_cheet_from_json(self):
        json = '{"name": "Apropos", "key": "C-h a {topics} RET", "description": "Display a list of commands whose names match {topics}", "note": "No notes", "tags": null, "context": "emacs"}'
        cheet = models.Cheet.from_json(json)
        self.assertEqual(repr(cheet), """
---
name: Apropos
key:  C-h a {topics} RET
desc: Display a list of commands whose names match {topics}
note: No notes
tags: No tags
---
""")

    def test_cheet_as_dict(self):
        expect = {'context': 'cheet.py',
                  'description': 'this is a test',
                  'key': 'C-h cheet',
                  'name': 'test cheet 0',
                  'note': 'no notes',
                  'tags': ['testcase', 'module']}

        cheet = copy.deepcopy(test_cheetsheet.cheets[0])
        self.assertEqual(cheet.as_dict(), expect)

    def test_cheet_as_json(self):
        cheet = copy.deepcopy(test_cheetsheet.cheets[0])
        self.assertEqual(cheet.as_json(), '{"name": "test cheet 0", "key": "C-h cheet", "context": "cheet.py", "description": "this is a test", "note": "no notes", "tags": ["testcase", "module"]}')
        

    # ==================================================
    # CheetSheet tests
    # ==================================================
    
    def test_cheetsheet_reduce_by_tag(self):
        cs = copy.deepcopy(test_cheetsheet)
        cs.reduce_by_tag('module')
        self.assertEqual(len(cs.cheets), 2)

if __name__ == "__main__":
    unittest.main()
