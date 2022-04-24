# constructs a graph of all node from 0 to the length of U
# adds directed edges from i to j in U[i][j]
# Returns dictionary equivalent to the graph
def construct_graph(u):
    graph = {0: []}
    for i in range(len(u)):
        ui = []
        for j in range(len(u[i])):
            ui.append(u[i][j])
        graph[i + 1] = ui
    return graph


# Return dictionary of the parents nodes that can be use to find the shortest path from the last node to any other node
def bfs(graph):
    queue = [len(graph) - 1]
    path_dict = dict.fromkeys([i for i in range(len(graph) - 1, -1, -1)])
    while queue:
        s = queue.pop(0)
        for destination in graph[s]:
            if path_dict[destination] is None:
                path_dict[destination] = s
                queue.append(destination)
    return path_dict


# Returns path from node a to b or None if there is no path
def point_to_point(a, b, path_dic):
    if a == b:
        return [str(b)]
    else:
        x = min(a, b)
        y = max(a, b)
        path = [x]
        while path_dic[x] is not None and x != y:
            path.insert(0, path_dic[x])
            x = path_dic[x]
        if x == y:
            return path
        else:
            return None
