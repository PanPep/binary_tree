class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_kid = None
        self.right_kid = None


class BST:
    def __init__(self):
        self.root = Node()

    def add(self, data):
        if self.root.data  == None:
            self.root.data = data
        else:

            def add_to_top(data, top):
                if data < top.data:
                    if top.left_kid == None:
                        top.right_kid = Node(data)
                    else:
                        add_to_top(data, top.left_kid)
                if data > top.data:
                    if top.right_kid == None:
                        top.right_kid = Node(data)
                    else:
                        add_to_top(data, top.right_kid)

            add_to_top(data, self.root)

    def display(self):
        result = ""

        def show_result(result, top):
            if top:
                if top.data:
                    result += str(top.data) + "-"
                    result = show_result(result, top.left_kid)
                    result = show_result(result, top.right_kid)
            return result




        print(show_result(result, self.root))



drzewo = BST()
drzewo.add(3)
drzewo.add(2)
drzewo.add(1)
drzewo.add(8)
drzewo.add(7)
drzewo.add(99)


drzewo.display()
