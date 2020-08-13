# Page to store to functions I made to call in the adv.py page

###### UPDATE THE FUNCTIONS TO READ GLOBAL VARIABLES ##########
    # So you don't have to pass in all the variables, you can just call it

# Function will be called when the player enters a new room
# This will quickly identify directions it cannot travel
def update_poss_directions(player, traversal_graph):
    '''
    Pass in player
    Update directions for that room - 
        If there is no exit in a certain direction, store None in that room's traversal graph
    Return nothing
    '''
    # Store current room ID
    room_value = player.current_room.id
    # Get exits
    exits = player.current_room.get_exits()

    # For each cardinal direction
    for direction in ['n', 's', 'w', 'e']:
        # If you can't move in that direction
        if direction not in exits:
            # Update dictionary to fill in None's
            traversal_graph[room_value][direction] = None


# Function will be called to move the player
# NEED TO UPDATE TO INCLUDE A BREAK THAT WILL CALL BFS WHEN WE THERE ARE NO UNEXPLORED EXITS
def move_player(player, visited, traversal_graph, traversal_path):
    '''
    Pass in player
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
        If there are not
            Call BFS
    '''

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
        # To work with in production
        return print('No where to go')
    
    else:
        # Save direction choice
        move_to = poss_directions[0]

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
        move_player(player, visited, traversal_graph, traversal_path)

