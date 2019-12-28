# https://wikidocs.net/1015

s1 = set([1, 2, 3])
print(s1)
s2 = set('Hello')
print(s2)
s3 = set()
print(s3)

l1 = list(s1)
print(l1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))
print(s1 - s2)
print(s1.difference(s2))

print(s1)
s1.add(7)
print(s1)
s1.update([8, 9, 10])
print(s1)
s1.remove(10)
print(s1)