
#variables
name ='Nsooli Winfred' 
age =23

# printing variables
#printing my details
print('My name is :'+name )
print('Im ',age, 'years old')



#Boolean
gender_female= True
print(gender_female)


# Creating a Dictionary
Dict = {1:'Monday', 2:'Tuesday', 3: 'Wednesday'}
print("\nThis a dictionary for the days of the week")
print(Dict)



#using the len() with tuple 
Animals = ("cow", "goat", "cat", "dog", "lion")

length = len(Animals)
print("The length of tuple is: ", length)

# How to access tuples
Animals = ("cow", "goat", "cat", "dog", "lion")

#Accessing first item via index 
print(Animals[0])

#Negative indexing(last item in the tuple)
print(Animals[-1])


#Range of indexes
#Search starts at index 1 and ends at index 5
print(Animals[1:5])


#This returns items from beginning to, but leaves out forth item
print(Animals[:4])

#Range of Negative Indexes
#Returns the items from index -3 (included) to index -1 (excluded)
print(Animals[-3:-1])


#check if item exisits in a tuple
if 'lion' in Animals:
    print("Yes lion is in the animals tuple")





#finding the length, data types, accessing items in a set, Add items, Add two sets together
days_week = {"Monday", "Tuesday", "Wednesday", "Thursday"}


#Finding length
length =len(days_week)
print(length)
  

#Data types
#All print<class, 'set'>
print(type(days_week))


#Acessing items
#Looping through a set
for y in days_week:
    print(y)

#Checking whether item exists
print("Thursday" in days_week)


#Add items in the set
Numbers ={10, 20, 40,30}

Numbers.add(70)
print(Numbers)



#Adding two sets
fruits = {"Banana", "Mango", "Lemeon", "Apple"}
colours = {"Yellow", "Green", "Blue ", "Gray"}

fruits.update(colours)
print(fruits)


# creating aList
fruits = ["Banana", "Mango", "Lemeon", "Apple"]
print(fruits)
#Data type
print(type(fruits))

#List constructor
fruits = list(("Banana", "Mango", "Lemeon", "Apple"))
print(fruits)
