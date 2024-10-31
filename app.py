n = input("Enter name:\n")
permn = input("Is that correct? (y/n) you won't be able to change it later!:\n")
if permn == "n":
    n = input("Enter name:\n")
print("Hello " + n)
print("This project is aimed to help you with your finances.")
print("This project is extremely basic, so you should not expect too much from it.")
print("A better version is underway, though!")
print("")
print("So, let us begin with some basic info.")
avgs = int(input("What is your average salary per month? There is no currency, feel free to enter only digits.\n"))
permn = input("Is that correct? (y/n) you won't be able to change it later!:\n")
if permn == "n":
    avgs = int(input("What is your average salary per month? There is no currency, feel free to enter only digits.\n"))
print("So, you make " + str(avgs) + " per month.")
print("So, that's " + str(avgs * 12) + " per year.")
print("How much percentage of money do you want to save?")
perc = int(input(""))
print("So, you want to save about " + str(avgs * perc / 100) + " per month.")
print("That leaves about " + str(avgs - (avgs * perc / 100)) + " per month.")
print("So, that's " + str((avgs - (avgs * perc / 100)) * 12) + " per year.")
print()
print()
print("How much do you already have?")
cur = int(input(""))
print("So, you have " + str(cur) + ".")
print("How much have you saved?")
sav = int(input(""))
print("So, you have " + str(sav) + " in savings.")
print("So, you have " + str(cur - sav) + " left.")
print("Now, simply type 'D' if you want to deposit, i.e you gained money.")
print("Type 'W' if you want to withdraw, i.e you lost money.")
print("Type 'C' if you want to check your balance.")
while True:
    inp = input("").lower()
    if inp == "d":
        amount = int(input("How much do you want to deposit?\n"))
        cur += amount
        sav += amount
    elif inp == "w":
        cur -= int(input("How much do you want to withdraw?\n"))
    elif inp == "c":
        print("You have " + str(cur))
        print("You have " + str(sav) + " in savings.")
    
