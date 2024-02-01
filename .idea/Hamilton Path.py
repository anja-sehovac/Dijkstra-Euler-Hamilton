print("This program will print out a Hamiltonian path if one exists:")



def next_vertex(graph, current_index):
    while True:
        hamilton[current_index] = (hamilton[current_index] + 1) % (num_vertices + 1)
        if hamilton[current_index] == 0:
            return
        if graph[hamilton[current_index - 1]][hamilton[current_index]]:
            for i in range(1, current_index):
                if hamilton[i] == hamilton[current_index]:
                    break
            else:
                return


def hamilton_path(graph, current_index):
    while True:
        next_vertex(graph, current_index)
        if hamilton[current_index] == 0:
            return
        if current_index == num_vertices:
            # If all vertices are visited, print the Hamiltonian path
            if set(hamilton[1:]) == set(range(1, num_vertices + 1)):
                print(hamilton[1:])
        else:
            hamilton_path(graph, current_index + 1)





test = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0]
]

num_vertices = len(test) - 1
hamilton = [0 for _ in range(num_vertices + 1)]
is_criteria_checked = False


hamilton_path(test, 1)