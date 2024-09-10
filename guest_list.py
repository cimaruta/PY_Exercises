#invite some people to dinner
guests = ['tommy', 'charlie', 'jethro']
message = ", would you like to come to dinner?"
print(guests)
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)
#jethro cant make the dinner so hes being replaced by penny, need to send invite again.
print(f"\n{guests[2]} can not make the dinner.")
guests[2] = 'penny'
print (guests)
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)
#invited three more people to dinner, one in the front, one in the middle and one at the end.
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
#now i can only invite two people, so i need to remove four and give them a sorry message
print('\nI can only invite two people to dinner.')
sorry = ', im sorry I cant invite you to dinner'
popped = guests.pop()
print(f'{popped} {sorry}')
popped = guests.pop()
print(f'{popped} {sorry}')
popped = guests.pop()
print(f'{popped} {sorry}')
popped = guests.pop()
print(f'{popped} {sorry}')
print(guests)
#invite the remaining two people
invite = ', you are still invited to dinner'
print(f'{guests[0]} {invite}')
print(f'{guests[1]} {invite}')
print(guests)
#delete the remaining guests guest list for fun
del guests[0]
del guests[0]
print(guests)