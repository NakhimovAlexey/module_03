calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    length = len(string)  # Длина строки
    upper_case = string.upper()  # Строка в верхнем регистре
    lower_case = string.lower()  # Строка в нижнем регистре
    return (length, upper_case, lower_case)  # Возвращаем кортеж
def is_contains(string, list_to_search):
    count_calls() # Увеличиваем счетчик вызовов
# Приводим строку и элементы списка к нижнему регистру для сравнения
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list_to_search) # Возвращаем результат проверки

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)

