print("This program will print out a Hamiltonian cycle if one exists:")



def next_vertex(graph, current_index):
    while True:
        hamilton[current_index] = (hamilton[current_index] + 1) % (num_vertices + 1)
        if hamilton[current_index] == 0:
            return
        if current_index == 1:
            return
        previous_index = 0
        if graph[hamilton[current_index - 1]][hamilton[current_index]]:
            for i in range(1, current_index):
                previous_index = i
                if hamilton[i] == hamilton[current_index]:
                    break
            if previous_index == current_index - 1:
                if current_index < num_vertices or current_index == num_vertices:
                    if graph[hamilton[num_vertices]][hamilton[1]]:
                        return


def hamilton_circuit(graph, current_index):
    while True:
        next_vertex(graph, current_index)
        if hamilton[current_index] == 0:
            return
        if (current_index == num_vertices) and graph[hamilton[current_index]][hamilton[1]]:
            hamilton.append(hamilton[1])
            print(hamilton[1:])
            hamilton.pop()
        else:
            hamilton_circuit(graph, current_index + 1)



test = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

num_vertices = len(test) - 1
hamilton = [0 for _ in range(num_vertices + 1)]
is_criteria_checked = False


hamilton_circuit(test, 1)