favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()} ")

poll = ['jen', 'edward', 'aaron', 'haru',]
print('\nHave you taken our poll?')

for name in poll:
    if name in favorite_languages.keys():
        print(f'\nThank you, {name.title()} for your response')
    else:
        print(f'\n{name.title()} Please take our poll')