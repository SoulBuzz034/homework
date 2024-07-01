immutable_var = 'строка', 2
print(immutable_var)
# изменить элементы кортежа невозможно, поскольку, кортежи неизменяемы
mutable_list = ([1, 2], 3, 4)
print(mutable_list)
mutable_list[0][0] = 34
print(mutable_list)