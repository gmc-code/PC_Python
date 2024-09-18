import keyword

print(keyword.kwlist)

my_dict = {'y': 'triangle', 'x': 'square', 'z': 'pentagon'}
my_dict_sorted_list = sorted(my_dict)
print(my_dict_sorted_list)

my_llist = [['car', 4, 65], ['dog', 2, 30], ['add', 3, 10], ['bee', 1, 24]]
print(list(reversed(my_llist)))
""" outputs [1, -2, -3, 5, 7]"""

my_list = [1, 5, -3, 7, -2]
print(list(reversed(my_list)))
""" outputs [1, -2, -3, 5, 7]"""

my_string_list = ['sheep', 'dog', 'bear']
print(list(my_string_list))
""" outputs ['dog', 'bear', 'sheep']"""

my_list_of_tuples = [('sheep', 5), ('dog', 3), ('bear', 4)]
print(list(reversed(my_list_of_tuples)))
""" outputs [('bear', 4), ('dog', 3), ('sheep', 5)]"""

my_list_of_tuples = [('sheep', 5), ('dog', 3), ('bear', 4)]
print(list(reversed(my_list_of_tuples)))
""" outputs [('dog', 3), ('bear', 4), ('sheep', 5)]"""
