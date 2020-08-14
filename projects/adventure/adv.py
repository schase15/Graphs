# Sprint Challenge Adventure
#### Best Score is 966 moves ######

'''
Understand:
    Graph of 500 rooms
    Must visit every room at least once - in as few steps as possible
    Return a list of cardinal directions to walk through the graph

    You are starting in room 0 which the player has the ability to move n,e,s,w to connected rooms
        Move in one direction, record what room you are now in
            Move to rooms that room is connected to and record what is n s e and w of it
    Add all of this information in a dictionary as you traverse
        {room ID: {'n': ?, 's': ?, 'w': ?, 'e': ?}

    You should pick a direction, traverse depth first recording cardinal information
    Once you hit a room where every direction has been explored, 
        use BFS to find the closest unexplored exit (target of a direction with a ?)

    Output needs to be a list of steps taken
        Record the cardinal direction you moved to get from room to room, not the room ID's

    Move the player by player.travel('n')
        Will move the player north 1 room , if you can't go that way it will tell you
        Has attribute self.current_room

    Room class:
        get_room_in_direction() returns room object in that direction
        get_exits() returns list of cardinal directions you can move in from that room
'''

'''
Plan:
    Build out a dictionary with each room ID as a key and the value a dictionary of unknown n,e,s,w values
        As we traverse the graph we will update these values, and use the ? as indicators that direction hasn't been explored
            If we can't travel in a certain direction, overwrite the ? with a None
            Otherwise, overwrite the ? with the room ID as you move in that direction
                Or as you enter a room from that direction
    As you move, you need to update a few things:
        1. Add the cardinal direction you are moving to the traversal path list
            Every time you move even if you are just moving to the next unknown exit to explore
        2. Add the new room ID to the previous room's cardinal direction dictionary
            Only if the exit has not been explored before
        3. When you enter a room, replace any direction you can't move with None
            Add the information for the direction you just came in
'''

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Import helper functions
from util import *

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

# Put the program inside a while loop to try to find a route under 960
# The computer makes a random choice when it decids what direction to move in, the route lengths vary
traversal_path = [0] * 1000

counter = 0

while len(traversal_path) >= 960:

    # Count loops to watch the program run
    counter += 1
    print(counter)

    # Instantiate player
    player = Player(world.starting_room)

    # Build an empty graph dictionary
    traversal_graph = {}

    # Based on the size of the map you are working with
    for room_id in range(len(world.rooms)):
        traversal_graph[room_id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

    # Fill this out with directions to walk
    # traversal_path = ['n', 'n']
    traversal_path = []

    # Create empty visited set
    visited = set()

    # Run my program to populate traversal path
    move_player(player, visited, traversal_graph, traversal_path, world)

print('_______________________________________________')
print('DONE!')
print(f"Length of Traversal Path: {len(traversal_path)}")
print(f"Traversal Path is: {traversal_path}")


print("______________________________________")
print('Start of test')

############################ TESTING ################################################

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
