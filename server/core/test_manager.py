from manager import CheetManager

m = CheetManager()

m.test_populate()

m.select_all()

print()
print('printing all....')
print('~~~~~~~~~~~~~~~~~~~~')

m.pprint()

print()
print('printing by tag = test_one ....')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

m.select_tag('test_one')
m.pprint()

print()
print('printing by context = emacs ....')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

m.select_context('emacs')
m.pprint()
