cat = 'Haru'
#test for equality and inequality
print(cat == 'Haru')
print(cat != 'Haru')
#test using the lower()
print(cat.lower() == 'haru')
#numerical equality tests
number = 27
print(number > 15)
print(number < 30)
print(number >= 35)
print(number <= 20)
#test using the and keyword and the or keyword
print(number < 39 and number > 15)
print(number > 10 or number >20)

#test whether an item is in a list
print('\nBREAK')
animals = ['cat', 'dog', 'bird']
if 'cat' in animals:
    print('True')
if 'bear' not in animals:
    print('True')