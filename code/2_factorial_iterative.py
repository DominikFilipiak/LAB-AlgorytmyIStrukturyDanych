def fct(n):
  k = n
  result = k
  while k > 1:
    k = k - 1
    result = result * k
  return result

fct(11)

### Wprowadźmy pętle FOR
for k in range (1, 5):
  print(k)

###
def fct2(n):
  result = n
  for k in range(1, n):
    result = result * k
  return result

fct2(5)
