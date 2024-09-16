my_dict = {'Ruslan': 1998, 'Lera': 2000, 'Vary': 2001}
print(my_dict)
my_dict['Ruslan'] = 1998
print(my_dict.get('Ruslan'))
print(my_dict.get('Alla'))
my_dict.update({'Jora': 1997,
                'Vacya': 2003})
del my_dict['Vary']
print(my_dict)
my_set = {True,3,2,3,3,4,5,'Kira'}
print(my_set)
my_set.add('Arbuz')
my_set.add(7)
print(my_set)
my_set.remove(True)
print(my_set)
