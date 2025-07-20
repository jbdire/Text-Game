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

#Simple function that takes in an integer and returns the name associated with it
def get_room(current):
    return rooms.get(current)

#Function that prompts the player to decide which direction to go based on where they are currently
def travel(room):
    if room == 1 or 3 or 4:
        choice = int(input(f'You are at {room} you can go East or West\nType [1] to go East\nType [2] to go West\n'))
    elif room == 0 or 2 or 5 or 6:
        choice = int(input(f'You are at {room} you can go North or South\nType [1] to go North\nType [2] to go South\n'))
    return choice

#Welcom/'Main Menu'
print('You wake up and look out your window.  The witches hut is glowing bright colors and you hear screams.')
print('There must be something you can do!')
print('You must visit your fellow viliagers and collect items to seige the witches hut!')
next = int(input('Type [1] to play!'))

#Game starts!
#Room is set by the starting point '0' and choice is set by the travel function
#Finally we update the room variable based on which direction the player chooses to go
if next == 1:
    room = get_room(0)
    choice = travel(room)
    if choice == 1:
        print('Heading North!\n\n\n')
        room = get_room(1)
    elif choice == 2:
        print('Heading West!\n\n\n')
        room = get_room(3)