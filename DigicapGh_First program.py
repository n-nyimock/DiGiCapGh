"""
if 5>2:
    print('Five is greater than three')

X,  Y, Z = 'Orange', 'Banana', 'Pawpaw'
print(X)
print(Y)
print(Z)

import random
print(random.randrange(1, 10))


age = 45
txt = 'My name is Justice , and i am {}'
print(txt.format(age))


quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollars"
print(myOrder.format(quantity, itemNo, price))


a = 200
b = 33
if b>a:
    print('b is greater than a')
else:
    print('b is not greater than a')

print(bool('Hello'))
print(bool(15))



def myFunction():
    return True


if myFunction():
    print('YES')
else:
    print('NO')


Y = 300
print(isinstance(Y, int))

weight_in_KG = input('Input your Weight: ')
weight_in_tone = (int(weight_in_KG) * 0.70)
print(weight_in_tone)
print((type))

F_name = input('What is your first name? ')
F_name = F_name.upper()
L_name = input('what is your last name? ')
Birth_year = input('what is your year of birth? ')
age = (2022 - int(Birth_year))
print(age + 3)
if age + 3 <=30:
    print('You are a young man from Ghana')
else:
    print('You should be in University by now and that is great achievement.')
real = (F_name.upper())
real1 = (L_name.upper())
my_details = "My name is {} {}"
print(my_details.format(real, real1))

y = bin(3)
print(y)

import random
X = range(1, 99)
my_num = input('Place your guess: ')
y = int(my_num)
if y <= 68:
    print('great')
print(X)

import random
num = random.randint(1, 99)
guess = None


while guess != num:
    guess = input('Guess a number between 1 and 99: ')
    guess = int(guess)

    if guess == 70:
        print('Congratulations! You won.')
        break
    elif guess > 70:
        print('Try again, your guess is too high!')
    else:
        print('Try again, your guess is too low!')



def my_function(**kid):
    print('His last name is ' + kid['lname'])


my_function(fname = 'Justice', lname = 'Bitanyanmi')



def my_function(country = "Ghana"):
    print('I am from ' + country)


my_function("Nigeria")
my_function("USA")
my_function('Germany')
my_function()
my_function('Senegal')



def my_function(food):
    for x in food:
        print(x)


fruits = ['Banana', 'Cherry', 'Apple']


my_function(fruits)


def my_function(x):
    return 7 * x


print(my_function(50))
print(my_function(10))
print(my_function(20))
print(my_function(4))
print(my_function(9))
print(my_function(43))
print(my_function(7))


def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


tri_recursion(10)


def greet_user(l_name, f_name):
    print(f'Hi {l_name }, {f_name}!')
    print("Welcome to today's tutorial")


print("Start")
greet_user("Justice", "Bitanyanmi")
print("Finish")


this_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = this_list.copy()
print(my_list)


try:
    age = int(input('Age: '))
    income = 30000
    risk = int(income/age)
    print(age)
    print(risk)
except ZeroDivisionError:
    print('age cannot be zero')
except ValueError:
    print('Invalid Value')
"""
import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())





































