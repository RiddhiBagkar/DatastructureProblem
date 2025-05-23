class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    
def insert_bst(root,value):
        if root is None:
            return TreeNode(value)
        
        if value < root.value:
            root.left = insert_bst(root.left,value)
        
        elif value > root.value:
            root.right = insert_bst(root.right,value)

        return root


def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def delete_root(root, key):
    if root is None:
        return root

    if key < root.value:
        root.left = delete_root(root.left, key)
    elif key > root.value:
        root.right = delete_root(root.right, key)
    else:
        # Node to delete found
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = find_min(root.left)
        root.value = temp.value
        root.right = delete_root(root.right, temp.value)

    return root

def search_bst(root, key):
    if root is None:
        return False  # Not found
    
    if root.value == key:
        return True   # Found
    
    elif key < root.value:
        return search_bst(root.left, key)
    
    else:
        return search_bst(root.right, key)


def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        
        print('    ' * level + f'-> {root.value}')
        
        print_tree(root.left, level + 1)


def inorder_trave(root):
    if root is not None:
        inorder_trave(root.left)
        
        print(root.value, end=" ")
        
        inorder_trave(root.right)



def preorder(root):
    if root is not None:
        print(root.value, end=' ')  
        
        preorder(root.left)         
        
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)       
        
        postorder(root.right)
        
        print(root.value, end=' ')


def bfs(root):
    if root is None:
        return

    queue = deque()       
    queue.append(root)    
    while queue:          
        node = queue.popleft()         
        print(node.value, end=" ")     

        if node.left:
            queue.append(node.left)   
        if node.right:
            queue.append(node.right) 

Value=[8,5,10,4,6,9,11] 
root=None

for value in Value:
    root= insert_bst(root,value)


insert_bst(root,7)
print_tree(root)
print("\n")

print("inorder traversal")
inorder_trave(root)
print("\n")

print("\nPreorder traversal")
preorder(root )
print("\n")

print(" \nPostorder traversal")
postorder(root)

print("\n")

print(search_bst(root,6))


# delete(root,4)
