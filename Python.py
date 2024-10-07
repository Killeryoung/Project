first_string = input("Введіть перший рядок: ")
second_string = input("Введіть другий рядок: ")
result = ''.join([char for char in first_string if char not in second_string])
print("Символи, які є у першому рядку і яких немає у другому:", result)
