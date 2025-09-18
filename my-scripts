'''fav_drink1 = input(str('long fav drink?'))
fav_drink2 = input(str('short fav drink?'))

fav1 = (len(fav_drink1))
fav2 = (len(fav_drink2))
fav3 = (fav1 - fav2)


print (fav_drink1, "is", fav3, "character(s) shorter than", fav_drink2)'''


'''
fav_drink = str(input())
firstchar = fav_drink[0]
print("The first character of", fav_drink, "is", firstchar)
'''

''' 
user_name = input()
user_address = input()
addresses_str = f"{user_name} can be found at {user_address}"
print (addresses_str)
'''

'''
bob = "bob"
print(bob)
print (type(bob))
print (type(3))
print (type(3.3))
print (type("3"))
print(3)
print("3")
int(bob)
print(bob)
'''
'''
word = 'banana'
for letter in word : 
    print (word[2])

print(word[3])
'''


'''
city = (input("city"), input("city"), int(input("num")))

print(city[0])
print(city[1])
print(city[2])
'''
'''
city_data = (1, 2, 3)

print(city_data[0])
print(city_data[1])
print(city_data[2])
'''
'''
first_name = 1
last_name = 2
state = 3
age = int(4)

person_data = (first_name, last_name, state, age)
print(f"First name: {person_data[0]}, Last name: {person_data[1]}, State: {person_data[2]}, Age: {person_data[3]}")
'''
'''
from collections import namedtuple
Color = namedtuple("Color", ["name", "R" , "G", "B"])

color_name = input()
red_channel = int(input())
green_channel = int(input())
blue_channel = int(input())

color = Color(color_name, red_channel, green_channel, blue_channel)

print(f"Color name: {color.name}, R: {color.R}, G: {color.G}, B: {color.B}")
'''
'''
monsters = {"Gorgon", "Medusa"}
trolls = {"William", "Bert", "Tom"}
horde = {"Gorgon", "Bert", "Tom"}
print (monsters.union(trolls))
print (monsters.difference)'''
'''
unique_numbers = set()
size1 = int(7)
size2 = int(78)
size3 = int(79)
size4 = int(70)

unique_numbers.add(size1)
unique_numbers.add(size2)
unique_numbers.add(size3)
unique_numbers.add(size4)

print(sorted(unique_numbers))'''

'''
colors_remaining = set()

new_color1 = input()
new_color2 = input()
new_color3 = input()
colors_remaining.add(new_color1)
colors_remaining.add(new_color2)
colors_remaining.add(new_color3)

#remove something if 3 or more. 
if len(colors_remaining) > 2:
    colors_remaining.pop()
    
#how many are left. 
num_colors = len(colors_remaining)

print(f"Number of values remaining: {num_colors}")  '''

'''
numbers_set1 = {21}
numbers_set2 = set()
numbers_set2.add(int(input()))
numbers_set2.add(int(input()))

# add set 2 to set 1 then remove 49
numbers_set1.update(numbers_set2)
numbers_set1.remove(49)
#add another input
numbers_set1.add(int(input()))

print(f"numbers_set1: {sorted(numbers_set1)}")
print(f"numbers_set2: {sorted(numbers_set2)}")'''

'''food_name1 = input()
item_count1 = int(input())
food_name2 = input()
item_count2 = int(input())
food_name3 = input()
item_count3 = int(input())

food_quantities = {}

food_quantities[food_name1] = item_count1
food_quantities[food_name2] = item_count2
food_quantities[food_name3] = item_count3

print(f"{food_name1}: {food_quantities[food_name1]}")
print(f"{food_name2}: {food_quantities[food_name2]}")
print(f"{food_name3}: {food_quantities[food_name3]}")'''

'''
food_quantities = {"waffles": 74, "peppers": 38, "oranges": 40}
print("Original:")
print(food_quantities)
#input key
key = input()
#if input is the thing, subtract 2 
if key == "waffles":
    food_quantities["waffles"] -= 2
elif key == "peppers":
    food_quantities["peppers"] -= 2
elif key == "oranges":
    food_quantities["oranges"] -= 2

print("Updated:")
print(food_quantities)'''
'''
length_in_days = int(input())

if length_in_days == 7:
    print("Exactly one week")
else:
    print("Not equal to one week")'''

### Zachary - Frame - assignment2 - RatePay 
### name: Frame, Zachary   
### date: 9/15/2025
### description: create overtime pay calculations using a function for the calculation
###

def computepay(hours, rate):
    if hours > 40:
        reghrs = 40
        othrs = hours - 40
    else:
        othrs = 0
        reghrs = hours
    pay = reghrs * rate + othrs * rate * 1.5
    return(pay)

hrs = input("input hours:")
rt = input("input pay (hourly):")
hours = float(hrs)
rate = float(rt)

###compute the pay 
print("your pay is:", (computepay(hours, rate)))