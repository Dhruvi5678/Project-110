import random
response = "y"
while response =="y":
    no = random.randint(1,6)
    if no == 1:
        print(" 0 ")
    if no == 2:
        print(" 00 ")
    if no == 3:
        print(" 000 ")
    if no == 4:
        print(" 00 ")
        print(" 00 ")
    if no == 5:
        print(" 00 ")
        print(" 0 ")
        print(" 00 ")
    if no == 6:
        print(" 000 ")
        print(" 000 ")
    response = input("Press y to roll the dice and n to exit")
    print("\n")