#exercise one
alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points')
if alien_color == 'red':
    print('You just earned 5 points')
#exercise two/three
alien_color = 'yellow'
if alien_color == 'green':
    print('\nYou just earned 5 points')
elif alien_color == 'yellow':
    print('\nYou just earned 10 points')
elif alien_color == 'red':
    print('\nYou earned 15 points')
#exercise 4
print('\nWhat stage of life are you at?')
age = 15
if age < 2:
    print('You are a baby')
elif age >= 2 and age < 4:
    print('You are a toddler')
elif age >= 4 and age < 13:
    print('You are a kid')
elif age >= 13 and age < 20:
    print('You are a teenager')
elif age >= 20 and age < 65:
    print('You are an adult')
elif age >= 65:
    print('You are an elder')
#exercise 5
fruits = ['watermelon', 'strawberry', 'banana']
print('\n')
if 'watermelon' in fruits:
    print('I like watermelon!')
if 'strawberry' in fruits:
    print('I like strawberry')
if 'banana' in fruits:
    print('I like banana')
if 'blueberry' not in fruits:
    print('I dont like blueberry')
if 'tomato' not in fruits:
    print('I dont like tomato')