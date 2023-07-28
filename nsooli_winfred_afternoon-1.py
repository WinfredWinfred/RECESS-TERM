#Exercise 1 (Lists):

#1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("Second item:", names[1])

#2. Write a python program to change the value of the first item to a new value#
names[0] = "Alex"
print("Updated list:", names)

#3. Write a python program to add a sixth item to the lis
names.append("Frank")
print("Updated list:", names)


#4. Write a python program to add “Bathel” as the 3rd item in your list
names.insert(2, "Bathel")
print("Updated list:", names)

#5. Write a python program to remove the 4th item from the list
del names[3]
print("Updated list:", names)

#6. Use negative indexing to print the last item in your list
print("Last item:", names[-1])


#7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
new_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print("Items:", new_list[2:5])

#8. Write a list of countries and make a copy of it.
countries = ["USA", "Canada", "Australia", "Japan", "Germany"]
countries_copy = countries.copy()
print("Copy:", countries_copy)

#9. Write a python program to loop through the list of countries
for country in countries:
    print(country)

#10. Write a list of animal names and sort them in both descending and ascending order.
animals = ["lion", "elephant", "tiger", "giraffe", "zebra"]
ascending_order = sorted(animals)
descending_order = sorted(animals, reverse=True)
print("Ascending order:", ascending_order)
print("Descending order:", descending_order)

#11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them

animals_with_a = [animal for animal in animals if 'a' in animal]
print("Animal names with 'a':", animals_with_a)

#12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["John", "Jane", "Alice"]
second_names = ["Doe", "Smith", "Johnson"]
full_names = [first + " " + second for first, second in zip(first_names, second_names)]
print("Full names:", full_names)



#Exercise2 (Tuples)
#1. Consider the tuple below; #Write a python program to output your favorite phone brand.

x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[0]
print("Favorite phone brand:", favorite_brand)

#2. Use negative indexing to print the 2nd last item in your tuple. 

second_last_item = x[-2]
print("Second last item:", second_last_item)


#3. Using the phones list above, write a python program to update “iphone” to “itel”
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("Updated tuple:", x)

#4. Write a python program to add “Huawei” to your tuple.
x = x + ("Huawei",)
print("Updated tuple:", x)

#5. Write a python program to loop through the tuple above.
for item in x:
    print(item)

#6. Write a python program to remove/delete the first item in your tuple.
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print("Updated tuple:", x)

#7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu"])
print("Cities in Uganda:", cities)

#8. Write a python program to unpack your tuple.
brand1, brand2, brand3, brand4 = x
print("Unpacked brands:", brand1, brand2, brand3, brand4)

#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print("Cities:", cities[1:4])

#10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Jane", "Alice")
last_names = ("Doe", "Smith", "Johnson")
full_names = first_names + last_names
print("Full names:", full_names)

#11. Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print("Multiplied colors:", multiplied_colors)

#12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print("Count of 8:", count_8)


#Exercise3 (Sets)
#1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])
print("Favorite beverages:", beverages)

#2. Use the correct method to add 2 more items to the beverages set.
beverages.add("water")
beverages.update(["soda", "smoothie"])
print("Updated set:", beverages)

#3. Given the set below;mySet = {“oven”, “kettle”, “microwave”, “refrigerator”}  Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

#4. Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print("Updated set:", mySet)

#5. Write a python program to loop through the set above.
for item in mySet:
    print(item)

#6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print("Updated set:", mySet)

#7. Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {25, 30, 35}
first_names = {"John", "Jane", "Alice"}
combined_set = ages.union(first_names)
print("Combined set:", combined_set)


#Exercise4 (Strings)
#1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
num = 42
text = "The answer is: "
concatenated = text + str(num)
print(concatenated)

#2. Consider the example below;txt = “ Hello, Uganda! ”Output the string without spaces at the beginning, in the middle and at the end.
txt = " Hello, Uganda! "
trimmed = txt.strip()
print(trimmed)

#3. Write a python program to convert the value of ‘txt’ to uppercase.
uppercase_txt = txt.upper()
print(uppercase_txt)

#4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
replaced_txt = txt.replace('U', 'V')
print(replaced_txt)

#5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.y = “I am proudly Ugandan”
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)

#6. The piece of code below will give an error when output;x = “All “Data Scientists” are cool!” Write a python program to correct it.
x = "All \"Data Scientists \" are cool!"

x = 'All "Data Scientists" are cool!'
print(x)



#Exercise5 (Dictionaries)
#1. With reference to the dictionary below, write a python program to print the value of the shoe size. Add this dictionary to your .py file

Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}

print(Shoes["size"])

#2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print(Shoes)

#3. Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)

#4. Write a python program to return a list of all the keys in the dictionary above.
keys = list(Shoes.keys())
print(keys)

#5. Write a python program to return a list of all the values in the dictionary above.
values = list(Shoes.values())
print(values)

#6. Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("Key 'size' exists.")
else:
    print("Key 'size' does not exist.")

#7. Write a python program to loop through the dictionary above.
for key, value in Shoes.items():
    print(key, ":", value)

#8. Write a python program to remove “color” from the dictionary.
Shoes.pop("color")
print(Shoes)

#9. Write a python program to empty the dictionary above.
Shoes.clear()
print(Shoes)

#10. Write a dictionary of your choice and make a copy of it.
original_dict = {"a": 1, "b": 2, "c": 3}
copied_dict = original_dict.copy()
print(copied_dict)

#11. Write a python program to show nested dictionaries
nested_dict = {
    "person1": {
        "name": "John",
        "age": 25
    },
    "person2": {
        "name": "Jane",
        "age": 30
    }
}

for person, details in nested_dict.items():
    print("Person:", person)
    for key, value in details.items():
        print(key, ":", value)
    print()


