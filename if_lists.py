#exercise 1
usernames = ['tommy', 'penny', 'jethro', 'admin', 'frank']
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello, {username.title()} would you like to see a status report?')
        else:
            print(f'Hello, {username.title()}. Welcome back!')
else:
    print('We need some users!')
#exercise 2
print('\n\n')

current_users = ['jax', 'haru', 'stitch', 'aaron', 'chad']
new_users = ['Aaron', 'charlie', 'CHAD', 'tommy', 'penny']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Sorry, the username "{new_user}" is unavailable.')
    else:
        print(f'The username "{new_user}" is available.')