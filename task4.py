import heapq
import uuid

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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
root.right.right = Node(11)

# Відображення дерева
draw_tree(root)


def heapify_tree(root_node):
    heapified = []

    def _heapify(tree, node):
        if node:
            heapq.heappush(tree, node.val)
            _heapify(tree, node.right)
            _heapify(tree, node.left)

    _heapify(heapified, root_node)

    print(heapified)

    root = Node(heapified[0])

    def build_heap_tree(node, i):
        lindex, rindex = 2 * i + 1, 2 * i + 2

        if lindex < len(heapified):
            node.left = Node(heapified[lindex])
            build_heap_tree(node.left, lindex)

        if rindex < len(heapified):
            node.right = Node(heapified[rindex])
            build_heap_tree(node.right, rindex)

    build_heap_tree(root, 0)
    return root


heap_tree = heapify_tree(root)

draw_tree(heap_tree)
