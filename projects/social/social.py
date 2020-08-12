import random

from queue import Queue

class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'User({repr(self.name)})'

class SocialGraph:
    def __init__(self):
        self.reset()

    # Creates bi-drectional edges: undirected graph
    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    # Adds a vertex
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def reset(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.reset()

        # Add users - numbers for the range of number of users input
        # Creates a list of user classes
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create all possible friendships
        possible_friendships = []

        # For each user in our users list, create tuples with each userID they can be friends with
        for user_id in self.users:
            # Possible friends for the user is the next user and all the users until the end
                # All of the nodes in infront of the user_ID have already created a friendship connecting the two
            for friend_id in range(user_id + 1, self.last_id + 1):
                # Tuples with (the userid, someone they could be friends with)
                possible_friendships.append((user_id, friend_id))

        # Randomize the list of possible friendship tuples
        random.shuffle(possible_friendships)

        # From the randomized list of friendships, we want to select the first i
            # Where i is the number of users times the average number of friendships(input)
                # Divided by 2 because the add_friendship function creates 2 friendships at once
        for i in range(num_users * avg_friendships // 2):
            # Select the tuple
            friendships = possible_friendships[i]
            # Add that tuple as a friendship
            self.add_friendship(friendships[0], friendships[1])

    # Helper get_friends method to be able to do BFT
    # Friendships are stored in a dictionary self.friendships
        # {vertex_id: set of friends}
    def get_neighbors(self, v):
        return self.friendships[v]

    # Path finding, given user to start from
    # How to you get from user#1 to every other user in in the connected social network
    # Return will be a dictionary with key being the node in the network and the value 
        # pair being the path it takes to get there from the input node
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        '''
        Plan:
            Use a BFT to visit every node, 
                If the node hasn't been visited, add it to the visited dictionary
                    {visited_node: path to get there}
                    Add its neighbors to the queue
                If it already has been visited, skip it and continue
            After queue is empty, return the populated visited dictionary
        '''
        # Create an empty queue
        q = Queue()

        # Start the queue with the input user - it should be a queue of lists
        q.enqueue([user_id])

        # Create a visited dictionary to store the node and the path to get there
            # {user_id: path}
        visited = {}

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # Grab the last vertex of the path
            v = path[-1]
            # If the vertex has not been visited, store vertex user_id and path to get there
            if v not in visited:
                # Add it to visited dictionary
                visited[v] = path
                # Get the neighbors of v, add them to the queue
                for neighbor in self.get_neighbors(v):
                    # Copy the path
                    next_path = path[:]
                    # append the neighbor vertex to it
                    next_path.append(neighbor)
                    # add the next path to the end of the queue
                    q.enqueue(next_path)

        # If we get here, all points have been traversed and added to the visited dictionary
        return visited

    # Method to answer question 3 part 2, percentage of users in a particular user's extended network
    def percent_users(self, user_id):
        # Get the number of users in the input users social network
            # That is, the length of the keys of the visited dictionary minus 1 (themselves)
        friends_dict = self.get_all_social_paths(user_id)
        num_friends = len(friends_dict.keys()) - 1

        # Divide this result by the total number of users in the system
            # Length of the keys of the self.users dictionary minus 1 (the original user)
        total_users = len(self.users.keys()) - 1

        percentage = num_friends / total_users

        return f"User {user_id}'s friend list is {percentage * 100}% of the total users"

    # Method to calculate average degrees of separation
    def avg_separation(self, user_id):
        # Create friends dictionary
        friends = self.get_all_social_paths(user_id)
        # Create total length counter
        length = 0
        # For each key in the visited dictionary, add the length of the value pair list
        for path in friends.items():
            length += len(path)
        # Divide this length by the number of friends the user has
        avg_sep = length / len(friends.keys())

        return f"The average degree of separation between user {user_id} and those in their extended network is: {avg_sep}"

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    print(sg.percent_users(1))
    print(sg.avg_separation(1))


'''
Questions:
1) You would have to call add_friendship() 500 times. To create 100 users with an average of 
    10 friends each, you need to form 1000 friendships. The function add_friendship() creates 2 
    friendships on each call. So we would need to call it 500 times to create 1000 friendships.

2) If there are 1000 users with an average of 5 random friends each, 99.6% of other users will 
    be in a particular user's extended social network.
    The average degree of separation between a particular user and and their extended network is 2.0.

'''



