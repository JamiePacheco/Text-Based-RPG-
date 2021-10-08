import time
import sys
import random
import os
import Inventory
#code to allow the text to appear one letter at a time
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

#defines the class enemy and player which allows for the creation of different enemies

class Enemy:
    def __init__(self, Name, HP, STR, AG):
        self.name = Name
        self.health = HP
        self.agility = AG
        self.strength = STR

class Player:
    def __init__(self, HP, STR, AG, LV, XP, LVP):
        self.health = HP
        self.agility = AG
        self.strength = STR
        self.level = LV
        self.XP = XP
        self.LVP = LVP

def Enemy_Generation():
   
    enemy_name = ["GOBLIN","TROLL","DEMON", "GHOUL", "AFFLICTED", "BEAST","CRACK HEAD","INCEL"]

    EnemyHealth = 50
    EnemyStrength = 10
    EnemyAgility = 1
    y = Enemy(random.choice(enemy_name),EnemyHealth ,EnemyStrength, EnemyAgility)

    return y

def Player_Generation():
    global WeaponAttackBonus, MaxHealth

    for x in Inventory.inventory:
        if Inventory.inventory[x]['Equipped'] == True:
            WeaponAttackBonus = Inventory.inventory[x]['Stats'][1]
        else:
            continue

    PlayerHealth = 100
    MaxHealth = PlayerHealth 
    PlayerStrength = 10
    PlayerAgility = 5
    PlayerLevel = 1
    PlayerXP = 0
    PlayerLevelPoints = 1

    
    P1 = Player(PlayerHealth, PlayerStrength, PlayerAgility, PlayerLevel, PlayerXP, PlayerLevelPoints)

    return P1

Player_Points = 0
User = Player_Generation()

def ExperienceGain():
    LevelXP = 100*User.level 
    min = 50*User.level
    max = 75*User.level

    XP = random.randint(min,max)

    if Player_Generation().XP == LevelXP:
        User.level += 1
        string(f"\n YOU HAVE LEVELED UP TO LEVEL {User.level}")


