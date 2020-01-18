# https://wikidocs.net/33

import sys

print(sys.argv)

if 'bye' in sys.argv:
  print('Good bye')
  sys.exit()

print(sys.path)