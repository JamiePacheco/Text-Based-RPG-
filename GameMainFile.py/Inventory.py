import random
import time
import sys
import os

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

class weapons:
	def __init__(self, Name,AttackPoints ,Durability, CriticalChance, Description):
		self.NM = Name
		self.AP = AttackPoints
		self.DP = Durability
		self.CC = CriticalChance
		self.Des = Description
	
#Weapon types defined with weapons class

WoodSword = weapons("WOOD SWORD", 10, 50, 100,"A FLIMSY WOODEN SWORD.")
WoodSpear = weapons("WOOD SPEAR", 15, 40, 1,"A FRAGILE WOODEN SPEAR")
WoodAxe = weapons("WOOD MACE", 20, 25, 0, "A WEAK WOODEN AXE")

IronSword = weapons("IRON SWORD", 15, 50, 2.5,"A TYPICAL IRON SWORD.")
IronSpear = weapons("IRON SPEAR", 25, 40, 1,"A SIMPLE IRON SPEAR.")
IronAxe = weapons("IRON AXE", 30, 25, 0, "A BASIC IRON AXE.")

SteelSword = weapons("STEEL SWORD", 25, 50, 2.5,"A STURDY STEEL SWORD")
SteelSpear = weapons("STEEL SPEAR", 30, 40, 1,"A WELL-CRAFTED STEEL SPEAR.")
SteelAxe = weapons("STEEL AXE", 35, 25, 0, "A POWERFUL STEEL AXE.")

EbonySword = weapons("EBONY SWORD", 35, 50, 2.5,"A BEAUTIFULLY CRAFTER SWORD MADE OF EBONY.")
EbonySpear = weapons("EBONY SPEAR", 40, 40, 1,"A SHARP, FEIRCE EBONY SPEAR.")
EbonyAxe = weapons("EBONY AXE",45 , 25, 0, "A BREATH TAKING EBONY AXE.")


IronWeaponDrops = [IronSword, IronSpear, IronAxe]
SteelWeaponDrops = [SteelSword, SteelSpear, SteelAxe]
EbonyWeaponDrops = [EbonySword, EbonySpear, EbonyAxe]

#Player's equiped items

PlayerEquipment = ["WOOD SWORD"]

#Inventory dictionary
inventory = {

	WoodSword.NM: {"ItemName": WoodSword.NM, "Stats": (WoodSword.DP, WoodSword.AP, WoodSword.CC), "Description": WoodSword.Des, "Equipped": True},
	WoodSpear.NM: {"ItemName": WoodSpear.NM, "Stats": (WoodSpear.DP, WoodSpear.AP, WoodSpear.CC), "Description": WoodSpear.Des, "Equipped": False},
	WoodAxe.NM: {"ItemName": WoodAxe.NM, "Stats": (WoodAxe.DP, WoodAxe.AP, WoodAxe.CC), "Description": WoodAxe.Des, "Equipped": False}
}

#print(f"Weapon: {inventory[Sword]['Weapon']}\n{inventory[Sword]['Stats'][1]} Damage\n{inventory[Sword]['Stats'][0]} Durability\n{inventory[Sword]['Stats'][2]} Critical Chance\nDescription: {inventory[Sword]['Description']}")

#code for loot drop event

def LootDropEvent(x):
	WeaponDropChance = random.randint(1,100)

	if WeaponDropChance < 40:
		pass
	elif WeaponDropChance >= 40 and WeaponDropChance < 75:
		drop = random.choice(IronWeaponDrops)

		string(f"\n{x} HAS DROPPED A {drop.NM}")
		string(f"\nWOULD YOU LIKE TO PICK IT UP?\n[1] YES\n[2] NO")
		DropChoice = input(":")

		if DropChoice == "1":
			inventory.update({drop.NM: {"ItemName": drop.NM, "Stats": (drop.DP, drop.AP, drop.CC), "Description": drop.Des, "Equipped": False}})

			string(f"\n{drop.NM} HAS BEEN ADDED TO YOUR INVENTORY")
		elif DropChoice == "2":
			string(f"\n{drop.NM} HAS BEEN LEFT ON THE GROUND")
			pass

	elif WeaponDropChance >= 75 and WeaponDropChance < 95:

		drop = random.choice(SteelWeaponDrops)

		string(f"\n{x} HAS DROPPED A {drop.NM}")
		string(f"\nWOULD YOU LIKE TO PICK IT UP?\n[1] YES\n[2] NO")
		DropChoice = input(":")

		if DropChoice == "1":
			inventory.update({drop.NM: {"ItemName": drop.NM, "Stats": (drop.DP, drop.AP, drop.CC), "Description": drop.Des, "Equipped": False}})

			string(f"\n{drop.NM} HAS BEEN ADDED TO YOUR INVENTORY")
		elif DropChoice == "2":
			string(f"\n{drop.NM} HAS BEEN LEFT ON THE GROUND")
			pass

	elif WeaponDropChance >= 95:
		drop = random.choice(EbonyWeaponDrops)

		string(f"\n{x} HAS DROPPED A {drop.NM}")
		string(f"\nWOULD YOU LIKE TO PICK IT UP?\n[1] YES\n[2] NO")
		DropChoice = input(":")

		if DropChoice == "1":
			inventory.update({drop.NM: {"ItemName": drop.NM, "Stats": (drop.DP, drop.AP, drop.CC), "Description": drop.Des, "Equipped": False}})

			string(f"\n{drop.NM} HAS BEEN ADDED TO YOUR INVENTORY")
		elif DropChoice == "2":
			string(f"\n{drop.NM} HAS BEEN LEFT ON THE GROUND")
			pass

