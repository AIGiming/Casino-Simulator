import random as r
import os
import time as t
import math as m

onetoft = [52]

money = 1000.0
fortune = 1.0
shopval = [0, 0]

savename = ""

for i in range(1, 54):
    onetoft.append(str(i))

def save(savename):
    f = open(savename, "w")
    f.write(str(money))
    f.write("\n")   
    f.write(str(fortune))
    f.write("\n")
    f.write(str(shopval[0]))
    f.write("\n")
    f.write(str(shopval[1]))

def readsave(savename):
    global money
    global fortune
    global shopval
    f = open(savename, "r")
    money = float(f.readline())
    fortune = float(f.readline())
    shopval[0] = int(f.readline())
    shopval[1] = int(f.readline())

def clearscreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def roule(choice, betting, fort):
    global money
    wheelchose = r.randint(0, 52)    
    if choice == "odd":
        if wheelchose % 2 != 0:
            money += r.random(100, betting) * fort
    elif choice == "even":
        if wheelchose % 2 == 0:
            money += r.random(100, betting) * fort
    elif choice in onetoft:
        if int(choice) == wheelchose:
            money += r.random(100, betting) * fort
        else:
            money -= betting
    money -= betting

def slots(bet, fort):
    bet = int(bet)
    slotmachine = ["7", "cherry", "apple", "wheat", "mace", "obsidian", "cherry", "apple", "apple", "wheat", "wheat", "wheat", "mace", "mace", "mace", "mace", "obsidian", "obsidian", "obsidian", "obsidian", "obsidian"]
    rand1 = r.choice(slotmachine)
    rand2 = r.choice(slotmachine)
    rand3 = r.choice(slotmachine)
    clearscreen()
    loopnum = r.randint(1, 100)
    for i in range(0, loopnum):
        print(f"{r.choice(slotmachine)} {r.choice(slotmachine)} {r.choice(slotmachine)}")
        t.sleep(0.1)
        clearscreen()
    print(f"{rand1} {rand2} {rand3}")
    t.sleep(0.5)
    clearscreen()
    print(f"{rand1} {rand2} {rand3}")
    if rand1 == rand2 and rand2 == rand3:
        if rand1 == "7":
            print("Jackpot! You won 777x your bet!")
            return bet * 777 * fort
        elif rand1 == "cherry":
            print("You won 666x your bet!")
            return bet * 666 * fort
        elif rand1 == "apple":
            print("You won 555x your bet!")
            return bet * 555 * fort
        elif rand1 == "wheat":
            print("You won 444x your bet!")
            return bet * 444 * fort
        elif rand1 == "mace":
            print("You won 333x your bet!")
            return bet * 333 * fort
        elif rand1 == "obsidian":
            print("You won 222x your bet!")
            return bet * 222 * fort
        else:
            print("You won 111x your bet!")
            return bet * 111 * fort
    elif rand1 == rand2:
        if rand1 == "7":
            print("You won 77x your bet!")
            return bet * 77 * fort
        elif rand1 == "cherry":
            print("You won 66x your bet!")
            return bet * 66 * fort
        elif rand1 == "apple":
            print("You won 55x your bet!")
            return bet * 55 * fort
        elif rand1 == "wheat":
            print("You won 44x your bet!")
            return bet * 44 * fort
        elif rand1 == "mace":
            print("You won 33x your bet!")
            return bet * 33* fort
        elif rand1 == "obsidian":
            print("You won 22x your bet!")
            return bet * 22 * fort
        else:
            print("You won 11x your bet!")
            return bet * 11 * fort
    elif rand2 == rand3 or rand1 == rand3:
        if rand3 == "7":
            print("You won 7x your bet!")
            return bet * 7 * fort
        elif rand3 == "cherry":
            print("You won 6x your bet!")
            return bet * 6 * fort
        elif rand3 == "apple":
            print("You won 5x your bet!")
            return bet * 5 * fort
        elif rand3 == "wheat":
            print("You won 4x your bet!")
            return bet * 4 * fort
        elif rand3 == "mace":
            print("You won 3x your bet!")
            return bet * 3 * fort
        elif rand3 == "obsidian":
            print("You won 2x your bet!")
            return bet * 2 * fort
        else:
            print("You won 1x your bet!")
            return bet * fort
    else:
        print("You lost your bet!")
        return -(bet * r.randint(1, 10))

def pinko(betting):
    global money
    betting = float(betting)
    landson = 50
    for i in range(0, 100):
        if r.randint(0, 1) == 1:
            landson += 1
        else:
            landson -= 1
    if landson <= 60 and landson >= 40:
        money -= betting * abs(landson - 50)
        print(f"You lost {betting * (abs(landson - 50) + 1)} dollars!")
    else:
        money += betting * abs(landson - 50)
        print(f"You won {betting * (abs(landson - 50) * 5)} dollars!")

