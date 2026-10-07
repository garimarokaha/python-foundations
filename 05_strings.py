# string is a sequence of characters used to represent text. 
#Character:            G   a   r   i   m   a
#positive Index:       0   1   2   3   4   5
#Negative Index:      -6  -5  -4  -3  -2  -1

#indexing concepts

name = "garima"
print(name)
print(name[0])# to print whats on the 0th index

print(name[2])# to print whats on the 2nd index

print(name[-1])# to print whats on the last index

name[0] #g
name[1] #a
name[2] #r  
name[3] #i
name[4] #m
name[5] #a 

name[-1] #a
name[-2] #m
name[-3] #i
name[-4]  #r
name[-5] #a
name[-6] #g


#slicing concepts
#slicing gives us a section of a string.
language = "python"
#to print pyt
language[0:3] #pyt
language #python
language[2:] #thon
print(language[:3]) #pyt


word = "machine"
#for chine 
print(word[2:])

name = "garima rokaha"
#length of the string , space lai pani 1 index count garchha
print(len(name))

print(name.upper()) #GARIMA ROKAHA
print(name.lower()) #garima rokaha
print(name.title()) #Garima Rokaha

#F string
name = "garima"
age = 22
print(f"my name is {name} and my age is {age}")
#f le chai kehi value chha {} vitra bhanera vanchha

name = "garima"
age = 22
goal = "AI Engineer"
print(f"my name is {name.upper() }, and my goal is to became an {goal.upper()}, also my age is {age}")
print(f"my name is {name.lower()}, and i am {age}yrs old , my goal is to become an {goal.lower()}")
print(f"my name is {name.title()}, my goal is to become {goal.title()}, my age is  {age}yrs old")

print(len(name)) #to calculate length of the name 
print(f"my name is {name }, my age is {age}, my goal is {goal}".upper()) #to convert the whole string into upper case
