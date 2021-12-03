class node:
    def __init__(self,value):
        self.value = value
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self,node_list):
        self.root = node(node_list[0])
        for value in node_list[1:]:
            self.insert(value)
    def search(self,node,parent,value):#搜索树中有没有这个值
        if node == None:#如果结点本身是空或者已经搜索到叶子结点
            return False,node,parent
        if node.value ==value:
            return True,node,parent
        if node.value > value:#二叉排序树，左子树都比根节点小
            return self.search(node.lchild,node,value)#就以该节点为父亲了
        else:
            return self.search(node.rchild,node,value)
    def insert(self,value):
        flag,n,p = self.search(self.root,self.root,value)#遍历整个树，看看有没有value这个值
        if not flag:#flag为真，就不插入了，二叉排序树不能相同
            new_node=node(value)
            if value>p.value:#这时候，p已经是与value的值最接近的数，value这个节点，要不放在左边，要么放在右边
                p.rchild = new_node
            elif value<=p.value:
                p.lchild = new_node
    def delete(self,root,value):
        flag,n,p = self.search(self.root,self.root,value)#遍历整个树，看看有没有value这个值
        if flag is False:
            print("can not find the key!")
            return
        else:#注意，删除要分成3种情况，现在n就是我们要删除的节点
            if n.lchild is None:
                if n==p.lchild:
                    p.lchild = n.rchild#让删除节点的右孩子变成父节点的左孩子，大小关系不变
                else:
                    p.rchild =n.rchild
                del n 
                return
            elif n.rchild is None:
                if n==p.lchild:
                    p.lchild = n.lchild#让删除节点的右孩子变成父节点的左孩子，大小关系不变
                else:
                    p.rchild =n.lchild
                del n
                return
            else:#n有左右两个孩子
                pre = n.rchild
                if pre.lchild is None:
                    n.value = pre.value
                    n.rchild = pre.rchild
                    del pre#因为这说明了pre是比n大的最小的数
                    return
                else:
                    next = pre.lchild
                    while next.lchild is not None:
                        pre = next
                        next = next.lchild
                    n.value = next.value#一直沿着最左边到达底部，找到n的右子树中比n大的最小的数
                    pre.lchild = next.rchild
                    delete(self,next,next.value)
    def pre_order_traverse(self,node):
        if node is not None:
            print(node.value,end=' ')
            self.pre_order_traverse(node.lchild)
            self.pre_order_traverse(node.rchild)
    def in_order_traverse(self, node):#二元搜索树可以用中序遍历进行排序
        if node is not None:
            self.in_order_traverse(node.lchild)
            print(node.value,end=' ')
            self.in_order_traverse(node.rchild)

    # 后序遍历
    def post_order_traverse(self, node):
        if node is not None:
            self.post_order_traverse(node.lchild)
            self.post_order_traverse(node.rchild)
            print(node.value)

array = [6,2,4,10,23,45,67,1,9,10,13,12,18]

bst = BST(array)

bst.in_order_traverse(bst.root)
print("\n")
bst.delete(3,9)
bst.in_order_traverse(bst.root)