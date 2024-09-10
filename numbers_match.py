from random import choice


def generate_random_list(numbers):
    num_list = []

    while len(num_list) < 5:
        i = choice(numbers)
        if i not in num_list:
            num_list.append(i)
    
    return num_list





numbers_list = range(11)

target_list = generate_random_list(numbers_list)

list_match = False

tries = 0
max_tries = 1_000_000

while not list_match:
    list_match = True
    
    random_list = generate_random_list(numbers_list)

    list_index = range(len(random_list))

    for i in list_index:
        if random_list[i] != target_list[i]:
            tries += 1
            list_match = False

        if tries >= max_tries:
            break



if list_match:
    print(f'{target_list} matches {random_list}')
    print(f'It tooks {tries} tries!')

else:
    print(f'Couldnt find a match in a million tries')