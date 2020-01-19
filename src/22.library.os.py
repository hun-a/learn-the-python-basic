# https://wikidocs.net/33

import os

print(os.environ)
print(os.environ['PATH'])
print()
print(os.chdir('/Users/hun/git/'))
print(os.getcwd())
print()
print(os.system('ls -lrt'))

f = os.popen('ls')
print(f.read())