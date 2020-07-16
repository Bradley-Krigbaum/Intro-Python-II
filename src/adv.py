from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_char = {
    'name': 'Brad',
    'room': 'outside'
}

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


current_room = player_char['room']
selected_room = ''


while True:
    # if player_char['name'].lower() == 'brad':
    #     player_char['name'] = input("\nWhat is your name adventurer?\n>  ")

    # if player_char['name'].lower() == '':
    #     player_char['name'] = 'nobody'.upper()

    if player_char['room'] == 'outside':
        current_room = player_char['room']
        room_description = room[current_room].__str__()
        print(F"\nHello, Adventurer.\nYou are currently {room[current_room]}")
        player_input = input("\n\nwhere to go?\npress N, N, N or... N?\n>  ")

        if player_input.lower() == 'n':
            selected_room = room[current_room].n_to
            current_room = 'foyer'
            player_char['room'] = current_room
            # print(current_room)
            print(F"\n\n\n\n\n    You entered the {selected_room}\n\n\n\n")
            new_input = input("Walk N, S, or E?\n>  ")

        elif player_input.lower() == 'q' or 'quit' or 'exit':
            break
        else:
            print("\n\nThat movement isn't allowed!\nPlease input a real direction!")

    elif player_char['room'] == 'foyer':
        if new_input.lower() == 's':
            selected_room = room[current_room].s_to
            current_room = 'outside'
            player_char['room'] = current_room
            print(F"\n\n\n\n\n\n\n\n    You walked South.\n{selected_room}\n\n\n\n\n\n\n\n")

        elif new_input.lower() == 'n':
            selected_room = room[current_room].n_to
            current_room = 'overlook'
            player_char['room'] = current_room
            print(F"\n\n\n\n\n\n\n\n    You walked North.\n{selected_room}\n\n\n\n\n\n\n\n")

        elif new_input.lower() == 'e':
            selected_room = room[current_room].e_to
            current_room = 'narrow'
            player_char['room'] = current_room
            print(F"\n\n\n\n\n\n\n\n    You walked Ease.\n{selected_room}\n\n\n\n\n\n\n\n")

        elif new_input.lower() == 'q' or 'quit' or 'exit':
            break
        else:
            print("\n\nThat movement isn't allowed!\nPlease input a real direction!")

    elif player_char['room'] == 'overlook':
        print(player_char['room'])
        break
        # elif new_input.lower() == 'q' or 'quit' or 'exit':
        #     break
        # else:
        #     print("\n\nThat movement isn't allowed!\nPlease input a real direction!")

    elif player_char['room'] == 'narrow':
        print(player_char['room'])
        break
        # elif new_input.lower() == 'q' or 'quit' or 'exit':
        #     break
        # else:
        #     print("\n\nThat movement isn't allowed!\nPlease input a real direction!")

    elif player_char['room'] == 'treasure':
        print(player_char['room'])
        break
        # elif new_input.lower() == 'q' or 'quit' or 'exit':
        #     break
        # else:
        #     print("\n\nThat movement isn't allowed!\nPlease input a real direction!")

    elif player_input.lower() == 'q' or 'quit' or 'exit':
        break
    else:
        print("\n\nThat movement isn't allowed!\nPlease input a real direction!")