def Weaponinspect(x):

	def WeaponStatsDisplay():
		WeaponDisplay = [
			f"\nWEAPON: {inventory[x]['ItemName']}\n",
			f"\nSTATS:\n",
			f"DAMAGE: {inventory[x]['Stats'][1]}\n",
			f"DURABILITY: {inventory[x]['Stats'][0]}\n",
			f"CRITICAL CHANCE: {inventory[x]['Stats'][2]}\n",
			f"DESCRIPTION: {inventory[x]['Description']}\n"
			]
		
		string(WeaponDisplay)

	def WeaponEquip():
		if inventory[x]['Equipped'] == True:
			string("THIS ITEM IS ALREADY EQUIPPED\n")
		else:
			for i in inventory:
				if inventory[i]['Equipped'] == True: 
					string("CANNOT EQUIP MORE THAN ONE WEAPON AT A TIME\n")
					break
				else:
					inventory[x]['Equipped'] = True
					PlayerEquipment.append(x)
					string(f"{x} HAS BEEN EQUIPPED\n")
					break
				
	def WeaponUnequip():
		if inventory[x]['Equipped'] == False:
			string("THIS ITEM IS NOT EQUIPPED\n")
		else:
			inventory[x]['Equipped'] = False
			PlayerEquipment.remove(x)
			string(f"{x} HAS BEEN UNEQUIPPED\n")

	def WeaponDrop():
		if inventory[x]['Equipped'] == True:
			string("CANNOT DROP EQUIPPED ITEMS\n")
			Item_Menu()
		elif inventory[x]['Equipped'] == False:
			string("YOU'RE ABOUT TO PERMANENTLY DROP THIS ITEM, ARE YOU SURE?\n[1] YES\n[2] NO")
			choice = input(":")
			if choice == "1":
				string(f"YOU HAVE DROPPED {inventory[x]['ItemName']}")
				del inventory[x]
				menu()
			elif choice == "2":
				Item_Menu()

	def Item_Menu():
		string("[1] EQUIP ITEM")
		string("[2] UNEQUIP ITEM")
		string("[3] DROP ITEM")
		string("[4] BACK")
		PlayerChoice = input(":")

		if PlayerChoice == "1":
			WeaponEquip()
			Item_Menu()
		elif PlayerChoice == "2":
			WeaponUnequip()
			Item_Menu()
		elif PlayerChoice == "3":
			WeaponDrop()
			menu()
		elif PlayerChoice == "4":
			menu()
		else:
			Item_Menu()

	WeaponStatsDisplay()
	Item_Menu()


def menu():
	pass

	def inventoryMenus():
		os.system("cls")
		string("THIS IS YOUR INVENTORY\n")
		for x in inventory:
			string(f" - {inventory[x]['ItemName']}")

		string("\n THESE ARE YOUR EQUIPED ITEMS\n")
		for x in PlayerEquipment:
			string(f" - {x}")

		string("\nWHAT ITEM WOULD YOU LIKE TO LOOK AT? (TYPE BACK TO GO TO PREVIOUS MENU)\n")
		WeaponInspectItem = input(":")

		if WeaponInspectItem.lower() == "back":
			os.system("cls")
			return 0
		
		else:
			os.system("cls")
			Weaponinspect(WeaponInspectItem.upper())
		
	inventoryMenus()


