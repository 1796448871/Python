# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # Optional[TreeNode] 指的其可以是TreeNode也可以是None

        #注意判断初始root不能是 None
        if not root:
            return []
        res=[]
        que = deque([root])  # 使用 deque 初始化队列

        while que:
            temp =[]
            size = len(que) #这一层的数量
            for _ in range(size) :
                nowNode = que.popleft()  # 使用 popleft() 弹出队列的第一个元素
                temp.append(nowNode.val)
                if nowNode.left:
                    que.append(nowNode.left)
                if nowNode.right:
                    que.append(nowNode.right)
            res.append(temp)
            
        return res