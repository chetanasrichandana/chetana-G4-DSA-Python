class Node:
    def __init__(self, data):
        self.left: Node = None
        self.right: Node = None
        self.data: int = data

class BinaryTree:
    def __init__(self):
        self.root: Node = None
    
    def __str__(self):
        res = ''
        if self.root is None:
            return 'Binary Tree is Empty'
        else:
            queue = [self.root]
            while queue:
                current_node = queue.pop(0)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                res += str(current_node.data)
        return res

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if not current_node.left:
                current_node.left = node
                return
            else:
                queue.append(current_node.left)
            
            if not current_node.right:
                current_node.right = node
                return
            else:
                queue.append(current_node.right)


    def preorder_traversal(self): #Root -> Left -> Right
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, current_node: Node, result: list):
        if current_node:
            result.append(current_node.data)
            self._preorder_traversal(current_node.left, result)
            self._preorder_traversal(current_node.right, result)
        return result

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, current_node: Node, result: list):
        if current_node:
            self._inorder_traversal(current_node.left, result)
            result.append(current_node.data)
            self._inorder_traversal(current_node.right, result)
        return result

    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, current_node: Node, result: list):
        if current_node:
            self._postorder_traversal(current_node.left, result)
            self._postorder_traversal(current_node.right, result)
            result.append(current_node.data)
        return result

    def remove(self, data):
        if self.root is None:
            return None
        if (self.root.left is None) and (self.root.right is None):
            if self.root.data == data:
                self.root = None
            return None
        

        queue = [self.root]
        to_remove = None
        current_node = None

        while queue:
            current_node = queue.pop(0)

            if current_node.data == data:
                to_remove = current_node
                
            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
        if to_remove:
            deepest_node_value = current_node.data
            # current_node = None
            self._delete_deepest_node(current_node)
            to_remove.data = deepest_node_value
    
    def _delete_deepest_node(self, node : Node):
        queue = [self.root]

        while queue:
            temp = queue.pop(0)
            if temp is node:
                temp = None
                return
            
            if temp.left:
                if temp.left == node:
                    temp.left = None
                    return
                else:
                    queue.append(temp.left)
            
            if temp.right:
                if temp.right == node:
                    temp.right = None
                    return
                else:
                    queue.append(temp.right)
    def Leaf_nodes_printing(self):
        return self._Leaf_nodes_printing(self.root)
    
    def _Leaf_nodes_printing(self,curr_node: Node):
        if curr_node:
            Flag=self._Leaf_nodes_printing(curr_node.left)
            if Flag:   print(curr_node.data)
            Flag=False
            self._Leaf_nodes_printing(curr_node.right)
        else:
            return True        


if __name__ == '__main__':
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    print(tree)
    tree.Leaf_nodes_printing()


