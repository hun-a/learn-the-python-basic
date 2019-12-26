# https://wikidocs.net/16

# The Dictionary as Associative array or Hash

dic = { 'name': 'pey', 'phone': '0119993323', 'birth': '1118' }
print(dic)

print({ 1: 'hi' })
print({ 'a': [1, 2, 3] })

a = { 1: 'a' }
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)

grade = { 'pey': 10, 'julliet': 99 }
print(grade['pey'])
print(grade['julliet'])
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

a[(1,2)] = 'tuple'
print(a)

'''
a[[1,2,3]] = 'list'
print(a)
Traceback (most recent call last):
  File "src/05.dictionary.py", line 29, in <module>
    a[[1,2,3]] = 'list'
TypeError: unhashable type: 'list'
'''

# The functions of dictionary
print(a.keys())
print(list(a.keys()))

for k in a.keys():
  print(k)

print(a.values())
print(list(a.values()))

for v in a.values():
  print(v)

print(a.items())
print(list(a.items()))

for k, v in a.items():
  print('key: {0}, value: {1}'.format(k, v))

print(a.get('name'))
print(a.get((1, 2)))

'''
print(a['no'])
Traceback (most recent call last):
  File "src/05.dictionary.py", line 60, in <module>
    print(a['no'])
KeyError: 'no'
'''
print(a.get('no'))
print(a.get('no', 'default'))

print('name' in a)
print('no' in a)

a.clear()
print(a)
