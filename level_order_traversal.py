class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def height(node):
    print("Inside the height function")
    if node is None:
        print("Condition when the node is None")
        return 0
    else:
        print("Going to find the height of the subtree")
        lheight = height(node=node.left)
        print("The left height of the node is ",lheight)
        rheight = height(node=node.right)
        print("The right height of the node is ",rheight)
        if lheight > rheight:
            print("The condition when lheight>rheight")
            return lheight + 1
        else:
            print("The condition when rheight>lheight")
            return rheight + 1


def printGivenLevel(root, level):
    print("Inside the printGivenlevel function")
    if root is None:
        print("The root value is None just take a return")
        return
    if level == 1:
        print("The value of level ==1 means root level")
        print(root.data, end=" ")

    elif level > 1:
        print("The value of level is ",level)
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def printLevelOrder(root):
    print("Call to the printLevelOrder Function")
    # to figure out the height of the root
    print("The height function being called ")
    h = height(root)
    print("The value of height is ",h)
    for i in range(1, h + 1):
        printGivenLevel(root, i)



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

printLevelOrder(root)

