class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

            # A utility function to do inorder tree traversal


def search(root, key):

    if root.val == key:
        return True
    else:
        if root.val < key:
            if root.right:
                return search(root.right, key)
            return False

        elif root.val > key:
            if root.left:
                return search(root.left, key)
            return False


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)


def printPreorder(root):
    if root:
        print(root.val, end=' ')
        printPreorder(root.left)
        printPreorder(root.right)


def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=' ')


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# Print inoder traversal of the BST
print(search(r, 65))
inorder(r)
print("\n")
printPreorder(r)
print("\n")
printPostorder(r)
