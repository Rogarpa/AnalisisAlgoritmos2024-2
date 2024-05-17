import numpy as np
class SortingAlgorithms:

    def LocalInsertionSort(self, array):
        print("====================")
        print("====================")
        print("====================")
        print("LOCAL INSERTION SORT ALGORITHM")
        if (not hasattr(array, '__len__')):
            raise Exception("Input has no array behaviour")
        if (len(array) <= 0):
            return array
        toInsertList = bilinked_list_node(array[0])
        lastInsertedNode = toInsertList
        for element in array[1:]:
            
            if(lastInsertedNode.data < element):
                lastInsertedNode = self.insert_right(element, lastInsertedNode)
            else:
                lastInsertedNode = self.insert_left(element, lastInsertedNode)
        
        head = self.getHead(toInsertList)
        return head.toArray(head)
    def getHead(self, node):
        head = node
        while(head.before != None):
            head = head.before
        return head
    def insert_left(self, data, node):
        
        if(node == None):
            return None
        left_node = node.before
        
        if(left_node == None):
            return node.insert_before(data)
        
        if(data >= left_node.data):
            return node.insert_before(data)
            
        
        return self.insert_left(data, left_node)
    def insert_right(self, data, node):
        
        if(node == None):
            return None
        right_node = node.next
        if(right_node == None):
            return node.insert_after(data)
        if(data <= right_node.data):
            return node.insert_after(data)
        return self.insert_right(data, right_node)
    def TreeSort(self, array):
        print("====================")
        print("====================")
        print("====================")
        print("TREE SORT ALGORITHM")
        if (not hasattr(array, '__len__')):
            raise Exception("Input has no array behaviour")
        if (len(array) <= 0):
            return array

        root = tree_node(array[0])
        for element in array[1:]:
            root.insert(element)
            print("element insertion = ", element)
            print(root.inorderTraversal(root), "\n")
        return root.inorderTraversal(root)

    def RadixLSDSort(self, array, digits_length):
        print("====================")
        print("====================")
        print("====================")
        print("RADIX LSD SORT ALGORITHM")
        digit_classes = []
        digit_classes_number = 35
        
        # Create digit_classes
        for i in range(digit_classes_number+1):
            digit_classes.insert(i, [])

        for element in array:
            digit_classes[self.getSymbolIndex(element[digits_length-1])].append(element)
        print("iteration = 0")
        print(digit_classes,"\n")

        i = digits_length-2
        while(i >= 0):
            print("iteration = ", i-(digits_length-3),"\n")
            print(digit_classes)
            for digit_class in digit_classes:
                if(digit_class == []):
                    continue
                class_elements_number = len(digit_class)
                
                while(class_elements_number > 0):
                    element = digit_class.pop(0)
                    class_elements_number -= 1
                    class_index = self.getSymbolIndex(element[i])
                    digit_classes[class_index].insert(len(digit_classes[class_index]), element)
            i -= 1
        print("iteration = ", digits_length,"\n")
        print(digit_classes)
        sorted_array = []
        for digit_class in digit_classes:
            sorted_array = sorted_array + digit_class
        return sorted_array
    def getSymbolIndex(self, symbol):
        max_ascii_letter = 122
        min_ascii_letter = 97
        max_ascii_number = 57
        min_ascii_number = 48
        ascii_number_padding = max_ascii_number - min_ascii_number

        ascii_code = ord(symbol)
        if(((ascii_code >= min_ascii_number) and (ascii_code <= max_ascii_number))):
            return (ascii_code - min_ascii_number)
        if(((ascii_code >= min_ascii_letter) and (ascii_code <= max_ascii_letter))):
            return ((ascii_code - min_ascii_letter)+1) + ascii_number_padding
        return -1
        
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
        return node

    def insert_after(self, data):
        node = bilinked_list_node(data)
        old_next = self.next
        self.next = node
        if(old_next != None):
            old_next.before = node
        node.before = self
        node.next = old_next
        return node
    
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
    
sorting = SortingAlgorithms()
array = [1,3,2,7,5,0]
char_array = [
    "011",
    "101",
    "093",
    "004",
    "z31",
    "z22",
    "z13",
]
print(sorting.LocalInsertionSort(array))

print(sorting.TreeSort(array))
print(sorting.RadixLSDSort(char_array, 2))
# # Tree Sort testing
# # Bilinked list testing
# head = bilinked_list_node(1)
# first_node = head.insert_before(5)
# head.insert_before(4)
# head.insert_before(3)
# print(first_node.toArray(first_node))
