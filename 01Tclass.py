import sys

sys.setrecursionlimit(10000)

class  Tree:
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
            node.left=Tree(val)
            break
        else:
            queue.append(node.left)
        if not node.right:
            node.right=Tree(val)
            break
        else:
            queue.append(node.right)


def dfs(root,path=[]):
    if root.val in ('0','-1'):return

    if not root.left and not root.right:
        path+=[root.val]
        res.append('->'.join(path))
        return
    
    if root.left:dfs(root.left,path+[root.val])
    if root.right:dfs(root.right,path+[root.val])

for l in sys.stdin:
    l=l.rstrip().split(',')

    tree=Tree(l[0])
    flag=True
    for i,j in enumerate(l[1:],1):
        if not j.isdigit():
            flag=False
            break
        if j=='null':
            insert(tree,'-1')
        elif tree.val=='0' and int(j) not in range(1,254):
            flag=False
            break
        
        elif  tree.val=='1' and int(j) not in range(2,255):
            flag=False
            break
        else:
            insert(tree,j)
    if flag:
        res=[]
        dfs(tree,[])
        for i in res:
            print(i)
