height = int(input("Enter your height.: "))
bill=0
if height >= 120:
    print("You can ride the rollercoaster!") 
    age=int(input("What is your age?: "))
    if age <12:
        bill=5
        print("Child tickets are $5.") 
    elif age <= 18:
        bill=7 
        print("Youth tickets are $7.")
    elif age >=45 and age <=55:
        print("you get a free  ride.")
    else:
        bill=12
        print("Adult tickets are $12.")

    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if  wants_photo =="Y":
        print("$3 extra for photo.")
        bill+=3
        
    print("your bill is", bill)
else:
    print("Sorry, You have to grow taller before you can ride.") 