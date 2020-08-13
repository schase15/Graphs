from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)



################################ MY CODE #############################################

# Import helper functions
from util import move_player, update_poss_directions

# Build an empty graph dictionary
traversal_graph = {}
# 500 rooms, 0-499
for room_id in range(3):
    traversal_graph[room_id] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# Create empty visited set
visited = set()




## testing functions and traversal ##


move_player(player, visited, traversal_graph, traversal_path)

print(traversal_graph)
print(traversal_path)
print(visited)
print(player.current_room.id)
print('_________________________')

# move_player(player, visited, traversal_graph, traversal_path)

# print(traversal_graph)
# print(traversal_path)
# print(visited)
# print(player.current_room.id)
# print('_________________________')

# x = move_player(player, visited, traversal_graph, traversal_path)
# print(traversal_graph)
# print(traversal_path)
# print(visited)
# print(player.current_room.id)
# print('_________________________')



# if x == 1:
    # bfs functionality
    # If we got here, that means in our traverse we have hit a room where all exists have
    # been explored
    # We need to move to the nearest room with an unexplored exit and continue to call move_player





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