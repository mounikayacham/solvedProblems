class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a value
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    # Search a value
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    # Delete a value
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Inorder Traversal (Left → Root → Right)
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.val, end=" ")
            self._inorder(node.right)

    # Preorder Traversal (Root → Left → Right)
    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self, node):
        if node:
            print(node.val, end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

    # Postorder Traversal (Left → Right → Root)
    def postorder(self):
        self._postorder(self.root)
        print()

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val, end=" ")

    # Level-order Traversal (BFS)
    def level_order(self):
        if not self.root:
            return
        from collections import deque
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.val, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()
bst = BST()

# Insert values
for val in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(val)

# Traversals
bst.inorder()      # 3 5 7 10 12 15 18
bst.preorder()     # 10 5 3 7 15 12 18
bst.postorder()    # 3 7 5 12 18 15 10
bst.level_order()  # 10 5 15 3 7 12 18

# Search
print(bst.search(7))  # <__main__.BSTNode object ...>
print(bst.search(10)) # None

# Delete
bst.delete(15)
bst.inorder()
    

