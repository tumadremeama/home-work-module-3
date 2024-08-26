def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

# 1 часть
print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(b=25)
print_params(c=[1, 2, 3])

# 2 часть
values_list = [3.14, 'текст', False]
values_dict = {'a': 42, 'b': 'слово', 'c': None}

# распаковка
print_params(*values_list)
print_params(**values_dict)

# 3 часть
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)