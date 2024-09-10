#a list of the games im playing right now
games = ['battle brothers', 'helldivers', 'foxhole']
print("These are currently my favourite games")	
print(games)
#rank of my favorite games
print('These are my favorite games ranked from 1 to 3')
print(f'1.{games[0]} 2.{games[2]} 3.{games[1]}')
#this is the main game im playing
print(f'Right now, {games[0].title()} is my favorite game to play.')
#modify the list
games[1] = 'new world'
#add games to list
games.insert(1, 'gta')
games.append('rimworld')
print('Sometimes ill play these games instead')
print(games)
#various delete functions
print(games)
del games[2]
hate = games.pop(1)
print(f'I actually only play {games}, i dont ever play {hate}')
#sort functions
games.sort()
print('Here is the list of games in alphabeitcal order')
print(games)
print('Here is the list in reverse alphabeitcal order')
games.sort(reverse=True)
print(games)
print(f'Here is the list sorted again and then reverse sorted. \n{sorted(games)}')
print(games)
#number of games in the list
length = len(games)
print(f'There are {length} games in this list.')