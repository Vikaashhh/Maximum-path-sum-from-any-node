'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        # Yeh variable globally sabse bada path sum store karega
        self.max_sum = float('-inf')
        
        def helper(node):
            if not node:
                return 0  # Agar node None ho toh 0 return karo
            
            # Left aur Right ka max contribution calculate karo
            left = max(0, helper(node.left))   # Agar negative hai toh ignore karo
            right = max(0, helper(node.right))

            # Current node ko root maan ke max path ka sum nikalo
            current_path_sum = node.data + left + right

            # Global max update karo agar naya path zyada hai
            self.max_sum = max(self.max_sum, current_path_sum)

            # Parent ko sirf ek hi path de sakte hain (ya left ya right)
            return node.data + max(left, right)
        
        helper(root)
        return self.max_sum
