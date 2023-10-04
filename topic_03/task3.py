dict = {'один': 1, 'два': 2, 'три': 3}
print("Original dictionary:", dict)

dict.update({'три': 3, 'чьотири': 4})
print("update():", dict)

del dict['два']
print("del():", dict)

dict.clear()
print("clear():", dict)

dict = {'один': 1, 'два': 2, 'три': 3}
keys = dict.keys()
print("keys():", list(keys))

values = dict.values()
print("values():", list(values))

items = dict.items()
print("items():", list(items))