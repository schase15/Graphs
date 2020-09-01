from queue import Queue

'''
Understand:
    Given an input node, find the furthest away node it is connected to     
        When only able to move up the family tree
    If there are two equally far away ancesters, return the ancestor node with the lowest numeric ID
    If the input has no parents, return -1

    The input will provide an adjacency list to build the ancestor tree
'''

'''
Plan:
    Use the given adjacency list to build a directional graph where the edges only move upwards
    Use the starting node to perform a breadth first traversal saving each path as we did for the BF search
        Save each path to a list
        Find the shortest path in the list
            Return the last value of the path
            If there are two paths that are the longest, return the lower value
            If there are parents, return -1
'''

def earliest_ancestor(ancestors, starting_node):
    # Use the ancestor information to build a graph
        # Don't need a full graph, just information about what its parents are
    # Put it in a dictionary, the second value is the key and the first value is added to the list of neighbors
    # {node ID: [list of parents]}
    d = {}

    # For each node in the ancestors list
    for node in ancestors:
        # Initialize the key in the dictionary
        if node[1] not in d:
            d[node[1]] = []
        # Add the parents into the value list
        d[node[1]].append(node[0])
    # This creates a dictionary of all the nodes that have parents
    # If the node doesn't have a parent it isn't in the dictionary

    # Breadth first traversal saving completed paths to a list
    # Start at the starting node, if it has parents add the parents' paths to the queue
        # If it doesn't have parents that is the end of the path, add the completed path to the output list
    # Look at the last item in the path to see if that item has parents
        # if it does, add path to each parent to the queue
        # If it doesn't, add that path to the output list

    # Create an empty queue
    q = Queue()
    # Enqueue a path to the starting node
    q.enqueue([starting_node])
    # Create a set to store visited paths
    visited = set()

    # Create a list to store paths to compare lengths
    paths = []

    # While the queue is not empty
    while q.size() > 0:
        # Dequeue the first path
        path = q.dequeue()
        # Grab the last node of the path
        v = path[-1]
        # If the vertex has not been visited
        if v not in visited:
            # add it to visited
            visited.add(v)
            # If the vertex has a parent
            if v in d:
                # Add a path to its parents to the queue
                for parent in d[v]:
                    # Copy the path
                    next_path = path[:]
                    # Append the parent vertex to it
                    next_path.append(parent)
                    # Add the next path to the end of the queue
                    q.enqueue(next_path)
            else:
                # If v doesn't have any parents, add the completed path to the list of paths
                paths.append(path)
        else:
            continue
    # If we are here, we have calculated all the completed paths from the starting node

    # Find the longest path
    # If there are two longest paths, return the lower value end node
        # Sort the list by length of lists
            # If there is a tie sort again by the last value, ascending
    sorted_path = sorted(paths, key = lambda path: (-len(path), path[-1]))

    # Our oldest ancestor is the last item of the first list
    oldest_ancestor = sorted_path[0][-1]

    # If there is no paths (only the starting node), return -1
    # If the resulting path is equal to the starting node, return -1
    if oldest_ancestor == starting_node:
        return -1
    else:
        return oldest_ancestor


# Run example
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
print(earliest_ancestor(test_ancestors, 4))
print(earliest_ancestor(test_ancestors, 5))
print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 7))
print(earliest_ancestor(test_ancestors, 8))
print(earliest_ancestor(test_ancestors, 9))
print(earliest_ancestor(test_ancestors, 10))
print(earliest_ancestor(test_ancestors, 11))
