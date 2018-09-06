

def bfs(graph, m, n):
    processed = {m}
    queue = [(m, v) for v in graph[m]]
    path = []
    while len(queue) > 0:
        parent, child = queue.pop(0)
        path.append((parent, child))
        if child == n: 
            return True, path
        if child not in processed:
            queue += [(child, v) for v in graph[child]]
            processed.add(child)
    return False, {}


def djikstra(graph, m, n):
    costs = {}
    parent = {}

    # add every vertex to the graph 
    queue = set(list(graph.keys()))
    for nodes in graph.values():
        queue.update(nodes)

    queue = list(queue)
    # initialize all costs to inf except the starting point
    for node in queue:
        costs[node] = float("inf")

    # starting node is 0
    costs[m] = 0

    while len(queue) > 0:
        # find the min weight node -- should be the source m
        current_node = min(queue, key=lambda x: costs[x])
        queue.remove(current_node)

        for neighbor in graph[current_node].keys():
            current_dist = costs[current_node] + graph[current_node][neighbor]['weight']
            if current_dist < costs[neighbor]:
                costs[neighbor] = current_dist
                parent[current_node] = neighbor
    return costs, parent


if __name__ == "__main__": 
    graph = {
      "c": {
        "a": {
          "weight": 3
        },
        "e": {
          "weight": 9
        }
      },
      "a": {
        "b": {
          "weight": 10
        },
        "d": {
          "weight": 5
        }
      },
      "e": {
        "d": {
          "weight": 3
        }
      },
      "b": {
        "c": {
          "weight": 1
        }
      },
      "d": {}
    }
    print(djikstra(graph, "a", "e"))
