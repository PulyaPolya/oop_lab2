# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node


class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print (root.key,end=" ")
		inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node


def minValueNode(node):
	current = node

	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left

	return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root
def find_g(root, lkpval, res):
    #res=[]
    if root != None:
        if root.key > lkpval:

            res.append(root.key)
            find_g(root.left, lkpval, res)
        find_g(root.right, lkpval, res)
    res.sort()
def find(root, lkpval, res):
    if lkpval < root.key:
        if root.left is None:
            return str(lkpval) + " Not Found"
        find(root.left, lkpval, res)
    elif lkpval > root.key:
        if root.right is None:
            return str(lkpval) + " Not Found"
        find(root.right, lkpval, res)
    else:
     res.append(root.key)




def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# If the key to be deleted
	# is smaller than the root's
	# key then it lies in left subtree
	if key < root.key:
		root.left = deleteNode(root.left, key)

	# If the kye to be delete
	# is greater than the root's key
	# then it lies in right subtree
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	# If key is same as root's key, then this is the node
	# to be deleted
	else:

		# Node with only one child or no child
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# Node with two children:
		# Get the inorder successor
		# (smallest in the right subtree)
		temp = minValueNode(root.right)

		# Copy the inorder successor's
		# content to this node
		root.key = temp.key

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.key)

	return root

'''
root = None
root = insert(root, 'aaaaa')
root = insert(root, 'bbb')
root = insert(root, 'ccc')
root = insert(root, 'dddd')
root = insert(root, 'eeeee')
root = insert(root, 'ffff')
root = insert(root, 'ggggg')

print ("Inorder traversal of the given tree")
inorder(root)
print('fpunf ')
a=[]
#find_g(root, 50,a)
print(a)

print ("\nDelete aaa")
root = deleteNode(root, 'aaaaa')
print ("Inorder traversal of the modified tree")
inorder(root)
'''
'''
print ("\nDelete 30")
root = deleteNode(root, 30)
print ("Inorder traversal of the modified tree")
inorder(root)

print ("\nDelete 50")
root = deleteNode(root, 50)
print ("Inorder traversal of the modified tree")
inorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
'''