# cs50python

# function print, arguments ( and " with " and ) to open and close arguments
print("hello, world")

# improve program to become interactive
input("What's your name? ")
print("hello, world")

# return value and variables, a single = is an assignment operator
name = input("What's your name? ")
print("Hello, ")
print(name)

# comments, such as this - can use as psuedocode, express thoughts - succinctly, methodically, algorithmically
"""
a block of comment
"""

# ask user for their name
name = input("What's your name? ")

# say hello to user
print("Hello, " + name)

# passing multiple arguments to print, a comma will insert a space
print("Hello,", name)

# cancatenotion joins the thing on the left with the thing on the right

# functions take arguments - docs.python.org/3/library/functions.html
#function, *objects means it can take any number of arguments, sep=' ' seperator makes a single blank space, end='\n' new line, 
#  print(*objects, sep=' ', end='\n', file=sys.stndout, flush=FALSE)
# positional and named parameters
# to add a quote print('hello, "friend"') or print("hello, \"friend\"")
# format string
print(f"hello, {name}")

# remove whitespace from string, where name is a string and name is a function and strip is a method. strip removes spaces, title capitlizes first letter of a string
name = name.strip().title()
name = name = input("What's your name? ").strip().title()

# ask user for name
name = input("What's your name? ").strip().title()
# split user's anme into first and last
first, last = name.split("")
#say hello
print(f"hello, {first}")

# interactive mode 
# integer + - * / %
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

#same outcome
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# same outcome
print(int(input("What's x? ")) + int(input("What's y? ")))

"""
What's x? 1.2
What's y? 3.4
"""
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x+y)

print(z)

'''
what's x? 999
what's y? 1
'''

# f string
print(f"{z}")
# f string with 000,000 as in 1,000
print(f"{z:,}")

# creating functions
'''
name = input("What's your name? ").strip().title()
hello()
print(name)
'''
def hello(to="World!"):
    print("Hello,", to)

hello()
name = input("What's your name? ").strip().title()
hello(name)



# --------------
user_input = input("Type something: ").lower
print(f"{user_input}")

name = input()
print(name.lower())
# ----------------------
name = input()
print(name.replace(" ", "..."))

