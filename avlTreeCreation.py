class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0
        self.balanceFactor = 0 #height(right)-height(left)
class AvlTree:
    def __init__(self) :
        self.__root = None
        self.__nodescount=0
    def find(self, value):
        return self.__contains(self.__root, value)
    def __contains(self,root, value):
        if root is None:
            return False
        if(root.value==value):
            return True
        if(root.value<value):
            self.__contains(root.right, value)      
        else:
            self.__contains(root.left, value) 

    def insert(self, value):
        if value == None:
            return False
        if self.find(value):
            return False
        else:
            self.root = self.__insert(self.__root,value)
            self.__nodescount+=1
            return True

    def __insert(self, root, value):
        if root==None :
            return Node(value)
        if(root.value<value):
            root.right=self.__insert(root.right,value)
        else:
            root.left=self.__insert(root.left, value)
        self.__update(root)
        return self.__balance(root) 
    
    def __update(self,root):
        leftheight, rightheight=-1, -1
        if root.left != None:
            leftheight=root.left.height
        if root.right != None:
            rightheight=root.right.height
        root.height=1+max(leftheight, rightheight)
        root.balanceFactor=rightheight-leftheight

    def __balance(self, root):
        if(root.balancingFactor==2):
            if(root.right.balancingFactor>0):
                return self.__rightRightCase(root)
            else:
                return self.__rightLeftCase(root)
        elif(root.balancingFactor==-2):
            if(root.right.balancingFactor>0):
                return self.__leftRightCase(root)
            else:
                return self.__leftLeftCase(root)
    def __rightRightCase(self, root):
        return self.__rotateLeft(root)
    def __rightLeftCase(self, root):
        root.right=self.__rotateRight(root.right)
        return self.__rotateLeft(root)
    def __leftLeftCase(self, root):
        return self.__rotateRight(root)
    def __leftRightCase(self, root):
        root.left=self.__rotateLeft(root.left)
        return self.__rotateRight(root)

    def __rotateRight(self, root):
        temp=root.left.right
        root.left.right=root
        root.left=temp
        self.__update(root)
        self.__update(root.left)
        return root.left
    
    def __rotateLeft(self, root):
        temp=root.right.left
        root.right.left=root
        root.right=temp
        self.__update(root)
        self.__update(root.right)
        return root.right

    def remove(self, value):
        if value is None :
            return False
        
        if not self.find(value) :
            return False
        else :
            self.__root = self.__remove(self.__root, value)
            self.__nodesCount -= 1
            return True
        
    def __remove(self, node, value) :
        if node.value == value :
            if node.left is None and node.right is None :
                del node
                return None
            elif node.left is None :
                temp = node.right
                del node
                return temp
            elif node.right is None :
                temp = node.left
                del node
                return temp
            else :
                successor = node.left
                while(successor.right is not None) :
                    successor = successor.right
                
                node.value = successor.value
                node.left = self.__remove(node.left, successor.value)
                return node        
        elif value > node.value :
            node.right = self.__remove(node.right, value)
        else : 
            node.left = self.__remove(node.left, value)
        self.__update(node)
        return self.__balance(node)
    
    
        
    

        
                


        