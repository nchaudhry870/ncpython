print("This file is used for list practice")
bicycles = ['honda', 'yamaha', 'kawasaki']
print(bicycles)
print(bicycles[0])

#Practice some string methods
#Change first element
bicycles[0] = 'ducati'

message = f"I like {bicycles[0].title()} bikes"
print(message)

bicycles.append('vespa')

print(bicycles)

bicycles.insert(1, 'eagle')

print (bicycles)

#print last element of list
print(bicycles[-1])


bicycles.pop()
print(bicycles.pop())
del bicycles[0]

print(bicycles)

bicycles.remove('eagle')
print(bicycles)

#add some more elements in the list 

bicycles.append('Sohrab')
bicycles.append('China Bike')

print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)

sortedList = sorted(bicycles)
print(sortedList)
print(bicycles)

bicycles.reverse()
print(bicycles)

print(len(bicycles))