class SortingAlgorithms:

    def LocalInsertionSort(self, array):
        
        return "LocalInsertionSort"

    def TreeSort(self, array):
        if (not hasattr(array, '__len__')):
            raise Exception("Input has no array behaviour")
        if (len(array) <= 0):
            return array

        root = tree_node(array[0])
        for element in array[1:]:
            root.insert(element)
        return root.inorderTraversal(root)

    def RadixLSDSort(self, array):
        print(array)

class bilinked_list_node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None

    def insert_before(self, data):
        node = bilinked_list_node(data)
        old_before = self.before
        self.before = node
        if(old_before != None):
            old_before.next = node
        node.before = old_before
        node.next = self

    def insert_after(self, data):
        node = bilinked_list_node(data)
        old_next = self.next
        self.next = node
        if(old_next != None):
            old_next.before = node
        node.before = self
        node.next = old_next
    
    def toArray(self, node):
        resultArray = []
        if(node == None):
            return resultArray
        if(node.data != None):
            resultArray.append(node.data)
        if(node.next != None):
            resultArray = resultArray + self.toArray(node.next)
        return resultArray

class tree_node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if (self.data == None):
            self.data = data
            return
        
        if data < self.data:
            if (self.left == None):
                self.left = tree_node(data)
            else:
                self.left.insert(data)
        elif (data > self.data):
            if (self.right == None):
                self.right = tree_node(data)
            else:
                self.right.insert(data)
    
    def inorderTraversal(self, root):
        res = []
        if (root == None):
            return res
        
        res = self.inorderTraversal(root.left)
        res.append(root.data)
        res = res + self.inorderTraversal(root.right)
        return res
    
# sorting = SortingAlgorithms()
# array = [3,2,1]
# array = []
# sorting.LocalInsertionSort(array)
# print(sorting.TreeSort(array))
# sorting.RadixLSDSort(array)
head = bilinked_list_node(1)
head.insert_after(5)
head.insert_after(4)
head.insert_after(3)
print(head.toArray(head))