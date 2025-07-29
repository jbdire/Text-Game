import curses
#Dictionary for Rooms
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
        if choice == 1:
            return 1
        elif choice == 2:
            return 2
        elif choice == 3:
            return 3
        elif choice == 4:
            return 4
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
            return room




        
    
    
#Function that enters the current room and tells you what item is inside
#Also shows inventory and updates inventory
def inside(room):
    roomName = rooms.get(room)
    item = items.get(room)
    if item in items:
        print("You've been here before")
        print(f'You are in {roomName}')
    else:
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
input('Press enter to play\n')



current = 0
while True:
    current = travel(current)
    choice = inside(current)
