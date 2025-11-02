def is_safe(graph, color, v, c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True
    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0
    return False

def solve_graph_coloring(graph, m):
    color = [0] * len(graph)
    if graph_coloring_util(graph, m, color, 0):
        return color
    else:
        return None

def display_result(color):
    if color is None:
        print("Solution does not exist")
    else:
        print("Assigned Colours to nodes:")
        for i, c in enumerate(color):
            print(f"Node {i}: Colour {c}")

graph1 = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0]
]
m1 = 3
print("Graph 1:")
coloring1 = solve_graph_coloring(graph1, m1)
display_result(coloring1)

graph2 = [
    [0,1,1,1,1],
    [1,0,1,1,1],
    [1,1,0,1,1],
    [1,1,1,0,1],
    [1,1,1,1,0]
]
m2 = 5
print("\nGraph 2:")
coloring2 = solve_graph_coloring(graph2, m2)
display_result(coloring2)
