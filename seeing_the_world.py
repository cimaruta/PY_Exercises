places = ['japan', 'germany', 'alaska', 'sweden', 'mongolia']
print(places)
#sort the list temporarily
print(sorted(places))
print(places)
#sort the list in reverse temporarily
print(sorted(places, reverse=True))
print(places)
#reverse the list permanently
places.reverse()
print(places)
#reverse the list back to its original state
places.reverse()
print(places)
#permanently sort the list in alphabetical order
places.sort()
print(places)
#permanently sort the list in reverse alphabetical order
places.sort(reverse=True)
print(places)