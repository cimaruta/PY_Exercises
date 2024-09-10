guests = ['tommy', 'charlie', 'jethro']
message = ", would you like to come to dinner?"
print(guests)
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)

print(f"\n{guests[2]} can not make the dinner.")
guests[2] = 'penny'
print (guests)
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)

print('\nI found a bigger table!')
guests.insert(0,'todd')
guests.insert(2,'frank')
guests.append('finn')
print(guests)
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)
print(guests[3].title() + message)
print(guests[4].title() + message)
print(guests[5].title() + message)
print(len(guests))
