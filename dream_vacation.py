name_prompt = "What is your name?\n"
visit_prompt = "If you could visit one place in the world, where would you go?\n"
terminate_prompt = "Would you like to let someone else answer? (yes/no).\n"
poll = {}
active = True
while active:
    name = input(name_prompt)
    visit = input(visit_prompt)
    end = input(terminate_prompt)
    poll[name] = visit
    if end == 'no':
        active = False

print('\n---Polling has ended, here are the results.---')
for name, visit in poll.items():
    print(f'{name.title()}: {visit.title()}')