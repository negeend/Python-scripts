class Node:
    def __init__(self, id, anime):
        self.id = id
        self.anime = anime
        self.left = None 
        self.right = None 

def DFS_recursive(node):
    print(node.anime)
    if node.left:
        DFS_recursive(node.left)
    if node.right:
        DFS_recursive(node.right)

def DFS_iterative(node):
    nodes_list = [node]
    while True:
        if len(nodes_list) == 0:
            break
        x = len(nodes_list)-1
        node = nodes_list[x]
        nodes_list.remove(node)
        print(node.anime)
        if node.right:
            nodes_list.append(node.right)
        if node.left:
            nodes_list.append(node.left)


root = Node(1, "Code Geass")
# Link up the nodes
root.left = Node(2, "Steins Gate")
root.right = Node(3, "Kimi no na wa")
root.left.left = Node(4, "Death Note")
root.left.right = Node(5, "Naruto")
root.right.left = Node(6, "One Piece")
root.right.right = Node(7, "Shingeki no Kyojin")

DFS_iterative(root)