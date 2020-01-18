# https://wikidocs.net/33

import pickle

f = open('object.bin', 'wb')
data = { 1: 'python', 2: 'you need' }
pickle.dump(data, f)
f.close()

f = open('object.bin', 'rb')
b_data = pickle.load(f)
print(b_data)
