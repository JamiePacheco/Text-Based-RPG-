import random
import time
import sys
import os
import combat

def string(x):

    i = 0
    while i < len(x):
        for char in x: 
            print(char, end="") 
            sys.stdout.flush() 
            time.sleep(0.02) 
            i += 1
    else:
        print("")

def CharacterMenu():


    def Player_Stats():
        global PlayerStats
        PlayerStats = {"LEVEL":combat.User.level,"EXP": combat.User.XP,"HEALTH": combat.User.health,"STRENGTH": combat.User.strength, "AGILITY": combat.User.agility, "LEVEL UP POINTS": combat.User.LVP}
        
        string("THESE ARE YOUR CHARACTER STATS:\n")
        
        for x in PlayerStats: string(f"{x}: {PlayerStats[x]}")


    def LevelUpPointsMenu():
        while combat.User.LVP > 0:
            string("WHAT STAT WOULD YOU LIKE TO LEVEL UP?:\n")
            string(f"[1] HEALTH: {PlayerStats['HEALTH']}")
            string(f"[2] STRENGTH: {PlayerStats['STRENGTH']}")
            string(f"[3] AGILITY: {PlayerStats['AGILITY']}")
            string(f"[4] BACK TO OTHER MENU")
            choice = int(input(": "))

            if choice == 1:
                combat.User.health += 20
                combat.User.LVP -= 1

                string(f"YOUR HEALTH IS NOW {combat.User.health}")
                
            if choice == 2:
                combat.User.strength += 1
                combat.User.LVP -= 1

                string(f"YOUR STRENGTH IS NOW {combat.User.strength}")
              
            if choice == 3:
                combat.User.agility += 1
                combat.User.LVP -= 1
                string(f"YOUR AGILITY IS NOW {combat.User.agility}")
            elif choice == 4:
                return 
        else:
            string("YOU HAVE NO POINTS TO SPEND")
        
    def Menu():

        string("\n[1] USE LEVEL POINT")
        string("[2] CHECK EXP NEEDED UNTIL NEXT LEVEL UP")
        string("[3] CHECK POINTS")
        string("[4] BACK")
        choice = input(":")

        if choice == "1":
            os.system("cls")
            LevelUpPointsMenu()
            os.system('cls')
            Player_Stats()
            Menu()
        elif choice == "2":
            string(f"\nEXP NEEDED TO LEVEL UP: {100*combat.User.level - PlayerStats['EXP']}\n")
            Menu()
        elif choice == "3":
            string(f"\n YOUR SCORE IS {combat.Player_Points} POINTS.")
            Menu()
        elif choice == "4":
            os.system("cls")
            return
        else:
            Menu()
    Player_Stats()
    Menu()
