# A dictionary is a collection of unordered key-value pairs.
#It can be created using curly braces {} or the dict() function.

#creation using curly braces
biodata1 = {
    'name':'Edwin',
    'tel': '0756342045',
    'age': 24,
    'studentnumber': 2200706853
    }

#creation using dict() function
fruits = dict({1:'Apple', 2: 'Orange', 3: 'Grapes', 4: 'Banana'})


#accessing dictionary values
#1. using square brackets
print(biodata1['age']) 
print(fruits[2])

# #2. using get() method
print(biodata1.get('name'))
print(fruits.get(1))

#updating dictionary values
#when the key already exists, the value is updated
biodata1['age'] = 27


#when the key does not exist, the key-value pair is added
biodata1['address'] = 'Wandegeya'
biodata1['status'] = 'Single'

#Removing dictionary values
biodata1.pop('studentnumber')
 #remove the value associated with the key and returns the value
print(biodata1)

biodata1.popitem() #removes the last inserted key-value pair and returns the pair
print(biodata1)

biodata1.clear() #removes all the key-value pairs and returns an empty dictionary
print(biodata1)



del biodata1  #deletes the entire dictionary
print(biodata1)

#Dictionary Methods
names = {1:"Elsa", 2:"Anna", 3:"Kristoff"}

#Get all keys
print(names.keys())

#Get all values
print(names.values())

#Get all key-value pairs
print(names.items())

#check if a key exists
exists = 1 in names #returns True or False
print(exists)

#copy a dictionary
copy = names.copy()
print(copy)