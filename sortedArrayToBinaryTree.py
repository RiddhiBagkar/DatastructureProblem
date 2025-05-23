class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
            if nums:
                mid = len(nums) // 2
                root = TreeNode(nums[mid])
                root.left = self.sortedArrayToBST(nums[:mid])
                root.right = self.sortedArrayToBST(nums[mid+1:])
                return root
            else:
                return None
def inorder_trave(root):
    if root is not None:
        print(root.val, end=" ")
        inorder_trave(root.left)
        
        
        inorder_trave(root.right)


nums=[-3,-10,2,4,5]
sol = Solution()
root = sol.sortedArrayToBST(nums)
print(inorder_trave(root))