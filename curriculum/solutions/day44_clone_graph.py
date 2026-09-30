from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        clones = {node: Node(node.val)}  # original -> clone; doubles as visited
        stack = [node]
        while stack:
            current = stack.pop()
            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                clones[current].neighbors.append(clones[neighbor])
        return clones[node]
