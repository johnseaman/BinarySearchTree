class Node:
	def __init__(self,data):
		self.right = None
		self.left = None
		self.data = data

class BinaryTree:
	def __init__(self):
		self.root = None 
	def getRoot(self):
		return self.root
		
	def deleteTree(self):	
		self.root=None
		
	def isEmpty(self):
		if self.root is None:
			return None

	def addNode(self,data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._add(self.root,data)
		return self.root
	
	def _add(self,currentNode, data):
		if currentNode.data>data:
			if currentNode.left:
				self._add(currentNode.left,data)
			else:
				currentNode.left = Node(data)
		if currentNode.data<data:
			if currentNode.right:
				self._add(currentNode.right,data)
			else:
				currentNode.right = Node(data)
	
	def printTree(self):
		if self.root is None:
			print("Nothing to show")
		elif self.root is not None and self.root.left is None and self.root.right is None:
			print(self.root.data)
		else:
			self._printTree(self.root)

	def _printTree(self,currentNode):
		if currentNode is not None:
			self._printTree(currentNode.left)
			print(str(currentNode.data))
			self._printTree(currentNode.right)

	def findNode(self,data):
		if self.root is None:
			print("Tree empty")
		else:
			self._findNode(self.root,data)

	def _findNode(self,currentNode,data):
		if currentNode.data==data:
			print("Found")

		elif currentNode.data>data and currentNode.left!=None:
			print("searching-left")
			self._findNode(currentNode.left,data)
		elif currentNode.data<data  and currentNode.right:
			print("searching-right")
			self._findNode(currentNode.right,data)
		
	def findLeafCount(self):
		if self.root is None:
			print("No Nodes")
		elif self.root is not None and self.root.left is None and self.root.right is None:
			print("1")	
		else:
			self._findLeaves(self.root)
	
	def _findLeaves(self,currentNode):
		leftCount = 0 
		rightCount = 0 
		if currentNode.left is not None:
			self._findLeaves(currentNode.left)
		else:
			leftCount = leftCount+1
	
		if currentNode.right is not None:
			self._findLeaves(currentNode.right)
		else:
			rightCount = rightCount+1
		
		return int(leftCount+rightCount)

	def findHeight(self, root):
		total = 0
		leftHeight = 0 
		rightHeight = 0
		if root is None:
			return 
		if root is not None and root.left is None and root.right is None:
			total = 0 
		else:
			if root.left:
				leftHeight = self.findHeight(root.left)+1
			if root.right:
				rightHeight = self.findHeight(root.right)+1
			
			if leftHeight>rightHeight:
				total = leftHeight 
			elif leftHeight<rightHeight:
				total = rightHeight
			else:
				total = rightHeight

		return total
		
	def BreadthFirstTraversal(self, root):
		if self.root is None:
			return 
		nodes = []
		nodes.append(self.root)
		current = root 
		while(len(nodes)>0):
			print(nodes[0].data)
			node = nodes.pop(0)
			if node.left is not None:
				nodes.append(node.left)
			if node.right is not None:
				nodes.append(node.right)
	def preOrderTraversal(self,root):
		currentNode = root
		if currentNode is None:
			return 
		print(currentNode.data)
		self.preOrderTraversal(currentNode.left)
		self.preOrderTraversal(currentNode.right)

	def inOrderTraversal(self,root):
		currentNode = root 
		if currentNode is None:
			return 
		self.inOrderTraversal(currentNode.left)
		print(root.data)
		self.inOrderTraversal(currentNode.right)
	
	def postOrderTraversal(self,root):
		currentNode = root 
		if currentNode is None:
			return 
		self.postOrderTraversal(currentNode.left)
		self.postOrderTraversal(currentNode.right)
		print(root.data)
