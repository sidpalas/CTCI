from Graph import *
from collections import deque

def doesPathExist(graph, nodeA, nodeB):
    queueA = deque(nodeA.children)
    searchAVisited = dict()
    searchAVisited[nodeA.name] = True
    queueB = deque(nodeB.children)
    searchBVisited = dict()
    searchBVisited[nodeB.name] = True
    while len(queueA) > 0 or len(queueB) > 0:
        if len(queueA)>0:
            nextNode = graph.nodes[queueA.popleft()]
            searchAVisited[nextNode.name] = True
            if nextNode.name == nodeB.name:
                return True
            else:
                for node in nextNode.children:
                    if not node in searchAVisited:
                        queueA.append(node)
        if len(queueB)>0:
            nextNode = graph.nodes[queueB.popleft()]
            searchBVisited[nextNode.name] = True
            if nextNode.name == nodeA.name:
                return True
            else:
                for node in nextNode.children:
                    if not node in searchBVisited:
                        queueB.append(node)
    return False

testGraph = Graph()
testGraph.nodes.append(Node(0,[1]))
testGraph.nodes.append(Node(1,[]))
testGraph.nodes.append(Node(2,[0,3]))
testGraph.nodes.append(Node(3,[2]))
testGraph.nodes.append(Node(4,[6]))
testGraph.nodes.append(Node(5,[4]))
testGraph.nodes.append(Node(6,[5]))

nodeA = Node(2,[0,3])
nodeB = Node(1,[])
nodeC = Node(6,[5])

print doesPathExist(testGraph,nodeA,nodeB)

print doesPathExist(testGraph,nodeA,nodeC)
