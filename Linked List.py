#linked list create
class node:
    def __init__(self, data = None):
        self.data = data
        self.nextval = None

class linkedlist:
    def __init__(self):
        self.headval = None

list1 = linkedlist()
list1.headval = node('mon')
e1 = node('tue')
e2 = node('wed')

list1.headval.nextval = e1
e2.nextval = e2


class node:
    def __init__(self, data = None):
        self.data = data
        self.nextval = None

class linkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.data)
            printval =printval.nextval
list1 = linkedlist()
list1.headval = node('wed')
e1 = node('thur')
e2 = node('fri')

list1.headval.nextval =e1
e1.nextval = e2

list1.listprint()




