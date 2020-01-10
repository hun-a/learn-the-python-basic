# https://wikidocs.net/26

# create

f = open('file.txt', 'w')
for i in range(1, 11):
  data = 'line %d\n' % i
  f.write(data)
f.close()

# read

f = open('file.txt', 'r')
line = f.readline()
print(line)
f.close()

f = open('file.txt', 'r')
while True:
  line = f.readline()
  if not line: break
  print(line, end='')
f.close()

f = open('file.txt', 'r')
lines = f.readlines()
for line in lines:
  print(line, end='')
f.close()


f = open('file.txt', 'r')
data = f.read()
print(data, end='')
f.close()

# append
f = open('file.txt', 'a')
for i in range(11, 21):
  data = 'line %d\n' % i
  f.write(data)
f.close()

# open the file with auto close
with open('file.txt', 'r') as f:
  print(f.read(), end='')

with open('file.txt', 'w') as f:
  f.truncate()