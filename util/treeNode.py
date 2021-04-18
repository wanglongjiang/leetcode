from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# list数据按照bfs遍历得到
def fromList(li: List[int]):
    if len(li) == 0:
        return None
    root = TreeNode(val=li[0])
    queue = [root]
    i = 1
    while i < len(li):
        node = queue[0]
        del queue[0]
        if li[i] is not None:
            node.left = TreeNode(val=li[i])
            queue.append(node.left)
        i += 1
        if i < len(li):
            if li[i]:
                node.right = TreeNode(val=li[i])
                queue.append(node.right)
            i += 1
    return root


def toList(node: TreeNode):
    li = []
    if node is None:
        return li
    queue = [node]
    li.append(node.val)
    while len(queue) > 0:
        node = queue[0]
        del queue[0]
        if node.left:
            queue.append(node.left)
            li.append(node.left.val)
        else:
            li.append(None)
        if node.right:
            queue.append(node.right)
            li.append(node.right.val)
        else:
            li.append(None)

    # 删掉末尾的null
    i = len(li) - 1
    while i > 0:
        if li[i] is None:
            del li[i]
        else:
            break
        i -= 1
    return li


print(toList(fromList([5, 1, 4, None, None, 3, 6])))
