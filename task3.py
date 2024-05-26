from collections import defaultdict
from heapq import *


def dijkstra(graph, start, target):
    distances = defaultdict(list)

    for from_, to, weight in graph:
        distances[from_].append((weight, to))

    heap_tree, seen, mins = [(0, start, ())], set(), {start: 0}

    def unpack(p, unpacked=None):
        unpacked = unpacked or []

        [unpack(i, unpacked) if isinstance(i, tuple) else unpacked.append(i) for i in p]
        return list(reversed(unpacked))

    while heap_tree:
        weight, to, path = heappop(heap_tree)

        if to not in seen:
            seen.add(to)
            path = (to, path)

            if to == target:
                return weight, unpack(path)

            for _w, _t in distances.get(to, ()):
                if _t in seen:
                    continue
                prev = mins.get(_t, None)
                next = weight + _w
                if prev is None or next < prev:
                    mins[_t] = next
                    heappush(heap_tree, (next, _t, path))

    return float("inf"), None


if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    nodes = set()
    [(nodes.add(edge[0]), nodes.add(edge[1])) for edge in edges]

    for node in sorted(nodes)[1:]:
        distance, path = dijkstra(edges, 'A', node)

        print(f'A -> {node}')
        print(f'Distance: {distance}')
        print(f'Path: {path}', end='\n\n')

# A -> B
# Distance: 7
# Path: ['A', 'B']
#
# A -> C
# Distance: 15
# Path: ['A', 'B', 'C']
#
# A -> D
# Distance: 5
# Path: ['A', 'D']
#
# A -> E
# Distance: 14
# Path: ['A', 'B', 'E']
#
# A -> F
# Distance: 11
# Path: ['A', 'D', 'F']
#
# A -> G
# Distance: 22
# Path: ['A', 'D', 'F', 'G']
