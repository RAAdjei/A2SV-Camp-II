# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(curr_node):
            if not curr_node:
                return [0, 0] 

            if curr_node in memo:
                return memo[curr_node]

            right = dp(curr_node.right)
            left =  dp(curr_node.left)
            

            rob = curr_node.val + left[1] + right[1]
            not_rob = max(left) + max(right)

            memo[curr_node] = [rob, not_rob]

            return memo[curr_node]

        return max(dp(root))    
        
