# https://wikidocs.net/30

try:
  a.a
except:
  print('Error occurred!')

try:
  f = open('no', 'r')
except FileNotFoundError:
  print('Not found')

try:
  4 / 0
except ZeroDivisionError as e:
  print(e)

try:
  a.a
except:
  print('Error!!')
finally:
  print("The 'Finally' statement will run always")

try:
  a = [1, 2]
  print(a[3])
  4 / 0
except ZeroDivisionError:
  print("you can't divide with zero")
except IndexError:
  print('You accessed the invalid index number')


try:
  a = [1, 2]
  print(a[3])
  4 / 0
except (ZeroDivisionError, IndexError) as e:
  print(e)

try:
  f = open('no_file', 'r')
except FileNotFoundError:
  pass

class Bird:
  def fly(self):
    raise NotImplementedError

class Eagle(Bird):
  pass

eagle = Eagle()
try:
  eagle.fly()
except NotImplementedError:
  print('Not implemented')

class Sparrow(Bird):
  def fly(self):
    print('so fast')

sparrow = Sparrow()
sparrow.fly()


class MyError(Exception):
  pass

def say_nick(nick):
  if nick == 'fool':
    raise MyError()
  print(nick)

try:
  say_nick('Angel')
  say_nick('fool')
except:
  print('Not allowed nickname')


try:
  say_nick('Angel')
  say_nick('fool')
except MyError as e:
  print(e)

'''
If you want to print the error message,
you should implement the __str__ method
in the error class as below.

class MyError(Exception):
  def __str__(self):
    return 'Not allowed nickanme'
'''