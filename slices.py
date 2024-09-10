#Exercise 4-10
print('\t\tExercise 4-10')
sodas = ['lime', 'orange', 'grape', 'cherry', 'watermelon' , 'berry']

print('\nThe first three itemes in the list are:')
print(sodas[:3])

print('\nThe three items from the middle of the list are:')
print(sodas[2:5])

print('\nThe las three itesm in the list are:')
print(sodas[-3:])

#exercise 4-11
print('\n\t\tExercise 4-11')

pizzas = ['pepperoni', 'supreme', 'hawaiian', 'meatlovers']
friend_pizzas = pizzas[:]
pizzas.append('margherita')
print('\nI like these pizzas:')
for pizza in pizzas:
	print(f'- {pizza}')

print('\nMy friend likes these pizzas')
friend_pizzas.append('chicago')
for friend_pizza in friend_pizzas:
	print(f'- {friend_pizza}')

#Exercise 4-12
print('\n\t\tExercise 4-12')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('watermelon')
friend_foods.append('chocolate')

print('\nMy favorite foods are:')
for my_food in my_foods:
	print(my_food)

print('\nMy friends favorite foods are')
for friend_food in friend_foods:
	print(friend_food)