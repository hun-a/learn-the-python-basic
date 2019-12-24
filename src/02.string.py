# https://wikidocs.net/13

# Expression for the String
print("Hello Python!")
print('Python is fun!')
print("""It's so interasting...""")
print('''Is it work?''')

print("Python's favorite food is perl")
print('Python\'s favorite food is perl')
print('"Python is very easy." he says.')
print("\"Python is very easy.\" he says.")

print("Life is too short\nYou need Python")
print('''
Life is too short
You need Python
''')
print("""
Life is too short
You need Python
""")

# Operators within String
head = 'Python'
tail = ' is fun!'
print(head + tail)

print(3 * 'python')
print('=' * 50)
print('My program')
print('=' * 50)

a = 'Life is too short'
print('string: ' + a)
print(len(a))
print(a[0])
print(a[-1])
print(a[0:4])
print(a[:4])
print(a[4:])
print(a[:])

date = '20010331Rainy'
year = date[0:4]
day = date[4:8]
weather = date[8:]
print(date)
print(year)
print(day)
print(weather)


# Formatting the String
applesByNumber = 'I eat %d apples'
print(applesByNumber % 3)
number = 3
print(applesByNumber % number)
applesByString = 'I eat %s apples'
print(applesByString % 'five')

print('%s is a string' % 'String')
print('%c is a character' % 'C')
print('%d is a integer' % 0)
print('%f is a floating-point' % 0.1)
print('%o is a octal number' % 2**10)
print('%x is a hexadecimal' % 2**10)
print('Error is %d%%' % 98)
print('%s can receive all format - %s %s %s' % ('%s', 1, 0x1ab3, 0.1))

print('%10s' % 'hi')  # Sort to the right
print('%-10sjane' % 'hi') # Sort to the left
print('%0.4f' % 3.42134234)
print('%10.4f' % 3.42134234)

applesByFunction = 'I eat {0} apples'
print(applesByFunction.format(3))
print(applesByFunction.format('five'))
acceptTwoArgs = applesByFunction + '. so I was sick for {1} days'
print(acceptTwoArgs.format(10, 'three'))
acceptByName = 'I ate {number} apples. so I was sick for {day} days.'
print(acceptByName.format(number = 10, day = 3))
mixed = 'I ate {0} apples. so I was sick for {day} days.'
print(mixed.format(10, day=3))

print('{0:<10}'.format('hi'))
print('{0:>10}'.format('hi'))
print('{0:^10}'.format('hi'))
print('{0:!<10}'.format('hi'))
print('{0:!>10}'.format('hi'))
print('{0:=^10}'.format('hi'))

print('{0:0.4f}'.format(3.4123412))
print('{{ and }}'.format())
name = 'huna'
age = 30

print(f'My name is {name} and age is {age}')
print(f'My age will be {age + 1} next year')
d = {'name':'stranger', 'age':30}
print(f'My name is {d["name"]} and age is {d["age"]}')
print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":!<10}')
print(f'{"hi":!>10}')
print(f'{"hi":=^10}')
y = 3.123123
print(f'{y:0.4f}')
print(f'{y:10.4f}')
print(f'{{ name }}')

# String functions
hobby = 'hobby'
print(hobby.count('b'))
print(hobby.find('o'))
print(hobby.find('k'))
print(hobby.index('h'))
# print(hobby.index('k')) <= error

print(','.join('abcde'))
print(','.join(['a','b','c','d']))

print(hobby.upper())
print(hobby.upper().lower())
print(' hi '.rstrip())
print(' hi '.lstrip())
print(' hi '.strip())
str = 'Life is too short'
print(str.replace('Life', 'Your leg'))
print(str.split())
print('a:b:c:d'.split(':'))