def has_euler_path_or_circuit(graph):
    odd_degree_count = sum(sum(row) % 2 != 0 for row in graph)

    # Check for Euler path or circuit
    if odd_degree_count == 0:
        print("The graph has an Euler circuit.")
        return True
    elif odd_degree_count == 2:
        print("The graph has an Euler path.")
        return True
    else:
        print("The graph does not have an Euler path or circuit.")
        return False

def fleury_algorithm(graph):
    start_vertex = 0
    for i in range(len(graph)):
        if sum(graph[i]) % 2 != 0:
            start_vertex = i
            break

    current_vertex = start_vertex
    circuit = [current_vertex]

    while any(graph[current_vertex]):
        for next_vertex in range(len(graph[current_vertex])):
            if graph[current_vertex][next_vertex] > 0:
                # Remove the edge from the graph
                graph[current_vertex][next_vertex] -= 1
                graph[next_vertex][current_vertex] -= 1

                # Move to the next vertex
                current_vertex = next_vertex
                circuit.append(current_vertex)
                break

    return circuit

def euler(matrix):
    if has_euler_path_or_circuit(matrix):
        euler_circuit = fleury_algorithm(matrix)
        print("Euler Circuit:", euler_circuit)




example_matrix = [
    [0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0]
]

# Find and print the Euler circuit
euler(example_matrix)