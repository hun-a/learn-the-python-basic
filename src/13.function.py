# https://wikidocs.net/24

def add(a, b):
  return a + b

print(add(1, 2))

def say():
  return 'Hi'

print(say())

def add_no_return(a, b):
  print('%d + %d = %d' % (a, b, a + b))

a = add_no_return(1, 2)
print(a)

b = add(b = 1, a = 3)
print(b)

def add_many(*args):
  result = 0
  for i in args:
    result += i
  return result

print(add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calculate(operator, *args):
  if operator == 'add':
    result = 0
    for i in args:
      result += i
    return result
  elif operator == 'mul':
    result = 1
    for i in args:
      result *= i
    return result

print(calculate('add', 1, 2, 3, 4, 5))
print(calculate('mul', 1, 2, 3, 4, 5))
  
def print_kwargs(**kwarg):
  print(kwarg)

print_kwargs(a = 1, b = 2)
print_kwargs(a = 1, b = [1, 2, 3, 4])
print_kwargs(a = { 'hi': 'hello' }, b = [1, 2, 3, 4])
print_kwargs(a = { 'hi': 'hello' }, b = (1, 2, 3, 4))

def add_and_mul(a, b):
  return a + b, a * b

print(add_and_mul(1, 2))

def say_myself(name, old, man = True):
  print("나의 이름은 %s 입니다." % name)
  print("나이는 %d살입니다." % old)
  if man:
    print("남자입니다.")
  else:
    print("여자입니다.")

say_myself('huna', 20)
say_myself('ca', 20, 0)

a = 1
def vartest(a):
  a = a + 1
  return a

print(vartest(1))
print(a)

a = vartest(1)
print(a)

def new_vartest(b):
  global a
  a = a + b
  return a

print(new_vartest(1))
print(a)

add = lambda a, b: a + b
print(add(1, 2))

def run_callback(a, b, fn):
  return fn(a, b)

print(run_callback(10, 20, lambda a, b: a + b))