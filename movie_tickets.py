prompt = "Type your age to get movie ticket prices.\n"
prompt += "Type 'quit' to exit\n"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        break
    message = int(message)
    if message < 3:
        print('\nYour ticket is free.')
    elif message < 13:
        print('\nYour ticket is $10')
    else:
        print('\nYour ticket is $15')