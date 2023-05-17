from graph import create_cluster_graph
from node import Node
import math

BS = Node(0, 0, x=0, y=0)

def Edist(node1, node2):
    # Calculate Euclidean distance between two nodes
    x1, y1 = node1.x, node1.y  # Assuming x and y coordinates are attributes of the nodes
    x2, y2 = node2.x, node2.y

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def cluster_head_selection(n, S, max_heads):
    # Sort nodes based on energy level in ascending order
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if S[j].energy < S[min_index].energy:
                min_index = j
        S[i], S[min_index] = S[min_index], S[i]

    # Calculate distances from nodes to the base station
    for i in range(n):
        S[i].distBs = Edist(BS, S[i])

    # Sort nodes based on distance to the base station in ascending order
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if S[j].distBs < S[min_index].distBs:
                min_index = j
        S[i], S[min_index] = S[min_index], S[i]

    # Select cluster heads
    head_count = 0
    for i in range(n):
        if head_count < max_heads:
            if not S[i].head and not S[i].member:
                S[i].head = True
                head_count += 1
                for j in range(i + 1, n):
                    if S[i].area > Edist(S[i], S[j]):
                        print(i,j)
                        S[i].members.append(S[j])
                        S[j].member = True
        else:
            break

    # Create a list of selected cluster heads
    CHs = [node for node in S if node.head]
    print("______")
    print(list(map(str, S[4].members)))
    print("______")

    return CHs


def main() :
    global BS
    S = [
        Node(5, 0, x=1, y=2),
        Node(8, 0, x=3, y=4),
        Node(3, 0, x=5, y=6),
        Node(10, 0, x=7, y=8),
        Node(6, 0, x=9, y=10),
        Node(4, 0, x=11, y=12)
    ]
    NUM_HEADS = 2
    _range = len(S)

    heads = cluster_head_selection(_range, S, NUM_HEADS)
    print(*heads, sep="\n")
    create_cluster_graph(S, heads)
    run_topology(S, heads)

if __name__ == "__main__":
    main()
