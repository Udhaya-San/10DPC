#Today LIST and Components of List are discussed and also the concept of List Slicing is discussed

task = ['eat','code','sleep','repeat']

print(task[0]) #eat
print(task[1]) #code
print(task[2]) #sleep
print(task[3]) #repeat

task.append('exercise') #add new element to the list
print(task)

copy1 = task.copy()
copy2 = task[:]
copy3 = list(task)

copy1.append("A") # [1, 2, 3]        <- untouched
print(copy1)      # [1, 2, 3, 'A']

task.extend(['exercise','repeat']) #add new elements to the list
print(task)

task.insert(6,'exercise') #insert new element at index 6
print(task)
task.count('exercise') #1
print(task.count('exercise')) #1

print("Hi I'm new to Python")