my_dict = {'Nikita' : 1995, 'Anna' : 1996}
print(my_dict.get('Nikita'))
my_dict['Vadim'] = 1997
print(my_dict)
my_dict['Katya'] = 1998
my_dict['Viktor'] = 1999
print(my_dict)
del my_dict['Viktor']
print(my_dict)
print(my_dict.get('Viktor', 'этот ключ и значение я удалил двумя строчками выше, поэтому значение не вывести'))
print(my_dict)

my_set = {1, 2, 3, 4, 'll', 1, 2, 3, 4, 'll'}
print(my_set)
my_set.add(13)
my_set.add(12)
print(my_set)
my_set.discard('ll')
print(my_set)
