# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
        else:
            ma = max(nums)
            index = nums.index(ma)
            root = TreeNode(ma)
            root.left = self.constructMaximumBinaryTree(nums[0: index])
            root.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return root
        
