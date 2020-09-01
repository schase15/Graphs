# Page to store to functions I made to call in the adv.py page

# Function will be called when the player enters a new room
# This will quickly identify directions it cannot travel
def update_poss_directions(player, traversal_graph):
    '''
    Pass in player, traversal_graph
    Update directions for that room - 
        If there is no exit in a certain direction, store None in that room's traversal graph
    Return nothing
    '''
    # Store current room ID
    room_value = player.current_room.id
    # Get exits for that room
    exits = player.current_room.get_exits()

    # For each cardinal direction
    for direction in ['n', 's', 'w', 'e']:
        # If you can't move in that direction
        if direction not in exits:
            # Update dictionary to fill in None's
            traversal_graph[room_value][direction] = None


# Function will be called to move the player
def move_player(player, visited, traversal_graph, traversal_path, world):
    '''
    Pass in player, visited, traversal_graph, traversal_path, world
    Check to see if the new room has been visited
        If it hasn't call the update_poss_directions function
        Add it to the visited set
    Check to see if there are unexplored directions to move in
        If there are:
            Move the payer in a possible direction
            Update the connections in the direction the player moves
                Both for the room that the player is leaving and for the 
                room that the player is entering
            Add the movement to the traversal path
        If there are no more unexplored exits - Call BFS
    '''
    import random

    # Save current room ID
    curr_id = player.current_room.id

    # Check if this room has been visited before
    if curr_id not in visited:
        # Update the possible directions
        update_poss_directions(player, traversal_graph)
        # Add the room to the visited set
        visited.add(curr_id)

    # For the room you are in, pick a random unexplored direction and move the player there
    poss_directions = []

    # Find if the room has an unexplored exit
    for key, value in traversal_graph[curr_id].items():
        if value == '?':
            poss_directions.append(key)

    # Check to see if there are possible directions to move in
    # If there aren't, call BFS
    if len(poss_directions) == 0:
        # Call BFS
        # print('No where to go')
        return bfs(player, visited, traversal_graph, traversal_path, world)
    
    else:
        # Save direction choice
        move_to = random.choice(poss_directions)

        # Set connection you are moving to before moving
        traversal_graph[curr_id][move_to] = player.current_room.get_room_in_direction(move_to).id

        # Move in a possible direction
        player.travel(move_to)

        # For the new room, set the direction that you just came from
        new_room = player.current_room.id

        if move_to == 'n':
            traversal_graph[new_room]['s'] = curr_id
        if move_to == 'e':
            traversal_graph[new_room]['w'] = curr_id
        if move_to == 's':
            traversal_graph[new_room]['n'] = curr_id
        if move_to == 'w':
            traversal_graph[new_room]['e'] = curr_id

        # Add the direction you went to the traversal_path
        traversal_path.append(move_to)

        # Recall the method
        move_player(player, visited, traversal_graph, traversal_path, world)

# To be used in BFS function
class Queue():
    '''
    Basic queue, first in first out operation for breadth first searching
    '''
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Helper function to get neighbors
def get_neighbors(room_id, world):
    '''
    Takes in one room_id
    Returns neighbors room_ids
        Neighbors are the rooms connected in each cardinal direction
    '''
    # Empty neighbors list
    neighbors = []
    # Grab the current room 
    current_room = world.rooms[room_id]
    # Grab the exits
    exits = current_room.get_exits()
    # Grab room_id's in each direction and add to neighbors list
    for direction in exits:
        neighbors.append(current_room.get_room_in_direction(direction).id)
    # Return room id's of the neighbors
    return neighbors

# Function to find the closest room with an unexplored exit
def bfs(player, visited, traversal_graph, traversal_path, world):
    '''
    Takes in all variables
    Finds the closest room with an unexplored exit
        Moves the player there
        Adds the cardinal directions to get there to the traversal path
    Calls the move_player function at the end to explore the new unexplored exit
    '''
    # Starting point is the dead-end room the player is currently in
    starting_vertex = player.current_room.id

    # Create an empty queue
    q = Queue()
    # and enqueue A PATH TO the starting room ID
    q.enqueue([starting_vertex])
    # Create a Set to store visited room's
    visited_bfs = set()

    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first PATH
        path = q.dequeue()
        # Grab the last room from the PATH
        v = path[-1]

        # If that room has not been visited...
        if v not in visited_bfs:

            # Find if the room has an unexplored exit
            poss_directions = []
            for key, value in traversal_graph[v].items():
                if value == '?':
                    poss_directions.append(key)        

            # If poss_directions isn't empty, that is the room we need to move to
            if len(poss_directions) > 0:
                # print('move to unexplored room')

                # Convert path to cardinal directions
                cardinal_dir = convert_to_cardinal(path, traversal_graph)

                # Append cardinal directions to traversal_path
                for item in cardinal_dir:
                    traversal_path.append(item)

                # Move the player to that room
                player.current_room = world.rooms[v]
                # print(f'Moved to: room {player.current_room.id}')
                # Call the move player function from the new room
                move_player(player, visited, traversal_graph, traversal_path, world)
                # End the while loop
                break

            # If it isn't the target, continue your search
            # Mark it as visited...
            visited_bfs.add(v)
            # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in get_neighbors(v, world):
                # Copy the path
                next_path = path[:]
                # append the neighbor room to it
                next_path.append(neighbor)
                # add the next path to the end of the queue
                q.enqueue(next_path)

# Helper function to convert the output of the BFS to cardinal directions
def convert_to_cardinal(path, traversal_graph):
    '''
    Takes in a list of room id's (integers)
    Returns a list of the cardinal directions needed to travel that path
    '''
    cardinal_path = []
    # Comparing two rooms in the list, so for range -1 of the length of the path list
    for i in range(len(path) -1):
        # For each room in the path in order
        d = traversal_graph[path[i]]

        for key, value in d.items():
            # Find the next room id value in the first room's connections
            if value == path[i+1]:
                # The key will be the direction to that next connected room
                cardinal_path.append(key)

    return cardinal_path
