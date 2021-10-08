import time
import random
import sys
import os
import combat
import Inventory
import Character
def RoomCode():

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

    RoomEntry = {
        "TORTURE ROOM": "YOU ENTER A TORTURE ROOM AND A CHILL RUNS DOWN YOUR SPINE.\n",
        "COMMON ROOM": "YOU ENTER A COMMON ROOM OF SORTS.\n",
        "BARRACKS": "YOU ENTER A ROOM THAT MUST'VE BEEN A BARRACKS.\n",
        "ARMORY" :"YOU ENTER AN ARMORY THAT MUST'VE SUPPLIED AN OLD ARMY.\n",
        "CAVE":"YOU ENTER A SPACE THAT LACKS ANY LIGHT.\n",
        "RUNDOWN ROOM": "YOU A ENTER A RUNDOWN ROOM FILLED WITH ROTTING CORPSES.\n",
        "WHITE ROOM": "YOU ENTER THE ROOM AND FEEL AT PEACE, BUT ON EDGE...\n"
        }


    def RoomsGeneration():     

        EnemySpawn = False
                
        Exits = ["left", "right", "forward"]

        Rooms = ["TORTURE ROOM", "COMMON ROOM", "BARRACKS", "ARMORY", "CAVE", "RUNDOWN ROOM"]

        RoomDescription = {
            "TORTURE ROOM": "YOU LOOK INSIDE OF THE ROOM AND SEE MANGLED BODIES AND GROTESQUE TORUTRE DEVICES.\n",
            "COMMON ROOM": "THE ROOM IS MAINLY EMPTY BESIDES A FEW TABLES AND CHAIRS SCATTERED AROUND.\n",
            "BARRACKS": "THERE ARE BEDS AND TABLES SCATTERED AROUND. LOOKS LIKE THE RESIDENTS LEFT IN A HURRY...\n",
            "ARMORY" :"THIS ROOM HAS OLD WEAPONS AND TOOLS IN IT, THEY ARE OF NO USE NOW.\n",
            "CAVE":"YOU LOOK AT THE WALLS AND REALIZE YOU'RE IN A CAVE.\n",
            "RUNDOWN ROOM": "YOU BREATH IN AND ARE MET WITH A FOUL SMELL YOU LOOK AROUND AND ATTEMPT TO VISUALIZE THE SLAUGHTER THAT HAPPENED HERE.\n",
            "WHITE ROOM": "YOU LOOK AROUND AND SEE WHITENESS AND NOTHINGNESS.\n"
            }

        EXITS = random.randint(1,3)

        doors = []

        i = 0
        while i < EXITS:
            doors.insert(i,random.choice(Exits))
            Exits.remove(doors[i])
            i+=1
        
        ROOM = random.choice(Rooms)

        EnemySpawnChance = random.randint(1,100)

        if EnemySpawnChance <= 80:
            EnemySpawn= True
        elif EnemySpawnChance > 80:
            EnemySpawn= False


        def inspect():

            os.system("cls")

            nonlocal EnemySpawn
            string(RoomDescription[ROOM])
            
            for x in doors:
                if x == "left":
                    string("THERE IS A DOOR TO YOUR LEFT.\n")
                elif x == "right":
                    string("THERE IS A DOOR TO YOUR RIGHT.\n")
                elif x == "forward":
                    string("THERE IS A DOOR STRAIGHT AHEAD.\n")

            if EnemySpawn == True:
                time.sleep(3)
                os.system("cls")
                combat.battle(combat.Enemy_Generation())
                EnemySpawn = False
                choice()
            elif EnemySpawn == False:
                time.sleep(3)
                os.system("cls")
                choice()

        def move():
            os.system("cls")
            string("YOU DECIDE TO LEAVE THE ROOM.\n\nWHAT DOOR DO YOU WANT TO GO THROUGH?\n")
            i = 0
            while i < EXITS:
                for x in doors:
                    if x == "left":
                        string(f"[{i+1}] LEFT")
                        i+=1
                    elif x == "right":
                        string(f"[{i+1}] RIGHT")
                        i+=1
                    elif x == "forward":
                        string(f"[{i+1}] STRAIGHT")
                        i+=1
            else:
                DoorChoice = input(":")
                if DoorChoice == "1":
                    os.system("cls")
                    RoomsGeneration()
                elif DoorChoice == "2":
                    os.system("cls")
                    RoomsGeneration()
                elif DoorChoice == "3":
                    os.system("cls")
                    RoomsGeneration()
                    
                else:
                    move()

        def choice():
            string(RoomEntry[ROOM])

            string("[1] INSPECT ROOM")
            string("[2] MOVE")
            string("[3] INVENTORY")
            string("[4] PLAYER STATS")

            CHOICE = input(":")

            if CHOICE == "1":
                inspect()
                choice()
            elif CHOICE == "2":
                move()
            elif CHOICE == "3":
                Inventory.menu()
                choice()
            elif CHOICE == "4":
                os.system("cls")  
                Character.CharacterMenu()
                choice()
            else:
                choice()

        choice()

    RoomsGeneration()
