def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d
x1, y1, x2, y2 =  [float(i) for i in input('Введите четыре действительных числа:\n').split()]
print(distance(x1, y1, x2, y2))
