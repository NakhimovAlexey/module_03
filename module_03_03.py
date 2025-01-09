# Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
# Вызов функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params(a = "R2D2")
print_params(b = 25)
print_params(c = [1,2,3])
# Распаковка параметров
values_list = ["Bike", 125, False]
values_dict = {"a": 123, "b": 321, "c": 213}
print_params(*values_list)
print_params(**values_dict)
# Распаковка + отдельные параметры:
values_list_2 = [15, "Sun"]
print_params(42, *values_list_2)