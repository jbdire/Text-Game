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

#Function to return a string of the name of the room that corresponds to the number associated with the 'loc' variable
def get_room(current):
    for i in range(len(rooms)):
        if current == rooms[i]:
            return rooms[i]

#Function that prompts the player to decide which direction to go based on where they are currently
def travel(room):
    if room == 1 or 3 or 4:
        choice = int(input(f'You are at {room} you can go East or West\nType [1] to go East\nType [2] to go West\n'))
    elif room == 0 or 2 or 5 or 6:
        choice = int(input(f'You are at {room} you can go North or South\nType [1] to go North\nType [2] to go South\n'))
    return choice

#First working line of code!
#This gets user input and stores it as a number value inside of 'choice'
choice = travel(rooms[0])
