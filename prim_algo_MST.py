# Identifying minimum spanning tree using Prim's algorithm

"""
This assumes that graph structure is represented as a dictionary of dictionaries

graph = {
    'current node': {'neighbour node': 'weight', 'neighbour node 2': 'weight 2'},
}
"""

def MST(graph, start):
    """
    This function takes in a graph object and a starting vertex.

    Using the starting vertex, this function iteratively find the next available noed with the smallest edge weight.
    If a node has already been visited, it will not be visited again to prevent a cycle from occuring.
    """

    result = [] # stores the edges of the MST
    visited = set() # stores visited nodes in a set to prevent a cycle from occuring
    visited.add(start) # add the starting node to the visited set

    queue = [] # queues up available nodes to be visited and sorts in ascending order
    for start, neigbour in graph.items():
        for node, weight in neigbour.items():
            queue.append((start, node, weight))
    queue.sort(key=lambda x: x[2]) # sort the queue in ascending order

    while queue:
        for start, adjacent, weight in queue:
            # if start node is in visited and adjacent node is not in visited, add the edge to the result
            if start in visited and adjacent not in visited:
                result.append((start, adjacent, weight)) # add edges to result as a tuple
                visited.add(adjacent) # add adjacent node to visited set
                queue.remove((start, adjacent, weight)) # remove the edge from the queue
                break # break out of the for loop to prevent the queue from being iterated through again
            # remove edge from queue if start and adjacent nodes have been visited to break out of queue
            elif start in visited and adjacent in visited:
                queue.remove((start, adjacent, weight))
                break
    return result

