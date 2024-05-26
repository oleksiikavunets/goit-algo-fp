import uuid
from collections import deque

import matplotlib.colors
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left = x - 1 / 2 ** layer
            pos[node.left.id] = (left, y - 1)
            add_edges(graph, node.left, pos, x=left, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right = x + 1 / 2 ** layer
            pos[node.right.id] = (right, y - 1)
            add_edges(graph, node.right, pos, x=right, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)

    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

    plt.show()


def build_tree(color):
    root = Node(0, color=color)
    root.left = Node(4, color=color)
    root.left.left = Node(5, color=color)
    root.left.right = Node(10, color=color)
    root.right = Node(1, color=color)
    root.right.left = Node(3, color=color)
    root.right.right = Node(11, color=color)
    return root


def bfs_recursive(node: Node, queue=None, visited=None):
    if visited is None:
        visited = set()

    if queue is None:
        queue = deque([node])

    if not node or not queue:
        return

    vertex = queue.popleft()

    if vertex not in visited:
        visited.add(vertex)

        grade = (len(visited) + 1) * 0.07
        r, g, b = matplotlib.colors.to_rgb(vertex.color)
        r, g, b = r + grade, g + grade, b + grade
        vertex.color = matplotlib.colors.to_hex((r, g, b))

        add_nodes = set()

        if vertex.left:
            add_nodes.add(vertex.left)

        if vertex.right:
            add_nodes.add(vertex.right)

        queue.extend(add_nodes - visited)

        bfs_recursive(vertex.left, queue, visited)
        bfs_recursive(vertex.right, queue, visited)


def dfs_recursive(vertex, visited=None):
    if vertex is None:
        return
    if visited is None:
        visited = set()
    visited.add(vertex)
    grade = (len(visited) + 1) * 0.07
    r, g, b = matplotlib.colors.to_rgb(vertex.color)
    r, g, b = r + grade, g + grade, b + grade
    vertex.color = matplotlib.colors.to_hex((r, g, b))
    for neighbor in (vertex.left, vertex.right):
        if neighbor not in visited:
            dfs_recursive(neighbor, visited)


tree = build_tree('#556655')

draw_tree(tree, 'Tree')
bfs_recursive(tree)
draw_tree(tree, 'BFS')

tree = build_tree('#556655')
dfs_recursive(tree)
draw_tree(tree, 'DFS')
