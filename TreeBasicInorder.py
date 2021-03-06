# creating the class for Node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def printInorder(root):
    if root:
        printInorder(root=root.left)
        print(root.val,sep=" ")
        printInorder(root=root.right)
def printPreOrder(root):
    if root:
        print(root.val)
        printPreOrder(root.left)
        printPreOrder(root.right)


def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.val)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("The inorder traversal is ",printInorder(root=root))
print("The preorder traversal is ",printPreOrder(root=root))
print("The postorder traversal is ",printPostOrder(root=root))


