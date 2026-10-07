#SETS
#Set -> A set is an unordered collection of unique elements. Sets are defined using curly braces {} or the set() function. Sets do not allow duplicate values and do not maintain any specific order.
#Set -> {}
#A Set is a collection that stores unique values.
numbers = {1,2,2,3,3,3,4}
print(numbers)
#duplicate values automatically remove hunchha.

labels ={"cat", "dog", "cat" ,"bird", "dog", "cat"}
print(labels)

#If we want the unique categories:
unique_labels =set(labels)
print(unique_labels)

# List  → [ ] → ordered collection, duplicates allowed
# Tuple → ( ) → immutable collection
# Set   → { } → unique values, no duplicates

skills = {"Python", "AI", "Python", "ML", "AI"}
print(skills)
print(len(skills)) #length 3 aayo unique value kei aauchha.

