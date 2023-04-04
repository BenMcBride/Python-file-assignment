num1 = 42 # variable declaration, initialize int
num2 = 2.3 # variable declaration, initialize int
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize array of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize object 
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize strings
print(type(fruit)) # log statement of type checking: fruit
print(pizza_toppings[1]) # log statement of the secont value in the pizza_toppings array
pizza_toppings.append('Mushrooms') # add value: 'Mushrooms to the array pizza_toppings
print(person['name']) # log statement printing the 'name' value within the person object
person['name'] = 'George' # changing the 'name' vlaue in the person object to 'George'
person['eye_color'] = 'blue' # adding the 'eye_color' value to the person object and setting it to = 'blue'
print(fruit[2]) # log statement of the 3rd value of fruit ('banana')

if num1 > 45: # if conditional
    print("It's greater") # log statement
else: # else conditional
    print("It's lower") # log statement

if len(string) < 5: # if conditional
    print("It's a short word!") # log statement
elif len(string) > 15: # else if conditional
    print("It's a long word!") # log statement
else: # else conditional
    print("Just right!") # log statement

for x in range(5): # for loop starting x at 0 and counting up to 4
    print(x) # log statement printing the value of x
for x in range(2,5): # for loop starting x at 2 and counting up to 4
    print(x) # log statement printing the value of x
for x in range(2,10,3): # for loop starting x at 2, counting up to 10, and incrementing by 3
    print(x) # log statement printing the value of x
x = 0 # variable declaration, initialize int
while(x < 5): # while loop that loops until x is >= 5
    print(x) # log statement printing the value of x
    x += 1 # add 1 to value of x

pizza_toppings.pop() # remove last value in array pizza_toppings
pizza_toppings.pop(1) # remove first value in array pizza_toppings

print(person) # log statement of person object
person.pop('eye_color') # remove 'eye_color' value from person object
print(person) # log statement of person object

for topping in pizza_toppings: # for loop that loops through each item in pizza_toppings
    if topping == 'Pepperoni': # if conditional 
        continue # continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if conditional
        break # break

def print_hello_ten_times(): # function defined
    for num in range(10): # for loop that starts at 0, and increments up to 9
        print('Hello') # log statement

print_hello_ten_times() # calls the function

def print_hello_x_times(x): # function defined
    for num in range(x): # for loop that starts at 0, and increments up to x
        print('Hello') # log statement

print_hello_x_times(4) # calls the funtion with x = 10

def print_hello_x_or_ten_times(x = 10): # function defined
    for num in range(x): # for loop that starts at 0, and increments up to x
        print('Hello') # log statement

print_hello_x_or_ten_times() # calls the function with x = 10
print_hello_x_or_ten_times(4) # calls the function with x = 4


"""
Bonus section
"""

# print(num3) - num3 isn't defined
# num3 = 72 - variable declaration as int
# fruit[0] = 'cranberry'  - error fruit isn't an array
# print(person['favorite_team']) - error 'favorite_team' isn't a key value
# print(pizza_toppings[7]) - error pizza_toppings[7] is out of range
#   print(boolean) - error invalid indentation
# fruit.append('raspberry') - error fruit isn't an array, so we can't append it
# fruit.pop(1) - error fruit isn't an array, so we can't pop it