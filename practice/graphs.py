vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    ['A', 'B'],
    ['A', 'D'],
    ['B', 'C'],
    ['C', 'D'],
    ['C', 'E'],
    ['D', 'E']
]

def find_adjacent_nodes(node):
    
    adjacent_nodes = []

    for edge in edges:
        try:
            node_index = edge.index(node)
        except ValueError:
            node_index = None

        if node_index is not None:
            adjacent_node = edge[1] if node_index == 0 else edge[0]
            adjacent_nodes.append(adjacent_node)

    return adjacent_nodes

def is_connected(node1, node2):

    for edge in edges:
        try:
            node_index_1 = edge.index(node1)
        except ValueError:
            node_index_1 = None
        
        try:
            node_index_2 = edge.index(node2)
        except ValueError:
            node_index_2 = None
        
        if node_index_1 is not None and node_index_2 is not None:
            return True
    
    return False

print(find_adjacent_nodes('C'))

print(is_connected('A', 'E'))