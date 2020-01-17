# https://wikidocs.net/32

# abs
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

# any
print(any([1, 2, 3]))
print(any([1, 2, 3, 0]))
print(any([0]))

# chr (0 ~ 127)
print(chr(65))
print(chr(97))
print(chr(126))

# dir
print(dir([1, 2, 3]))
print(dir({ '1': 'a' }))
print(dir((1, 2, 3)))

# divmod
print(divmod(7, 3))
print(7 // 3)
print(7 % 3)

# enumerate
for i, name in enumerate(['body', 'foo', 'bar']):
  print(i, name)

# eval
print(eval('1 + 2'))
print(eval("'hi' + 'a'"))
print(eval("divmod(4, 3)"))

# filter
def positive(l):
  result = []
  for i in l:
    if i > 0:
      result.append(i)
  return result

arr = [1, -3, 2, 0, -5, 6]
print(positive(arr))

def short_positive(x):
  return x > 0

print(list(filter(short_positive, arr)))
print(list(filter(lambda x: x > 0, arr)))

# hex
print(hex(234))
print(hex(3))

# id
a = 1
print(id(1))
print(id(a))
b = a
print(id(b))
print(id(4))

# input
a = input()
print(a)
b = input('Enter: ')
print(b)

# int
print(int('3'))
print(int(2.3))
print(int('11', 2))
print(int('0o10', 8))
print(int('1A', 16))

# isinstance
class Person: pass
a = Person()
print(isinstance(a, Person))
print(isinstance(3, Person))

# len
print(len('python'))
print(len([1, 2, 3]))
print(len((1, 2)))
print(len({'1': '2', '2': '3', '4': '5'}))

# list
print(list('python'))
print(list((1, 2, 3)))

# map
def two_times(numberList):
  result = []
  for number in numberList:
    result.append(number * 2)
  return result

a = [1, 2, 3, 4]
print(two_times(a))

def twice(x):
  return x * 2

print(list(map(twice, a)))
print(list(map(lambda x: x * 2, a)))

# max
print(max([1, 2, 3, 100, 0]))
print(max('python-z'))

# min
print(min([1, 2, 3, 4, 100, 0, -199]))
print(min('python-z'))

# oct
print(oct(34))
print(oct(12345))

# open
f = open('test.txt', 'rb')
print(f.readlines())
f1 = open('test.txt', 'r')
f2 = open('test.txt')
print(f1.readlines(), f2.readlines(), sep='\n')

# ord
print('a', ord('a'), chr(ord('a')))
print('A', ord('A'), chr(ord('A')))

# pow
print(pow(2, 4))
print(pow(3, 3))

# range
print(list(range(11)))
print(list(range(0, 11)))
print(list(range(0, 11, 3)))

# round
print(round(4.51))
print(round(4.55))
print(round(4.51, 1))
print(round(4.55, 1))
print(round(4.518, 2))
print(round(4.551, 2))

# sorted
a = [3, 1, 2, 5, 100, 6]
b = 'zero'
c = (3, 1, 2, 78, 0)
print(sorted(a))
print(sorted(b))
print(sorted(c))

# str
print(str(3))
print(str('hi'.upper()))

# sum
print(sum([1, 2, 3, 4, 5]))
print(sum(range(0, 6)))

# tuple
print(tuple([1, 2, 3, 4]))
print(tuple('zero'))
print(tuple((1, 2, 3)))
print(tuple({'1': '2'}))

# type
print(type('#'))
print(type(1))
print(type([]))
print(type(open('test.txt')))
print(type(open('test.txt', 'rb')))

# zip
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip('abc', 'def')))
print(zip([1, 2, 3], [4, 5, 6]))