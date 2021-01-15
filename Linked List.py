#linked list create
#creating a node
class node:
    def __init__(self, data = None):
#assinging a data to node 
        self.data = data
#assinging address for the data to next value
        self.nextval = None
#creating a head node
class linkedlist:
    def __init__(self):
        self.headval = None
#calling class functions and assinging to list1
list1 = linkedlist()
#calling headval and assining value to the head node
list1.headval = node('mon')
#assinging value to variable e1 and e2 by calling node
e1 = node('tue')
e2 = node('wed')
#assinging the address of the head node to the node e1
list1.headval.nextval = e1
#assinging the address for node e1 to the next node value e2
e1.nextval = e2


class node:
    def __init__(self, data = None):
        self.data = data
        self.nextval = None

class linkedlist:
    def __init__(self):
        self.headval = None
#Travesing through the linked list to print the value
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