def wheel(betting):
    global money
    global fortune
    money -= betting
    wheelpick = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 8, 9]
    wheelchoice = r.choice(wheelpick)
    if wheelchoice == 1:
        money -= 2.0 * betting
        print("You lost 2 times your betting amount!")
    elif wheelchoice == 2:
        fortune -= 0.1
        print("You lost 10 percent of fortune!")
    elif wheelchoice == 3:
        fortune += 0.1
        print("You gained 10 percent of fortune!")
    elif wheelchoice == 4:
        money += 11.0 * betting * fortune
        print("You got 10 times your money!")
    elif wheelchoice == 5:
        fortune += 0.2
        print("You have 20 percent more fortune now!")
    elif wheelchoice == 6:
        money += 21.0 * betting * fortune
        print("You now got 20 times your bet!")
    elif wheelchoice == 7:
        fortune += 0.5
        print("You got 50 percent more fortune!")
    elif wheelchoice == 8:
        money += 101.0 * betting * fortune
        print("You now have 100 times more money that you betted!")
    elif wheelchoice == 9:
        fortune *= 100.0
        money += 1001.0 * betting * fortune
        print("You not have 100 percent more fortune, 1000 times your bet money, and a re-roll.\n     Re-rolling...")
        wheel(betting)


sleeptime = True

while True:
    print("What would you like to do?\n")
    print("    There are 4 games: Roulette, Wheel and Slots. To play roulette, enter \"roulette\", to play Wheel enter \"wheel\", and to play the slot machines use \"slots\". To play Plinko, use \"plinko\".\n")
    print("    Use \"shop\" to buy upgrades for your fortune and money.\n")
    print(f"    You have a total of {money:.1f} dollars, and you will get {fortune:.1f}x times money than what you usually get.")
    
    terminal = input()
    terminal = terminal.lower()
    if terminal == "help":
        print("There are 4 games: Roulette, Wheel and Slots. To play roulette, enter \"roulette\", to play Wheel enter \"wheel\", and to play the slot machines use \"slots\". To play Plinko, use \"plinko\".\n")
        sleeptime = False

    elif terminal == "save":
        print("Do you have a save file? (Y / N)")
        dec = input()
        if dec == "Y":
            print("What is the name of your save? (Include the extention of the file.)")
            savename = input()
            print("Are you reading or writing to the save? (R / W)")
            devname = input()
            if devname == "R":
                readsave(str(savename))
            else:
                save(str(savename))
        else:
            print("If you don't have a save, would you like to create one? (Y / N)")
            devin = input()
            if devin == "Y":
                print("What is the name of the file you want to save to? (Add extentions)")
                namesav = input()
                save(str(namesav))

    elif terminal == "roulette":
        print("Please enter your bet. (It can be anywhere from 1-52, or \"odd\" or \"even\")")
        bet = input()
        bet = bet.lower()
        roulettestate = True

        if bet == "odd" or bet == "even" or str(bet) in onetoft:
            print("Please enter the amount of money you would like to bet on.")
            betmon = input()
            if betmon.lower() == "all":
                betmon = money
            try:
                betmon = float(betmon)
            except ValueError:
                print("Please enter a valid number.")
            else:
                betmon = float(betmon)
                if betmon <= money and betmon > 0:
                    if roule(bet, betmon, fortune) == True:
                        print("You won! You took everyone else's money.")
                        money += betmon * fortune
                        money += r.randint(100, m.floor(money)) * fortune
                    else:
                        print("You lost! You lost all your money. :(")
                        money -= betmon

                else:
                    print("Woah there. Don't try to cheat the system!")

        else:
            print("Please choose a valid value for the roulette!")

    elif terminal == "slots":
        print("How much would you like to bet?")
        betmon = input()
        if betmon.lower() == "all":
            betmon = money
        try:
            betmon = float(betmon)
        except:
            print("Please enter a valid number.")
        else:
            if betmon > 0 and betmon <= money:
                money -= int(betmon)
                money += slots(betmon, fortune)
            else:
                print("Woah there. Don't try to cheat the system!")

    elif terminal == "wheel":
        print("How much money do you want to bet on the wheel?")
        betmon = input()
        if betmon.lower() == "all":
            betmon = money
        try:
            betmon = float(betmon)
        except:
            print("Please enter a valid number.")
        else:
            if betmon <= money and betmon > 0.0:
                wheel(betmon)
            else:
                print("Woah there. Don't try to cheat the system!")

    elif terminal == "shop":
        print(f"SHOP:\n   1. Get 1.5x fortune for {150**int(shopval[0])+1} dollar(s)!\n   2. Get 3x fortune for {10000**int(shopval[1])+1}")
        cmd = input()
        if cmd == "buy":
            buynum = int(input())
            if buynum == 1:
                if money >= 150**shopval[0] + 1:
                    print("Bought")
                    money -= 150**shopval[0] + 1
                    fortune *= 1.5
                    shopval[0] += 1
                else:
                    print("You don't have enough money!")
            elif buynum == 2:
                if money >= 10000**shopval[1] + 1:
                    print("Bought")
                    fortune *= 3
                    money -= 10000**shopval[1] + 1
                    shopval[1] += 1

    elif terminal == "plinko":
        print("How much money do you want to bet on the pinko?")
        betmon = input()
        if betmon.lower() == "all":
            betmon = money
        try:
            betmon = float(betmon)
        except:
            print("Please enter a valid number!")
        else:
            if betmon <= money and betmon > 0.0:
                pinko(betmon)
            else:
                print("Woah there. Don't try to cheat the system!")
                
    else:
        print("To get help, enter \"help\"")

    if money <= 0:
        print("You have no money left! You are homeless.\n    Play again?")
        if input().lower() == "yes":
            money = 1000.0
            fortune = 1.0
            shopval = [0, 0]
            clearscreen()
        else:
            break

    if sleeptime == True:
        t.sleep(1)
        clearscreen()
    else:
        sleeptime = True
