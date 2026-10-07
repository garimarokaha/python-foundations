# list help to keep the multiple values together in a single variable. It is a collection of items in a particular order. Lists are mutable, meaning you can change their content without changing their identity.
scores =[90, 80 , 92, 88]
print(scores[0])
print(scores[2])
print(scores[-1])


#list mutuable ho that means the values inside the list can be changed ....
scores= [90,95,77,88,99,23,12,11,44,3]
print(scores[4]) #99

#if we have to add a new value in the list then we can use append 
scores.append(100)
print(scores) # [90, 95, 77, 88, 99, 23, 12, 11, 44, 3, 100]

#to remove the value from the list we can use remove function
scores.remove(3)
print(scores) # [90, 95, 77, 88, 99, 23, 12, 11, 44, 100]

#to calcualte the length of the list we can use len function
print(len(scores)) #10 

#we can also slice the list just like we slice the string
print(scores[0:3]) # [90, 95, 77]

print(scores[2:5])# [77, 88,99]

print(scores[3:]) # 3 index bata pacchadi samma ko aauchha

print(scores[-1]) #100
print(scores[:3]) # 0 index bata 3 index samma ko aauchha


#some usefull functions in list
# len() → number of elements
# min() → smallest value
# max() → largest value
# sum() → total

print(len(scores)) #10 is the length of the list
print(max(scores)) # 100 value is max
print(min(scores)) #11 value is min
print(sum(scores)) # 579 sum of all the values in the list

scores.sort() #sort the list in ascending order
print(scores)
scores.sort (reverse=True) #sort the list in descending order
print(scores)

scores.clear () # clear the list
print(scores)

scores = [90, 80 , 92, 88]
average =sum(scores)/len(scores)
print(average)
#average = total / number of values

#TUPLE
# A Tuple is similar to list but it is immutable, meaning you cannot change its content once it is created. Tuples are defined using parentheses ().
scores = [90,80,92] #list
coordinates = (27.7, 85.3)  # tuple
# List -> []
# Tuple -> ()
# Mutable = can be changed after creation.
# Immutable = cannot be changed after creation.
coordinates=(27.7, 85.3)
print(coordinates[0]) #27.7
print(coordinates[1]) #85.3
coordinates[0]=40 # This will raise an error since tuples are immutable
print(coordinates) # (27.7, 85.3)

# LIST                     TUPLE

# [90, 80, 92]             (90, 80, 92)
#      ↓                         ↓
# mutable                   immutable
# can change                cannot change

dimensions = (1920, 1080)
print(dimensions)
print(dimensions[0]) #1920
print(dimensions[1]) #1080
print(len(dimensions)) #2


