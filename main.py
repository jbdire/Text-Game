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
    if current == 1 or 3 or 4:
        choice = int(input(f'You are at {current} you can go East or West\nType [1] to go East\nType [2] to go West\n'))
    elif current == 0 or 2 or 5 or 6:
        choice = int(input(f'You are at {current} you can go North or South\nType [1] to go North\nType [2] to go South\n'))
    return choice

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
    
inventory = []

#Welcom/'Main Menu'
print('You wake up and look out your window.  The witches hut is glowing bright colors and you hear screams.')
print('There must be something you can do!')
print('You must visit your fellow viliagers and collect items to seige the witches hut!')
next = int(input('Type [1] to play!'))

#Game starts!
#Room is set by the starting point '0' and choice is set by the travel function
#Finally we update the room variable based on which direction the player chooses to go
if next == 1:
    room = 0
    choice = travel(0)
    if choice == 1:
        print('Heading North!\n\n\n')
        inside(1)
    elif choice == 2:
        print('Heading South!\n\n\n')
        inside(3)
