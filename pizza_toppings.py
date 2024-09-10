prompt = "What pizza toppings would you like to add?"
prompt += "\nType, 'quit' when you are finished. \n"
condition = True
while condition:
    message = input(prompt)
    if message == 'quit':
        condition = False
    else:
        print(f'{message.title()} has been added to your pizza!')