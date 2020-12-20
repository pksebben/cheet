



if __name__ == "__main__":
    k = {}
    l = []
    k['1'] = {1: 'a', 2: 'b', 3: 'c'}
    k['2'] = {1: 'a', 2: 'b', 3: 'c'}
    print(k)
    k['1'] = {"blarg": "none"}
    print(k)
    for i in k:
        print(k[i]) 

# {
#     'context': {
#         'keybind' : {...data},
#         'otherkeybind' : {...data},
#     },
#     "other context" :  {
#         ...keybinds
#     }
# }
