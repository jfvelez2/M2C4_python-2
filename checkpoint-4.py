from decimal import Decimal
import math
# M2C4 Python Assignment

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
family_list = ['John', 'Eugenia', 'Emmanuel', 'Elena', 'Evan']
print(family_list)

post = ('Python Basics', 'Intro guide to python', 'Some cool python content', 'published')
print (post)

float = 10.82
print(float)

integer = 123
print(integer)

decimal_value = Decimal(3.14159265359)
print(decimal_value)

NK_Olimpija  = {
    'DF': 'Silva',
    'FW': 'Nukić',
    'MF': 'Elšnik',
    'GK': 'Vidovšek'
}

print(NK_Olimpija)

# Exercise 2: Round your float up.
print(round(float))

# Exercise 3: Get the square root of your float.
print(math.sqrt(float))

# Exercise 4: Select the first element from your dictionary.
print(list(NK_Olimpija.values())[0])

# Exercise 5: Select the second element from your tuple.
second_element = post[1]
print(second_element)

first, second, third, fourth = post
print(second)

# Exercise 6: Add an element to the end of your list.
family_list.append('George')

print(family_list)

# Exercise 7: Replace the first element in your list.
family_list[0] = 'Fredy'

print(family_list)

# Exercise 8: Sort your list alphabetically.
alpha_list = sorted(family_list)

print(alpha_list)

# Exercise 9: Use reassignment to add an element to your tuple.
post += ('tags',)

first, second, third, fourth, fifth = post

print(first)
print(second)
print(third)
print(fourth)
print(fifth)