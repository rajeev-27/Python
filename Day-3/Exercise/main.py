print("Welcome to Python Pizza Deliveries!") 
size = input("What size pizza do you want? S, M, or L: ") 
 
if size=="S":
    bill=15
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    if add_pepperoni=="Y":
        bill+=2
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese=="Y":
        bill+=1
elif size=="M":
    bill=20
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    if add_pepperoni=="Y":
        bill+=3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese=="Y":
        bill+=1
elif size=="L":
    bill=25
    add_pepperoni = input("Do you want pepperoni? Y or N: ")
    if add_pepperoni=="Y":
        bill+=3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese=="Y":
        bill+=1
else:
    print("please choice right symbol")

print("your bill is" ,bill)
    