from GUI import GUI

class LinkList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"{self.value}"
    
if __name__ == "__main__":
    # link_list = LinkList()
    # link_list.append(1)
    # link_list.append(2)
    # link_list.append(3)
    
    # print(link_list.head)
    # print(link_list.head.next)
    # print(link_list.head.next.next)2
    g = GUI()
    g.run()