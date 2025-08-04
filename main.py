#Dictionary for Rooms
from symbol import pass_stmt

rooms = {
    0: 'The Town Square', #North of the library #South of the pub #West of the apothecary #East of the armory
    1: 'The Pub', #North of the town square #West of the market
    2: 'The Library', #South of the town square
    3: 'The Apothecary', #East of the town square #South of the market
    4: 'The Amory', #West of the town square #North of the alley
    5: 'The Market', #East of the pub #North of the apothecary #East of the alley
    6: 'The Alley',#East of the market #South of the armory
    7: 'The WitchesHut'#South of the alley
}

#Dictionary for Items
items = {
    1: '1 Beer',
    2: '1 Spellbook',
    3: '4 Potions',
    4: '1 Sword',
    5: '3 Pieces of Bread',
    6: '1 Strange Dagger'
}

#Function that prompts the player to decide which direction to go based on where they are currently
def travel(room):
    current = rooms.get(room)
    if room == 0:
        print(f'Welcome to {current}!')
        choice = int(input(f'You can go in any cardinal direction.\n[1] North\n[2] South\n[3] East\n[4] West\n'))
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            return choice
        else:
            return print('Invalid choice')
    else:
        if room == 1:
            choice = int(input(f'You are in {current} you can go:\n[1] South\n[2] East\n'))
            if choice == 1:
                room = 0
                return room
            elif choice == 2:
                room = 5
                return room
            else:
                print('Invalid direction')
        if room == 2:
            print(f'You are in {current} you can only go North!\n')
            room = 0
            return room
        if room == 3:
            choice = int(input(f'You are in {current} you can go:\n[1] North\n[2] West\n'))
            if choice == 1:
                room = 4
                return room
            elif choice == 2:
                room = 0
                return room
            else:
                print('Invalid direction')
        if room == 4:
            choice = int(input(f'You are in {current} you can go:\n[1] East\n[2] South\n'))
            if choice == 1:
                room = 0
                return room
            elif choice == 2:
                room = 6
                return room
            else:
                print('Invalid direction')
        if room == 5:
            choice = int(input(f'You are in {current} you can go:\n[1] South\n[2] East\n[3] West\n'))
            if choice == 1:
                room = 3
                return room
            elif choice == 2:
                room = 6
                return room
            elif choice == 3:
                room = 1
                return room
            else:
                print('Invalid direction')
        if room == 6:
            choice = int(input(f'You are in {current} you can go:\n[1] North\n[2] South\n [3] East\n'))
            if choice == 1:
                room = 4
                return room
            elif choice == 2:
                room = 7
                return room
            elif choice == 3:
                room = 5
                return room
            else:
                print('Invalid Direction')
        if room == 7:
            if items in inventory:
                print('You Won!')
            if items not in inventory:
                print('You lost')
   
#Function that enters the current room and tells you what item is inside
#Also shows inventory and updates inventory
#If item is already in inventory, there is a short message and the function returns none
def inside(room):
    roomName = rooms.get(room)
    item = items.get(room)
    if item in inventory:
        print("You've been here before")
        print(f'You are in {roomName}')
        return None
    elif room == 0:
        return None
    elif room == 7:
        return None
    else:
        print(f'Welcome to {roomName}')
        print(f'You found {item} in {roomName}!')
        print(f'{item} has been added to your inventory!')
        inventory.append(item)
        choice = int(input(f'Are you ready to move on?\n[1] Yes\n[2] View inventory\n'))
        if choice == 1:
            print("Let's Go!")
        elif choice == 2:
            print('')
            print(f'Inventory:\n{inventory}')
        else:
            print("Let's Go!")
        return room
def on_win():
    print(f"You sneak your way around the mysterious Witch Hut and glance through the window\n"
          f"...\n"
          f"You take a bite out of your last piece of bread and drink up the rest of your beer\n"
          f"You take your last mana potion\n"
          f"You then slip through the window...\n"
          f"You whisper a spell you learnt from your spellbook\n"
          f"The witch blocks your spell and starts for you, you take out your sword but she's too quick\n"
          f"She sends a magic bolt towards the sword and it flies out of your hand\n"
          f"You try to think of another spell but you don't have enough time, the witch is whispering an incantation with an evil grin,\n"
          f"You begin to freeze up as you reach for your last weapon\n"
          f"Finally, as the ice begins to creep past your elbow, the dagger has already left your hand\n"
          f"As the dagger colides with the witch's shoulder, she burst into a bright blue flame\n"
          f"...\n"
          f"And just like that... Ding Dong the witch is dead!\n")
    return None
def on_lose():
    print("You don't have enough items in your inventory to defeat the witch yet...\n"
          "You lose, womp womp\n")
    return None

inventory = []

#Welcome/'Main Menu'
print('You wake up and look out your window.  The witches hut is glowing bright colors and you hear screams.')
print('There must be something you can do!')
print('You must visit your fellow viliagers and collect items to seige the witches hut!')
input('Press enter to play\n')

current = 0
while True:
    if current == 7:
        if all(item in inventory for item in items.values()):
            on_win()
            break
        else:
            on_lose()
            break
    current = travel(current)
    choice = inside(current)
