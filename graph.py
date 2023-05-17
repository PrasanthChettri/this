import networkx as nx
import matplotlib.pyplot as plt

def create_cluster_graph(S, CHs):
    G = nx.Graph()

    # Add nodes to the graph
    for node in S:
        G.add_node(node)

    # Add edges between cluster heads and their members
    for head in CHs:
        for member in head.members:
            G.add_edge(head, member)

    # Add edges between BS and CH nodes
    for head in CHs:
        G.add_edge("BS", head)

    # Create a layout for the graph
    pos = nx.spring_layout(G)

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, nodelist=S, node_color='blue', alpha=0.5)
    nx.draw_networkx_nodes(G, pos, nodelist=CHs, node_color='red')
    nx.draw_networkx_nodes(G, pos, nodelist=["BS"], node_color='green')

    # Draw edges
    nx.draw_networkx_edges(G, pos)

    # Draw labels (optional)
    nx.draw_networkx_labels(G, pos)

    # Show the graph
    plt.axis('off')
    plt.show()
