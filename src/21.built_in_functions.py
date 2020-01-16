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