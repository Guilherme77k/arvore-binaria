class newNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree():
    root = newNode(5)
    root.left = newNode(2)
    root.right = newNode(6)
    root.left.left = newNode(1)
    root.left.right = newNode(4)
    root.left.right.left = newNode(3)
    root.right.right = newNode(8)
    root.right.right.right = newNode(9)
    root.right.right.left = newNode(7)
    return root

def sum_odd_level_nodes(root, level=1):
    if not root:
        return 0
    if level % 2 == 1:
        return root.value + sum_odd_level_nodes(root.left, level + 1) + sum_odd_level_nodes(root.right, level + 1)
    return sum_odd_level_nodes(root.left, level + 1) + sum_odd_level_nodes(root.right, level + 1)

if __name__ == "__main__":
    tree_root = create_tree()
    result = sum_odd_level_nodes(tree_root)
    print(f"Soma dos nós nos níveis ímpares: {result}")

def tree_size(root):
    if not root:
        return 0

    queue = [root]
    count = 0

    while queue:
        current_node = queue.pop(0)
        count += 1

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return count

if __name__ == "__main__":
    root = newNode(5)
    root.left = newNode(2)
    root.right = newNode(6)
    root.left.left = newNode(1)
    root.left.right = newNode(4)
    root.left.right.left = newNode(3)
    root.right.right = newNode(8)
    root.right.right.right = newNode(9)
    root.right.right.left = newNode(7)

    print(f"Tamanho da árvore: {tree_size(root)}")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def in_order_traversal(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.value, end=" ")
        current = current.right

root = newNode(5)
root.left = newNode(2)
root.right = newNode(6)
root.left.left = newNode(1)
root.left.right = newNode(4)
root.left.right.left = newNode(3)
root.right.right = newNode(8)
root.right.right.right = newNode(9)
root.right.right.left = newNode(7)

print("Em-ordem:")
in_order_traversal(root)


def post_order_traversal(root):
    stack = []
    result = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            result.insert(0, current.value)
            current = current.right

        current = stack.pop()
        current = current.left

    for value in result:
        print(value, end=" ")

root = newNode(5)
root.left = newNode(2)
root.right = newNode(6)
root.left.left = newNode(1)
root.left.right = newNode(4)
root.left.right.left = newNode(3)
root.right.right = newNode(8)
root.right.right.right = newNode(9)
root.right.right.left = newNode(7)

print("\nPós-ordem:")
post_order_traversal(root)

def pre_order_traversal(root):
    stack = [root]

    while stack:
        current = stack.pop()
        print(current.value, end=" ")

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

root = newNode(5)
root.left = newNode(2)
root.right = newNode(6)
root.left.left = newNode(1)
root.left.right = newNode(4)
root.left.right.left = newNode(3)
root.right.right = newNode(8)
root.right.right.right = newNode(9)
root.right.right.left = newNode(7)

print("\nPré-ordem:")
pre_order_traversal(root)
print()

class nivel:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root = newNode(5)
root.left = newNode(2)
root.right = newNode(6)
root.left.left = newNode(1)
root.left.right = newNode(4)
root.left.right.left = newNode(3)
root.right.right = newNode(8)
root.right.right.right = newNode(9)
root.right.right.left = newNode(7)

print("Percurso em nível:")
level_order_traversal(root)
print()

class verifica:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_strict_binary_tree(root):
    if not root:
        return True

    if not root.left and not root.right:
        return True

    if root.left and root.right:
        return is_strict_binary_tree(root.left) and is_strict_binary_tree(root.right)

    return False

root = newNode(5)
root.left = newNode(2)
root.right = newNode(6)
root.left.left = newNode(1)
root.left.right = newNode(4)
root.left.right.left = newNode(3)
root.right.right = newNode(8)
root.right.right.right = newNode(9)
root.right.right.left = newNode(7)

result = is_strict_binary_tree(root)
if result:
    print("A árvore é estritamente binária.")
else:
    print("A árvore não é estritamente binária.")