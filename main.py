# D&D simple simulator
import random
import math


def get_name() -> str:
    return input("Enter a character name : ")


def sum_of_four_six_sided_dice_with_lowest_dropped():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)

    lowest_d = min(d1, d2, d3, d4)
    if lowest_d == d1:
        return d2 + d3 + d4
    elif lowest_d == d2:
        return d1 + d3 + d4
    elif lowest_d == d3:
        return d1 + d2 + d4
    else:
        return d1 + d2 + d3


def get_ability_modifier(ability) -> int:
    modifier = math.floor((ability - 10) / 2)
    return modifier


def menu() -> int:
    print("1 - Attack")
    print("2 - Negotiate")
    print("3 - Search")
    print("4 - Eat")
    choice = int(input("Enter and action [1-4]:"))
    return choice


def roll_d20() -> int:
    rolled = random.randint(1, 20)
    return rolled


def roll_d6() -> int:
    rolled = random.randint(1, 6)
    return rolled


def get_random_loot() -> str:
    loot = ("100 Gold", "2 Ruby Gems", "+1 Sword of Fire", "+1 Ring of Protection from Evil", "Broken Helmet")
    return random.choice(loot)


# Main program.

# Get the player's character name.
character_name = get_name()

# Character Attributes.
strength = 1
dexterity = 1
constitution = 1
intelligence = 1
wisdom = 1
charisma = 1
roll_again = "y"
i = 4

while i > 0 and roll_again == "y":
    strength = sum_of_four_six_sided_dice_with_lowest_dropped()
    print("STR:", strength)
    dexterity = sum_of_four_six_sided_dice_with_lowest_dropped()
    print("DEX:", dexterity)
    constitution = sum_of_four_six_sided_dice_with_lowest_dropped()
    print("CON:", constitution)
    wisdom = sum_of_four_six_sided_dice_with_lowest_dropped()
    print("WIS:", wisdom)
    intelligence = sum_of_four_six_sided_dice_with_lowest_dropped()
    print("INT:", intelligence)
    charisma = sum_of_four_six_sided_dice_with_lowest_dropped()
    print("CHR:", charisma)
    i -= 1
    roll_again = input("Roll again? {} trie(s) remaining..".format(i+1))
else:
    print("Final results:")
    print("Name:", character_name)
    print("STR:", strength)
    print("DEX:", dexterity)
    print("CON:", constitution)
    print("INT:", intelligence)
    print("WIS:", wisdom)
    print("CHR:", charisma)

# Get user action choice.
print("You adventure begins!")
print("You approach a small hut with an odd man standing in the doorway.")
print("He looks at you with a cold stare of curiosity, do you...")

# Results of user action.
for x in range(4):
    user_action = menu()
    if user_action == 1:
        # Attack action.
        print("You attack!")
        if get_ability_modifier(strength) >= get_ability_modifier(dexterity):
            print("You need a 12 or better on d20 to succeed.")
            print("You have a STR modifier of {}".format(get_ability_modifier(strength)))
            player_modifier = get_ability_modifier(strength)
        else:
            print("You need a 12 or better on d20 to succeed.")
            print("You have a DEX modifier of {}".format(get_ability_modifier(dexterity)))
            player_modifier = get_ability_modifier(dexterity)
        player_rolled = roll_d20() + player_modifier
        if player_rolled >= 12:
            print("Player roll results = {} : HIT!".format(player_rolled))
            # Find damage done.
            damage_done = roll_d6() + get_ability_modifier(strength)
            if damage_done < 0:
                damage_done = 0
            print("You did {} point of damage!".format(damage_done))
        else:
            print("Player roll results = {} : MISS!".format(player_rolled))
    elif user_action == 2:
        # Negotiate action.
        print("You attempt to negotiate with them.")
        print("You need a 15 or better on d20 to succeed.")
        print("You have a CHR modifier of {}".format(get_ability_modifier(charisma)))
        player_rolled = roll_d20() + get_ability_modifier(charisma)
        if player_rolled >= 12:
            print("Player roll results = {} : Success!  You have negotiated a truce!".format(player_rolled))
        else:
            print("Player roll results = {} : Fail!  You have made the person very angry!".format(player_rolled))
    elif user_action == 3:
        # Search action.
        print("You attempt to search them.")
        if get_ability_modifier(wisdom) >= get_ability_modifier(intelligence):
            print("You need a 15 or better on d20 to succeed.")
            print("You have a WIS modifier of {}".format(get_ability_modifier(wisdom)))
            player_modifier = get_ability_modifier(wisdom)
        else:
            print("You need a 15 or better on d20 to succeed.")
            print("You have a INT modifier of {}".format(get_ability_modifier(intelligence)))
            player_modifier = get_ability_modifier(intelligence)
        player_rolled = roll_d20() + player_modifier
        if player_rolled >= 12:
            print("Player roll results = {} : Success!".format(player_rolled))
            player_loot = get_random_loot()
            print("You found [{}] on the person and take it for yourself!".format(player_loot))
        else:
            print("Player roll results = {} : Fail!".format(player_rolled))
            print("You find nothing on this person.")
    else:
        # Eat action.
        print("You decide to eat but you food is rancid!")
        print("Check Saving Throw against being sick.")
        print("You need a 10 or better on d20 to save against getting sick.")
        player_modifier = get_ability_modifier(constitution)
        print("you have a CON modifier of {}".format(player_modifier))
        player_rolled = roll_d20() + player_modifier
        if player_rolled >= 10:
            print("Player roll results = {} : Success!".format(player_rolled))
            print("You ate the rancid food like a champ, you must have an iron stomach!")
        else:
            print("Player roll results = {} : Fail!".format(player_rolled))
            print("You ate the rancid food and are now sick, shitting your pants uncontrollably!")
else:
    print("\nYour adventure is over.  Thanks for playing.")
