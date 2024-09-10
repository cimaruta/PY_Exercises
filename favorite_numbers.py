favorite_numbers = {
    'aaron': [27, 5, 18,],
    'tam': [50, 23, 11,],
    'mari': [9, 27,],
    'haru': [59, 37, 57,],
    'stitch': [23, 94, 3, 12,],
    }
for names, numbers in favorite_numbers.items():
    print(f"{names.title()}'s favorite numbers are:")
    for number in numbers:
        print(number)