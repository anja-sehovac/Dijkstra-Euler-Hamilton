def dijkstra(graph, start_node):
    # Get the number of nodes in the graph
    num_nodes = len(graph)

    # Initialize distances, predecessors, and last_visited
    distances = [float('infinity')] * num_nodes
    predecessors = [None] * num_nodes
    last_visited = [None] * num_nodes

    distances[start_node] = 0
    last_visited[start_node] = start_node

    # List of unvisited nodes
    unvisited_nodes = list(range(num_nodes))

    while unvisited_nodes:
        # Find the node with the smallest distance value
        current_node = min(unvisited_nodes, key=lambda node: distances[node])

        # Remove the current node from the unvisited set
        unvisited_nodes.remove(current_node)

        # Update the distances, predecessors, and last_visited for neighboring nodes
        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0:
                potential_distance = distances[current_node] + graph[current_node][neighbor]
                if potential_distance < distances[neighbor]:
                    distances[neighbor] = potential_distance
                    predecessors[neighbor] = current_node
                    last_visited[neighbor] = current_node

    return distances, predecessors, last_visited


def get_shortest_path_in_letters(predecessors, last_visited, target):
    path = []
    current_node = target
    while current_node is not None:
        path.insert(0, chr(ord('A') + current_node))
        current_node = predecessors[current_node]
    return path, chr(ord('A') + last_visited[target])


def print_shortest_paths(graph_matrix, start_node_letter):
    start_node = ord(start_node_letter) - ord('A')  # Convert letter to index
    distances, predecessors, last_visited = dijkstra(graph_matrix, start_node)

    for node in range(len(graph_matrix)):
        path, last_node_visited = get_shortest_path_in_letters(predecessors, last_visited, node)
        print(
            f"Shortest path from {start_node_letter} to {chr(ord('A') + node)}: {path}, Distance: {distances[node]}, Last Node Visited: {last_node_visited}")


# Example usage with a graph represented as an adjacency matrix
graph_matrix_example = [
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
]

start_node_example = 'A'  # Corresponds to 'A'
print_shortest_paths(graph_matrix_example, start_node_example)

#Exampe 2
print_shortest_paths([
    [0, 1, 2, 0],
    [1, 0, 1, 3],
    [2, 1, 0, 0],
    [0, 3, 0, 0]
], 'A')