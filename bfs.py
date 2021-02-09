class Node:
    def __init__(self, id, anime):
        self.id = id
        self.anime = anime
        self.left = None 
        self.right = None 

def BFS_iterative(node):
    nodes_list = [node]
    while True:
        if len(nodes_list) == 0:
            break
        node = nodes_list[0]
        nodes_list.remove(node)
        print(node.anime)
        if node.left:
            nodes_list.append(node.left)
        if node.right:
            nodes_list.append(node.right)

def BFS_recursive(node, visited):
    print(node.anime)
    
    neighbors = [node.left,node.right]
    
    if (neighbors == [None, None]):
        return
    
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.append (neighbor)
            print(neighbor.anime)
    for neighbor in neighbors:
        BFS_recursive(neighbor, visited)


root = Node(1, "Code Geass")
# Link up the nodes
root.left = Node(2, "Steins Gate")
root.right = Node(3, "Kimi no na wa")
root.left.left = Node(4, "Death Note")
root.left.right = Node(5, "Naruto")
root.right.left = Node(6, "One Piece")
root.right.right = Node(7, "Shingeki no Kyojin")

visited = []
BFS_iterative(root)
print()
BFS_recursive(root, visited)