class TreeNode:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):

        if self.value is None:
            self.value = value
            return

        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True


###############################################################

    def isBalanced(self, root):
        def dfs(root):
            if not root:
                print("Reached a leaf node, returning [True, 0]")
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            print(
                f"Node ({root.value}): BALANCED?\tleft[0]={left[0]}, \tright[0]={right[0]}")
            print(
                f"Node ({root.value}): HEIGHT?\tleft[1]= {left[1]}, \tright[1]={right[1]}")
            print(f"Node ({root.value}): balanced = {balanced}")
            print()

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
###############################################################

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.value, end='  ')
        if self.right:
            self.right.inOrderTraversal()

    def preOrderTraversal(self):
        print(self.value, end='  ')
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()

    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.value, end='  ')

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


tree = TreeNode()
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(1)
tree.insert(3)
tree.insert(6)
tree.insert(9)

print("\n(A) Print Tree")
tree.display()

# print("\nInorder Traversal")
# tree.inOrderTraversal()
# print("\nPreOrder Traversal")
# tree.preOrderTraversal()
# print("\nPostOrder Traversal")
# tree.postOrderTraversal()

print(f"RESULT: Is the tree balanced? {tree.isBalanced(tree)}")
print("-----------------------------------")

tree2 = TreeNode()
tree2.insert(50)
tree2.insert(60)
tree2.insert(40)
tree2.insert(30)
tree2.insert(45)
tree2.insert(10)

print("\n(B) Print Tree")
tree2.display()

print(f"RESULT: Is the tree balanced? {tree2.isBalanced(tree2)}")
print("-----------------------------------")

print("\n")
