# https://wikidocs.net/14

# List
odd = [1, 3, 5, 7, 9]
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]
print(a, b, c, d, e)

# Indexing and slicing
print(b[0], b[1], b[2])
print(b[0] + b[1] + b[2])
print(b[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

a = [1, 2, 3, 4, 5]
print(a[0:2])

a = '12345'
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

# Calculate the list
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)
print(len(a))

# Mutate the list
a = [1, 2, 3]
a[2] = 4
print(a)
del a[1]
print(a)
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

# List functions
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5, 6])
print(a)

a = [1, 4, 3, 2]
a.sort()
print(a)
a = ['a', 'c', 'b']
a.sort()
print(a)
a.reverse()
print(a)

print(a.index('a'))
print(a.index('b'))

a = [1, 2, 3]
a.insert(3, 5)
print(a)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

print(a.pop())
print(a)
print(a.pop(0))
print(a)

a = [1, 2, 3, 1]
print(a.count(1))

a.extend([4, 5])
print(a)
print(a + [4, 5])