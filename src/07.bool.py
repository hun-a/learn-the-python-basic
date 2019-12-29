# https://wikidocs.net/17

a = True
b = False
print(a, b)
print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(2 < 1)
print(type(1 == 1))

def checkBool(a):
  print(f'{a} is {bool(a)}')

checkBool('python')
checkBool('')
checkBool([1, 2, 3])
checkBool([])
checkBool(())
checkBool({})
checkBool(1)
checkBool(2)
checkBool(0)
checkBool(None)

a = [1, 2, 3, 4]
print(f'a is {a}')
while a:
  print(a.pop())
print(f'a is {a}')
