import random
choose= int(input("What do you choose? Enter '0' for rock, '1' for paper or '2' for scissors: "))
if choose  ==  0:
    print("Rock")
elif  choose == 1:
    print("Paper")
elif choose == 2:
    print("Scissor")
else:
    print("Choose right option.")

print("Computer choose: ")
choose_com  = random.randint(0, 2)
if choose_com ==  0:
    print("Rock")
elif  choose_com == 1:
    print("Paper")
elif  choose_com == 2:
    print("scissor")

if choose == choose_com:
    print("Draw")
elif choose == 0 and choose_com == 2:
    print("You Win")
elif choose == 1 and choose_com == 0:
    print("You Win")
elif choose == 2 and choose_com == 1:
    print("You Win")
else:
    print("You Lose")

