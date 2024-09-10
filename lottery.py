from random import choice

def get_winning_ticket(possibilities):
    winning_ticket = []
    while len(winning_ticket) < 4:
        element = choice(possibilities)
        if element not in winning_ticket:
            winning_ticket.append(element)
    return winning_ticket



def get_ticket(possibilities):
    ticket = []
    while len(ticket) < 4:
        element = choice(possibilities)
        if element not in ticket:
            ticket.append(element)
    return ticket


def check_ticket(winning_ticket, rand_ticket):
    for element in rand_ticket:
        if element not in winning_ticket:
            return False
    return True








possibilities = ["A", "B", "C", "D", "E",]
possibilities.extend(range(1,10))

winning_ticket = get_winning_ticket(possibilities)

plays = 0
max_plays = 1_000_000
won = False

while not won:
    rand_ticket = get_ticket(possibilities)
    won = check_ticket(winning_ticket, rand_ticket)
    plays += 1
    if plays >= max_plays:
        break


if won:
    print('you win')
    print(f'The winnning ticket is: {winning_ticket}')
    print(f'Your ticket is: {rand_ticket}')

    print(f'It took {plays} to get there.')

else:
    print('you lose')