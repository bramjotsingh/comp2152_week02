import random

# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']

print("Available Weapons:", ', '.join(weapons))

# Inputs with error handling
combatStrength = input("Enter the hero's combat strength (1-6): ")
if not combatStrength.isdigit() or int(combatStrength) < 1 or int(combatStrength) > 6:
    print("Invalid input: Combat strength should be a number between 1 and 6.")
    combatStrength = 1  # Default value for invalid input
else:
    combatStrength = int(combatStrength)

mCombatStrength = input("Enter the monster's combat strength (1-6): ")
if not mCombatStrength.isdigit() or int(mCombatStrength) < 1 or int(mCombatStrength) > 6:
    print("Invalid input: Monster combat strength should be a number between 1 and 6.")
    mCombatStrength = 1  # Default value for invalid input
else:
    mCombatStrength = int(mCombatStrength)

# Simulate battle rounds
for j in range(1, 21, 2):  # Simulation of 20 rounds, stepping by 2
    # Dice rolls for hero and monster
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)
    
    # Hero weapon selection
    weaponRoll = heroRoll  # Use heroRoll for weapon selection
    heroWeapon = weapons[weaponRoll - 1]
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")
    if heroWeapon != 'Fist':
        print("Thank goodness you didn't roll the Fist...")

    monsterWeapon = weapons[monsterRoll - 1]
    
    # Calculate total strength
    heroTotal = combatStrength + weaponRoll
    monsterTotal = mCombatStrength + monsterRoll
    
    # Print round details
    print(f"\nRound {j}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}")
    print(f"Hero selected {heroWeapon}, Monster selected {monsterWeapon}")
    print(f"Hero total strength: {heroTotal}, Monster total strength: {monsterTotal}")
    
    # Determine winner
    if heroTotal > monsterTotal:
        print("Hero wins the round")
    elif heroTotal < monsterTotal:
        print("Monster wins the round")
    else:
        print("That's a tie")
    
    # Truce condition
    if j == 11:
        print("\nBattle truce declared in round 11. Game Over!")
        break

# End of battle
if j != 11:
    print("\nBattle concluded after 20 rounds")