def battle(y):

    global Player_Points

    turn = True
    surrender1 = False

    string(f"\nA {y.name} HAS APPEARED!")

    Initial_Enemy_health = y.health

    #this is the function for the player's turn

    def player_turn():

        nonlocal turn, surrender1
        turn = True
        surrender1 = False

        def surrender():
            chance = random.randint(1, 100)

            if chance <= 70:
                line=y.name, " HAS SPARED YOU."
                string(line)

                nonlocal surrender1, turn
                surrender1 = True
                turn = False


            elif chance > 70:
                line=y.name, " IS NOT SO BENEVOLENT..."

                string(line)
                User.health = User.health - random.randint(5,10)
                
                turn = False

        def attack():
            
            for x in Inventory.inventory:
                if Inventory.inventory[x]['Equipped'] == True:
                    WeaponAttackBonus = Inventory.inventory[x]['Stats'][1]
                else:
                    continue
            dodge_chance = 0 + y.agility * 0.5

            dodge_RNG = random.randint(0,100)

            if dodge_RNG <= dodge_chance:
                line = "\n"+y.name + " HAS DODGED YOUR ATTACK."
                string(line)
            elif dodge_RNG > dodge_chance:

                for x in Inventory.inventory:
                    if Inventory.inventory[x]['Equipped'] == True:
                        CriticalStrikeChance = round(Inventory.inventory[x]['Stats'][0])
                    else:
                        continue
                
                Chance = random.randint(1,100)
                if Chance <= CriticalStrikeChance:
                    damage = 2*(WeaponAttackBonus + User.strength)
                    y.health = y.health - damage
                    string(f"\nYOU HAVE HIT A CRITICAL STRIKE FOR {damage} DAMAGE ON {y.name}")
                elif Chance > CriticalStrikeChance:
                    damage = WeaponAttackBonus + User.strength
                    y.health = y.health - damage
                    string(f"\nYOU HAVE ATTACKED {y.name} FOR {damage} DAMAGE")
               
                string(f"\n{y.name} NOW HAS {y.health} HEALTH")


            nonlocal turn
            turn = False

        def heal():

            if User.health < 100:

                heal = random.randint(5, 10)

                NewHealth = User.health + heal

                if NewHealth > 100:
                    while NewHealth > 100:
                        NewHealth = NewHealth - 1
                    else:
                        User.health = NewHealth
                elif NewHealth <= 100:
                    User.health = NewHealth
                    
                line = "YOU HAVE HEALED FOR ", heal, " POINTS"
                line2 = "YOU HAVE ", User.health, " HEALTH"

                string(line)
                string(line2)

                nonlocal turn
                turn = False

            elif User.health == 100:
                string("YOU ARE AT MAX HEALTH.")
                player_turn()


        def Enemy_Stats():
            
            line = "\n",y.name, "'S STATS ARE:"
            line2 = "HEALTH: ", y.health
            line3 = "STRENGTH: ", y.strength
            line4 = "AGILITY: ", y.agility

            string(line)
            string(line2)
            string(line3)
            string(line4)

        def Player_Stats():

            line = "\nYOUR STATS ARE:"
            line2 = "HEALTH: ", User.health
            line3 = "STRENGTH: ", User.strength
            line4 = "AGILITY: ", User.agility

            string(line)
            string(f"LEVEL: {User.level}")
            string(line2)
            string(line3)
            string(line4)
          


        while turn == True:
            string("\nWHAT WOULD YOU LIKE TO DO?")
            string("[1] ATTACK")
            string("[2] HEAL")
            string("[3] LOOK AT YOUR STATS")
            string("[4] LOOK AT INVENTORY")
            string("[5] LOOK AT ENEMY STATS")
            string("[6] SURRENDER")

            choice = input("ACTION: ")

            os.system("cls")

            if choice == '1':
                attack()
                time.sleep(2)
                os.system("cls")
            elif choice == '2':
                heal()
                time.sleep(2)
                os.system("cls")
            elif choice == '3':
                Player_Stats()
            elif choice == '4':
                Inventory.menu()
                player_turn()
            elif choice == '5': 
                Enemy_Stats()
            elif choice == '6':
                surrender()
            else:
                player_turn()

    #this is the function for the enemy's turn

    def enemy_turn():

        line = "IT IS " + y.name + "'S TURN."
        string(line)

        nonlocal turn
        turn = False

        def Enemy_attack():

            dodge_chance =+ User.agility * 0.5

            dodge_RNG = random.randint(0,100)

            if dodge_RNG <= dodge_chance:
                line1 = y.name + " GOES FOR AN ATTACK\n"
                line2 = "YOU HAVE DODGED THE ATTACK"

                string(line1)
                string(line2)
            elif dodge_RNG > dodge_chance:
                damage = 10 + y.strength

                AttackDescription = [f"\n{y.name} HAS SLASHED YOU FOR {damage} DAMAGE", f"\n{y.name} HAS INFLICTED {damage} DAMAGE", f"\n{y.name} HAS ATTACKED FOR {damage} DAMAGE"]

                User.health = User.health - damage
                string(random.choice(AttackDescription))
                time.sleep(1.5)
                os.system("cls")

            nonlocal turn
            turn = True

        def Enemy_heal():

            if y.health < Initial_Enemy_health:

                heal = random.randint(5,10)

                NewHealth = y.health + heal

                if NewHealth > 100:
                    while NewHealth > 100:
                        NewHealth = NewHealth - 1
                    else:
                        y.health = NewHealth
                elif NewHealth <= 100:
                    y.health = NewHealth

                line = "\n" + y.name + " HAS HEALED FOR ", heal, " HEALTH POINTS"

                string(line)

                nonlocal turn
                turn = True
            else:
                Enemy_attack()

        chance = random.randint(1,100)

        if chance <= 20:
            Enemy_heal()
        elif chance > 20:
            Enemy_attack()

    def ExperienceGain():
        LevelXP = 100*User.level 
        min = 50
        max = 75

        XP = random.randint(min,max)
        
        string(f"YOU HAVE GAINED {XP} XP")
        
        User.XP += XP

        if User.XP >= LevelXP:
            User.level += 1
            User.LVP += 1 
            return string(f"\n YOU HAVE LEVELED UP TO LEVEL {User.level} AND GAINED ONE LEVEL UP POINT\n")
        else:
            return


    while User.health > 0 and y.health > 0 and surrender1 == False:
        if turn == True:
            player_turn()
        elif turn == False:
            enemy_turn()
    else:
        if User.health <= 0 and y.health > 0:

            string("\nYOU HAVE DIED\n")
            sys.exit(string(f"YOUR FINAL SCORE WAS: {Player_Points}"))

        elif y.health <= 0 and User.health > 0:

            string(f"\n{y.name} HAS DIED")
            User.health = MaxHealth
            ExperienceGain()
            Player_Points += 1
            Inventory.LootDropEvent(y.name)
            time.sleep(2)
            os.system("cls")

        elif surrender1 == True and y.health > 0 and User.health > 0:
            User.health = MaxHealth
            string("YOU HAVE SUCCESSFULLY ESCAPED")