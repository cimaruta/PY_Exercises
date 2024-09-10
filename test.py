from random import choice

def get_list(numbers):
    rand_list = []

    while len(rand_list) <= 5:
        i = choice(numbers)
        if i not in rand_list:
            rand_list.append(i)
    
    return rand_list



def sort_list(rand_list):
    index = range(len(rand_list) - 1)

    sorting = False

    while not sorting:
        sorting = True

        for i in index:
            if rand_list[i] > rand_list[i+1]:
                rand_list[i], rand_list[i+1] = rand_list[i+1], rand_list[i]
                sorting = False


normal_numbers = list(range(11))


print(get_list(normal_numbers))