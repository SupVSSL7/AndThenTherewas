# reinforcing foundations along with newly acquired security skills and awareness
# to produce new solutions from previous methods.

'''
num1 = input('Enter a number: ')
num2 = input('Enter a second number: ')
answ = int(num1) + int(num2)
print(f'{num1} + {num2} = {int(num1) + int(num2)}')
print(answ)

#####

me = "Kelley"

if me:
    print(me + " is Here!!")
    print(me * 10)


#####
first = input("whats your first name? ")
last  = input("whats your last name? ")
print(first +  last, " it's nice to meet you!")

email = input("Enter your email:  ")
city  = input("Enter your city:  ")
phone = input("Enter phone: ")

print(first +  last, city)
print(email, phone)
# finalprint = input(bool("Does this look correct?: "))
#if finalprint == yes:
#    print("Great!")
#else:
#   print("just start over again, please..")'''

x = input("Enter a number: ")
if int(x) == 41:
    print(x + f"does match my choice--41")
else:
    y = input("pick another number: ")

    if int(y) == 42:
        print(f'My number does in FACT equal 42')
    else:
        print(f"Your answer does NOT equal 42")

name = input("what is your name: ")
if name.lower() == "holly":
    print("Hey " + name.upper() + " BABY!!")
elif name.lower() == "kelley":
    print("AY " + name.upper() + " THATS MY DAWG!")
if name.lower() == "holly" or name == "kelley":
    print("THERES THAT HOT COUPLE!!")
else:
    print("WHO ARE YOU again BRO?")
    print("You're not Holly or Kelley")









