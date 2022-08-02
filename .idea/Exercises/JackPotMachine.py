import random
coins = 100

print("Jackpot Machine made by Ezzerof")

while coins > 0:
    print("")
    print("You have",coins, "points.")
    print("Press 0 to exit, any other button to play.")
    wager = input()
    if coins == 0 or wager == str("0"):
        break
    # Printing random numbers from 0 to 9
    x = random.randint(0,9)
    y = random.randint(0,9)
    z = random.randint(0,9)
    print(x,y,z)

    if x == y and y == z:
        if x==5:
            coins= coins + 2000
            print("You WON 2000 points. BIG JACKPOT")
            continue
        else:
            coins= coins + 20
            print("You WON 20 points.")
    elif x == y or x == z or y == z:
        if x == 5 and x == y:
            print("JACKPOT you won 200 points.")
            coins= coins + 200
        elif x == 5 and x == z:
            print("JACKPOT you won 200 points.")
            coins= coins + 200
        elif y == 5 and y == x:
            print("JACKPOT you won 200 points.")
            coins= coins + 200
        elif y == 5 and y == z:
            print("JACKPOT you won 200 points.")
            coins= coins + 200
        elif z == 5 and z == x:
            print("JACKPOT you won 200 points.")
            coins= coins + 200
        elif z == 5 and z == y:
            print("JACKPOT you won 200 points.")
            coins= coins + 200
        else:
            coins= coins + 10
            print("You WON 10 points.")
    else:
        coins= coins - 10
        print("You lost",". You have", coins, "points.")