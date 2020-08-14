from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)



################################ MY CODE #############################################

# Import helper functions
from util import *

# Build an empty graph dictionary
traversal_graph = {}
# 500 rooms, 0-499
for room_id in range(len(world.rooms)):
    traversal_graph[room_id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Create empty visited set
visited = set()




## testing functions and traversal ##
move_player(player, visited, traversal_graph, traversal_path, world)


print(traversal_graph)
print(traversal_path)
print(len(traversal_path))
print(visited)
print(player.current_room.id)
print('_________________________')

'''
Everything is working up to here
It traverses the map and visits every node and populates the traversal graph properly
    I checked and the output is right for all of the smaller maps

Just need to convert the path from the BFS output to cardinal directions
'''

# breakpoint()


############################# TESTING ################################################

# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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