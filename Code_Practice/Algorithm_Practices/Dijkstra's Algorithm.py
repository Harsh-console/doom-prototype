inf = 10000
source_key = 0
destination_key = 1

# Format: node: [(edges), current_estimate, parent, explored]
MAP = {
    0: [((2, 3), (5, 2)), inf, None, False],         # A
    1: [((3, 1), (4, 2), (6, 2)), inf, None, False], # B
    2: [((0, 3), (4, 1)), inf, None, False],       # C
    3: [((1, 1), (2, 4)), inf, None, False],       # D
    4: [((1, 2), (2, 1), (5, 3), (6, 6)), inf, None, False], # E
    5: [((0, 2), (4, 3), (6, 5)), inf, None, False], # F
    6: [((1, 2), (4, 6), (5, 5)), inf, None, False], # G
}
MAP[source_key][1] = 0
def update_estimates(key):
    connected_nodes_tuple = MAP[key][0]
    current_estimate = MAP[key][1]
    for node in connected_nodes_tuple:
        key_node = node[0]
        edge_weight = node[1]
        new_estimate = current_estimate + edge_weight
        if new_estimate < MAP[key_node][1]:
            MAP[key_node][1] = new_estimate
            MAP[key_node][2] = key  # set parent to reconstruct path

def least_value_connected_unexplored_node(_, start):
    if start:
        return source_key  # Delay marking as explored until main loop

    least_estimate = inf
    req_node = None
    for key in MAP:
        if not MAP[key][3] and MAP[key][1] < least_estimate:
            req_node = key
            least_estimate = MAP[key][1]
    return req_node

# Main Dijkstra loop
present_key = least_value_connected_unexplored_node(None, True)

while True:
    update_estimates(present_key)
    if present_key is None:
        print("No path found to destination.")
        break
    MAP[present_key][3] = True  # Mark as explored after updating estimates

    if MAP[destination_key][3]:  # Destination reached
        break

    present_key = least_value_connected_unexplored_node(present_key, False)
    
# Output shortest path and cost
if MAP[destination_key][1] < inf:
    print("Shortest distance to destination:", MAP[destination_key][1])

    # Reconstruct path
    path = []
    node = destination_key
    while node is not None:
        path.append(node)
        node = MAP[node][2]
    path.reverse()
    print("Path:", path)
else:
    print("No reachable path.")
