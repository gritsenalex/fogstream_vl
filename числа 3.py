k = int(input('Введите число от 1 до 10:\n'))
n = 540 + k * 45 + (k - 1) // 2 * 20 + (k - 1) % 2 * 5
hour = n // 60 #целочисленное деление
minute = n % 60 
print(f'{hour:02d}:{minute:02d}') #для красоты вывода
