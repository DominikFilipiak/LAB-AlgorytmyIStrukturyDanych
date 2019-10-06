from math import sqrt

print("Równanie kwadratowe: (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b**2 - 4*a*c

if delta > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(delta))/(2*a))     
    x2 = (((-b) - sqrt(delta))/(2*a))
    print("Są dwa pierwiastki: {} i {}".format(x1, x2))
elif delta == 0:
    num_roots = 1
    x = (-b) / 2*a
    print("Jest jeden pierwiastek: {}".format(x))
else:
    num_roots = 0
    print("Nie ma pierwiastków, delta < 0.")
