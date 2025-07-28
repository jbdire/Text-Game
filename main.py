#Dictionary for Rooms
rooms = {
    0: 'The Town Square',
    1: 'The Pub',
    2: 'The Library',
    3: 'The Apothecary',
    4: 'The Amory',
    5: 'The Market',
    6: 'The Alley',
    7: 'The WitchesHut'
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
    if current == 0:
        choice = int(input(f'You are currently at {current}, You can go\nNorth[1]\nSouth[2]\nEast[3]\nWest[3]\nType [1] [2] [3] or [4]'))
        if choice == 1:
            choice = f'{current}_north'
        elif choice == 2:
            choice = f'{current}_south'
        elif choice == 3:
            choice = f'{current}_east'
        elif choice == 3:
            choice = f'{current}_west'
    
    
#Function that enters the current room and tells you what item is inside
#Also shows inventory and updates inventory
def inside(room):
    roomName = rooms.get(room)
    item = items.get(room)
    print(f'Welcome to {roomName}')
    print(f'You found {item} in {roomName}!')
    print(f'{item} has been added to your inventory!')
    inventory.append(item)
    choice = int(input(f'Are you ready to move on?\n[1] Yes\n[2] View inventory'))
    if choice == 1:
        print("Let's Go!")
    elif choice == 2:
        print(f'Inventory: {inventory}')
    else:
        print("Let's Go!")
    return room
    
inventory = []

#Welcom/'Main Menu'
print('You wake up and look out your window.  The witches hut is glowing bright colors and you hear screams.')
print('There must be something you can do!')
print('You must visit your fellow viliagers and collect items to seige the witches hut!')
input('Press enter to play')



current = 0
while inventory != '1 Beer' and inventory != '1 Spellbook' and inventory != '4 Potions' and inventory != '1 Sword' and inventory != '3 Pieces of Bread' and inventory != '1 Strange Dagger':
    choice = travel(current)
    room = inside(choice)

