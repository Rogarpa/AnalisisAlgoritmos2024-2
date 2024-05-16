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
node = bilinked_list_node()
