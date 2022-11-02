# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:52:04 2022

@author: laura
"""

#1.1

a = 2
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#1.2

amount_feet = input("Please enter the amount of feet to convert to acres ")
intfeet = int(amount_feet)
amount_acres = intfeet / 43560
print(amount_acres)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#1.3

inputcel = input("Degrees Celsius ")
intcel = int(inputcel)
tempfahr = (intcel * (9/5)) + 32
print(tempfahr)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#1.4

kilodrive = input("How many km did you drive? ")
intkilo = int(kilodrive)
gasliter = input("How many litres of gas did it take? ")
intgas = int(gasliter)
kilorat = intkilo / 100
literrat = intgas / kilorat
print("Your car used", literrat, "liters per 100 km")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#1.5

print("The following ingredients make 48 cookies")
print("But we understand if you want to make less")
amount_cookies = input("How many cookies would you like to make? ")
int(amount_cookies)
sugar48 = 200
butter48 = 100
flour48 = 275

sugarrat = sugar48 / 48
butterrat = butter48 / 48
flourrat = flour48 / 48

sugarnew = sugarrat * float(amount_cookies)
butternew = butterrat * float(amount_cookies)
flournew = flourrat * float(amount_cookies)

print("Thank you for your input")
print("For", amount_cookies, "cookies you need the following: ")
print("- ", sugarnew, "grams of sugar instead of 200 grams")
print("- ", butternew, "grams of butter instead of 100 grams")
print("- ", flournew, "grams of flour instead of 275grams")
print("Bon appetit!")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#1.6

masterstudents = input("How many master students are registered in this class? ")
phdstudents = input("And how many phd student are there? ")

totalclass = float(masterstudents) + float(phdstudents)
percmas = float(masterstudents) / float(totalclass)
percphd = float(phdstudents) / float(totalclass)
percmas100 = percmas * 100
percphd100 = percphd * 100
print("Percentage master students: ", percmas100,"%")
print("Percentage PhD students: ", percphd100,"%")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#1.7

name_of_bacterium = input('Name a species of bacteria: ')
name_of_population = input('What is the name of the population: ')
doubling_time = input('What is its doubling time (d) in minutes? ')
initial_individuals = input('How many initial individuals (N0) were there? ')
observation_time = input('What was the observation time (t) in minutes? ')

double_exp = float(observation_time) / float(doubling_time)
pop_growth = 2**double_exp
final_pop = pop_growth * float(initial_individuals)
final_pop = int(final_pop)

print(f'The number of individuals in {name_of_bacterium} population {name_of_population} is {final_pop}')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#2.1

user_name = input("User name: ")
password = input("Password: ") #pass -> password

#The first line asks the user to enter their username
#The input of the variable is assigned to user_name
#The second line means to ask the user for password input
#However the variable that is used to assign value to has another syntax meaning
#Therefore the code will not work correctly
#If pass is changed to password for instance the code would be functional

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#2.2

print("Hello World") 
#prints Hello World
print = "Printer on floor 1"
#assigns string to variable 'print'
print("Oh my!") 
#prints Oh My!

#'print =' -> 'print(...)' to make the code work

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#2.3

write("Hello World") #means to print 'Hello World'

#write is not a predefined function in Python

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#2.4

write = print write("Hello World")
#attempts again to use write as a functin but with print function mixed in
#remove the second write to assign a print function to variable 'write'

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#3.2

input_user = input("Please type a single character: ")
compval = "y"
print(compval == input_user)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#4

#When it comes to numbers with many digits the float() function is imprecise
#As mentioned in the lecture it makes many rounding errors and therefore can give wrong output
 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#5

age_child = input("What is the age of the child? ")
height_child = input("what is the height of the child in cm? ")
adult = input("Does a guardian accompany the child yes/no? ")

if adult == "yes":
    print("age lower")
    if int(age_child) >= 8 and int(height_child) >= 130:
        print("Child can go on the Roller Coaster")
    else:
        print("Child cannot go on the Roller Coaster")
else:
    if int(age_child) >= 10 and int(height_child) >= 130: 
        print("Child can go on the Roller Coaster")
    else:
        print("Child cannot go on the Roller Coaster")
        