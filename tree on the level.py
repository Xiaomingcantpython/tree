class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def bfs(root):
    if not root:return
    queue=[root]
    res=[]

    while queue:
        node=queue.pop(0)
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return res

while True:
    try:
        ans=True
        stop=False
        nodes=[]
        s=set()
        while True:
            if stop:break
            for i in input().split():
                if i=='()':
                    stop=True
                    break
                val,path=i[1:-1].split(',')
                if path not in s:
                    nodes.append((val,path))
                    s.add(path)
                else:
                    ans=False

        count=1
        nodes.sort(key=lambda x:len(x[1]))
        val,path=nodes.pop(0)

        if path!='' or not ans:
            print('not complete')
        else:
            tree=Tree(val)
            for val,path in nodes:
                node=tree
                for p in range(len(path)):
                    if path[p]=='L':
                        if not node.left and p==len(path)-1:
                            node.left=Tree(val)
                        elif node.left:
                            node=node.left
                        else:
                            ans=False
                            break
                    else:
                        if not node.right and p==len(path)-1:
                            node.right=Tree(val)
                        elif node.right:
                            node=node.right
                        else:
                            ans=False
                            break
                count+=1
            if ans:
                res=bfs(tree)
                if len(res)==count:
                    print(' '.join(res))
                else:
                    print('not complete')
            else:
                print('not complete')
    except:
        break