#!/usr/bin/env python

class Tree:
	def __init__(self):
		self.node = None

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def print_node(tree, node):
	if tree.node:
		print_node(tree.node)
	if node:
		if node.left:
			print_node(tree, node.left)
		print(node.value + "\n")
		if node.right:
			print_node(tree, node.right)

def insert(tree, node, value):
	if tree.node is None:
		tree.node = Node.Node(value)
		return
	else:
		if value < node.value:
			if node.left:
				insert(tree, node.left, value)
			else:
				node.left = Node.Node(value)
		elif value > node.value:
			if node.right:
				insert(tree, node.right, value)
			else:
				node.right = Node.Node(value)

def collect_input(tree):
	while 1:
		value = input("Enter your input: ")
		insert(tree, None, value)
		print_node(tree, None)
		collect_input(tree)

if __name__ == "__main__":
	tree = Tree.Tree()
	collect_input(tree)