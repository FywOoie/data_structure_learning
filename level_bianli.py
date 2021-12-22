import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_bianli(root):
    if not root:
        return []
    result, queue = [], collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
