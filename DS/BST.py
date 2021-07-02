class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    @staticmethod
    def insert(root, node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    Node.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    Node.insert(root.left, node)

                # A utility function to do inorder tree traversal

    @staticmethod
    def countNodes(node):
        root = node
        count = 1
        if root:
            if root.right:
                count += Node.countNodes(root.right)
            if root.left:
                count += Node.countNodes(root.left)
        return count

    @staticmethod
    def search(root, key):

        if root.val == key:
            return True
        else:
            if root.val < key:
                if root.right:
                    return Node.search(root.right, key)
                else:
                    return False

            elif root.val > key:
                if root.left:
                    return Node.search(root.left, key)
                else:
                    return False

    @staticmethod
    def inorder(root):
        if root:
            Node.inorder(root.left)
            print(root.val, end=' ')
            Node.inorder(root.right)

    @staticmethod
    def printPostorder(root):
        if root:
            Node.printPostorder(root.left)
            Node.printPostorder(root.right)
            print(root.val, end=' ')

    @staticmethod
    def printPreorder(root):
        if root:
            print(root.val, end=' ')
            Node.printPreorder(root.left)
            Node.printPreorder(root.right)


r = Node(50)
Node.insert(r, Node(30))
Node.insert(r, Node(20))
Node.insert(r, Node(40))
Node.insert(r, Node(70))
Node.insert(r, Node(60))
Node.insert(r, Node(80))
print(Node.countNodes(r))

# Print inoder traversal of the BST
# print(r.search(r, 60))
# r.inorder(r)
# print("\n")
# r.printPreorder(r)
# print("\n")
# r.printPostorder(r)
