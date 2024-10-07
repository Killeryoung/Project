numbers = input("Введіть числа, розділені пробілами: ")
result = ' '.join([f"x={num}" for num in numbers.split()])
print("Результат:", result)
