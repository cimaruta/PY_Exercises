foods = ('spaghetti', 'omolete', 'sandwhich', 'fried rice',	'pizza')
print('Here is our menu\n')
for food in foods:
	print(f'-{food.title()}\n')
print('\nOur menu has changed, here is the new menu:\n')
foods = ('chicken parm', 'pizza', 'bread sticks', 'ravioli')
for food in foods:
	print(f'-{food.title()}\n')
