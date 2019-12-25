
# https://wikidocs.net/15

# Tuple is the immutable version of the list

print(())
print((1,))
print((1, 2, 3))
t1 = 1, 2, 3
print(t1)
print(('a', 'b', ('ab', 'cd')))

t1 = (1, 2, 'a', 'b')
'''
del t1[0]

Traceback (most recent call last):
  File "src/04.tuple.py", line 14, in <module>
    del t1[0]
TypeError: 'tuple' object doesn't support item deletion

t1[0] = 'c'

Traceback (most recent call last):
  File "src/04.tuple.py", line 23, in <module>
    t1[0] = 'c'
TypeError: 'tuple' object does not support item assignment
'''

print(t1[0])
print(t1[3])
print(t1[1:])
t2 = (3, 4)
print(t1 + t2)
print(t2 * 3)
print(len(t1))
