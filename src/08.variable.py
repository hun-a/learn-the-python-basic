# https://wikidocs.net/18

from copy import copy

a = 1
b = 'python'
c = [1, 2, 3]

print(a, b, c)
print(a, id(a))
print(b, id(b))
print(c, id(c))

print('b - a: ', int(id(b)) - int(id(a)))

a = [1, 2, 3]
b = a
print(a)
print(b)
print(a is b)
a[1] = 4
print(a)
print(b)
print(id(a))
print(id(b))

b = a[:]
print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))

b = copy(a);
print(a)
print(b)
print(a is b)
print(id(a))
print(id(b))

(a, b) = 'hi', 'hello'
print(a, b)

a, b = ('hi', 'hello')
print(a, b)

[a, b] = ['hi', 'hello']
print(a, b)

a = b = 'world'
print(a, b)

a = 3
b = 5
print(a, b)
a, b = b, a
print(a, b)
