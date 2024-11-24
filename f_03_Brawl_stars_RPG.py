import random
import time

# Char
Poison = "crow"
Bomb = "grom"
Shotgun = "shelly"
Cactus = "spike"
gun = "colt"
morbin = "mortis"
tank = "frank"

# Outputs
all_numbers = []
generate = random.randint(1, 1)
Heal_gen = random.randint(1, 5)

# dmg
Poison_DMG = 300
Bomb_DMG = 350
Shotgun_DMG = 500
Cactus_DMG = 450
gun_DMG = 300
morbin_DMG = 250
tank_DMG = 350

# HP
Poison_HP = 1200
Bomb_HP = 1400
Shotgun_HP = 1700
Cactus_HP = 1200
gun_HP = 1300
morbin_HP = 1500
tank_HP = 2000

# Healing_mech
Heal = Heal_gen * 75
No_Heal = 0

# Char select
print("Choose your character")
char_slct = input('''
         1.Crow
         2.Grom
         3.Shelly
         4.Spike
         5.Colt
         6.Mortis
         7.Frank
''')

if char_slct == "crow":
    print(f"You selected Crow!")
if char_slct == "grom":
    print(f"You selected Grom!")
if char_slct == "shelly":
    print(f"You selected Shelly!")
if char_slct == "spike":
    print(f"You selected Spike!")
if char_slct == "colt":
    print(f"You selected Colt!")
if char_slct == "mortis":
    print(f"You selected Mortis!")
if char_slct == "frank":
    print(f"You selected Frank!")

# DMG_calc
if char_slct == "crow":
    Main_ATK = Poison_DMG
if char_slct == "grom":
    Main_ATK = Bomb_DMG
if char_slct == "shelly":
    Main_ATK = Shotgun_DMG
if char_slct == "spike":
    Main_ATK = Cactus_DMG
if char_slct == "colt":
    Main_ATK = gun_DMG
if char_slct == "mortis":
    Main_ATK = morbin_DMG
if char_slct == "frank":
    Main_ATK = tank_DMG

# DMG_calc
if char_slct == "crow":
    Main_HP = Poison_HP
if char_slct == "grom":
    Main_HP = Bomb_HP
if char_slct == "shelly":
    Main_HP = Shotgun_HP
if char_slct == "spike":
    Main_HP = Cactus_HP
if char_slct == "colt":
    Main_HP = gun_HP
if char_slct == "mortis":
    Main_HP = morbin_HP
if char_slct == "frank":
    Main_HP = tank_HP

# Boss_stats
Boss_HP = 3000
Boss_DMG = 200

# Loading match
print("Loading into match...")
time.sleep(0.5)
print('''
    3...)
    2...
    1...
    ''')
print("BEGIN!")

# Main_Sim
print(generate)
if generate == 1:
    print("You encounter the BOSS!")
    time.sleep(0.3)
    Fight_Boss = input("Fight or run? ")
    if Fight_Boss == "fight":
        print("You started attacking the BOSS")
        time.sleep(0.8)
    else:
        print('''You failed to run away
        
        restart the simulation ''')

while Boss_HP > 0 and Main_HP > 0:
    if Fight_Boss == "fight":
        print(f"You dealt {Main_ATK} to the BOSS")
        Boss_HP -= Main_ATK
        time.sleep(0.8)

        print(f"BOSS is now at {Boss_HP} HP")
        time.sleep(0.8)

        print(f"Boss deals {Boss_DMG}")
        Main_HP -= Boss_DMG
        time.sleep(0.8)

        print(f"Your HP is at {Main_HP}")
        time.sleep(0.8)

        Heal_question = input("Do you want to heal? ")
        if Heal_question == "yes":
            print(f"you healed {Heal}HP ")
            Main_HP += Heal
        else:
            print("you did not heal")
            Main_HP += No_Heal
        time.sleep(0.8)

# Defeating_the_boss
if Boss_HP <= 0:
    print("You defeated the BOSS!!! ")

# Defeating_the_Player
if Main_HP <= 0:
    print("You were defeated by the BOSS!!! ")
