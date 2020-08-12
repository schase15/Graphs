"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # Instantiate a graph class with an empty dictionary to hold the different 
        # nodes of the graph
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # Create a vertex, add it to the dictionary
        # For the vertex, start a set to hold the list of neighbors its connected to
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Make sure the verticies exist to make the connection
        if v1 in self.vertices and v2 in self.vertices:
            # Add the v2 as to the list of neighbors for v1
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # Return the list of neighbors
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # Add the starting index to the queue
        q.enqueue(starting_vertex)
        # Create empty set for visited vertices
        visited = set()
        # While gueue is not empty
        while q.size() > 0:
            # Dequeue a vertex
            v = q.dequeue()
            # If vertex not visited
            if v not in visited:
                # Visit it! Perform whatever we are doing to it
                print(v)
                # Mark as visited
                visited.add(v)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Stack()
        # Add the starting index to the queue
        q.push(starting_vertex)
        # Create empty set for visited vertices
        visited = set()
        # While queue is not empty
        while q.size() > 0:
            # Dequeue a vertex
            v = q.pop()
            # If vertex not visited
            if v not in visited:
                # Visit it! Perform whatever we are doing to it
                print(v)
                # Mark as visited
                visited.add(v)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        Visited default is a blank set, as vertices are visited and added, we will 
        pass the updated visited set to the next call
        """
        # When python default is immutable, it is processed weirdly
        # use this type of format to get initialize a set for the first time
        if visited is None:
            visited = set()

        vertex = starting_vertex

        # if we have visited it, skip over it
        if vertex in visited:
            return
        # Otherwise, print, add it to visited, recursive call on each neighbor
        else:
            # Print
            print(vertex)
            # Add vertex to visited
            visited.add(vertex)
            # For each neighbor, recursive call
            for n_vertex in self.get_neighbors(vertex):
                # Pass in the neighbor vertex and the updated visited
                self.dft_recursive(n_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # and enqueue A PATH TO the starting vertex ID
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]

            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path

                # If it isn't the target, continue your search
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    # Copy the path
                    next_path = path[:]
                    # append the neighbor vertex to it
                    next_path.append(neighbor)
                    # add the next path to the end of the queue
                    q.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        q = Stack()
        # and enqueue A PATH TO the starting vertex ID
        q.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.pop()
            # Grab the last vertex from the PATH
            v = path[-1]

            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path

                # If it isn't the target, continue your search
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    # Copy the path
                    next_path = path[:]
                    # append the neighbor vertex to it
                    next_path.append(neighbor)
                    # add the next path to the end of the queue
                    q.push(next_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        Default visited is empty set
        """
        # Start with an empty visited set
        visited = set()

        def inner_dfs(path):
            
            # Grab the last vertex from the PATH
            v = path[-1]

            # CHECK IF IT'S THE TARGET
            if v == destination_vertex:
                # IF SO, RETURN PATH
                return path

            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue -recursive call
                for neighbor in self.get_neighbors(v):
                    # Copy the path - each recursive call needs a new copy of the path
                    # The previous call is still utilizing the previous version of the path object
                    next_path = path[:]
                    # append the neighbor vertex to it
                    next_path.append(neighbor)
                    # Recursive function with updated path and visited set
                    found = inner_dfs(next_path)

                    # We need a way to return the found path from all the recursive calls
                    # Check to see if a path or if None is passed back
                    # Continues to get passed along to the original call which will return the path

                    # If the destination vertex is found, return the path
                    if found:
                        return found

        # use the starting vertex for the first call
        return inner_dfs([starting_vertex])








if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    print("_______________________________________")

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
