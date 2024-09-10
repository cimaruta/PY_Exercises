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
    return rand_list




numbers = list(range(11))

random_list = get_list(numbers)


print("Here is a random list!")
print(random_list)


sorted_list = sort_list(random_list)

print("Now its sorted, mate.")
print(sorted_list)