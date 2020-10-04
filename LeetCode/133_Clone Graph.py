"""
문제)
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


Test case format:

For simplicity sake, each node's value is the same as the node's index (1-indexed). For example, the first node with val = 1, the second node with val = 2, and so on. 
The graph is represented in the test case using an adjacency list.
Adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        graph = {node.val:Node(node.val, [])} #key: node의 값, value: Node객체(val = key, neighbors는 []로 초기화)
        que =deque()
        que.append(node) #que에는 탐색할 (주어진)node객체 넣어주기
        while que:
            cur_node = que.popleft()
            for n in cur_node.neighbors: #이웃한 노드들 모두 탐색
                if n.val not in graph:#방문한적없다면
                    tmp = Node(n.val, []) #새로운 node객체 생성
                    graph[n.val] = tmp #딕셔너리에 넣어주기
                    que.append(n)#que에 넣기
                graph[cur_node.val].neighbors.append(graph[n.val]) #이웃노드 넣어주기
        return graph[node.val]