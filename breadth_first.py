from collections import deque

# Define the graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []

# Initialize the search queue
search_queue = deque()
search_queue += graph["you"]
searched = []

def person_is_seller(name):
    return name[-1] == 'm'

def bfs_seller_search():
    global search_queue
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
    return False  # This line is outside the loop

# Call the function to start the search
bfs_seller_search()
