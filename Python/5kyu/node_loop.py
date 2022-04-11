"""
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. Your objective is to determine the length of the loop.
"""


class Node:
    next = None


node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node2
node3.next = node4
node4.next = node2


def loop_size(node):
    node_list = []
    next_node = node
    while True:
        if next_node in node_list:
            return len(node_list) - node_list.index(next_node)
        else:
            node_list.append(next_node)
            next_node = next_node.next


print(loop_size(node1))
