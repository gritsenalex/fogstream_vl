n = int(input('Введите число:\n'))
n = n % 1440
hour = n // 60
minute = n % 60
print(f'{hour:02d}:{minute:02d}')
