import sys


class TreeNode:
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None
    
def insert(root,val):
    if not root.val:
        root.val=val
        return
    
    queue=[root]

    while queue:
        node=queue.pop(0)

        if not node.left:
            node.left=TreeNode(val)
            break
        else:
            queue.append(node.left)
        if not node.right:
            node.right=TreeNode(val)
            break
        else:
            queue.append(node.right)

def dfs(root,path):
    if root.val=='null':return

    if (not root.left or root.left.val=='null') and (not root.right or root.right.val=='null'):
        path+=[root.val]
        res.append('->'.join(path))
        return
    if root.left:dfs(root.left,path+[root.val])
    if root.right:dfs(root.right,path+[root.val])

def Input():
    return sys.stdin.readline().rstrip()

l=Input().split(',')
tree=TreeNode(l[0])

for i in l[1:]:
    if i=='null':
        insert(tree,'null')
    else:
        insert(tree,i)

res=[]
dfs(tree,[])

for i in res:
    print(i)