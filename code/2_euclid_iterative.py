def euclid(a, b):
  r = a % b
  print('{}=q*{}+{}'.format(a, b, r))
  while r != 0:
    a = b
    b = r
    r = a % b
    print('{}=q*{}+{}'.format(a, b, r))
  return b

euclid(1071, 462)
