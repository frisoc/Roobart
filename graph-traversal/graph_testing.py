def bfs_connected_component(graph, start):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


nodes = {1: [50, 30], 2: [100, 155], 3: [200, 155],
         4: [305, 110], 5: [110, 280], 6: [340, 275],
         7: [90, 430], 8: [230, 380], 9: [335, 475]}
