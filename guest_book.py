from pathlib import Path

path = Path('guest_book.txt')


guest_names = '---Guest Names---'

print('Please tell me the names of your party. Type "q" when done:\n')
while True:

    guest = input("")

    if guest == 'q':
        break
    
    guest_names += '\n'
    guest_names += guest
    
path.write_text(guest_names)

print(path.read_text())
    

