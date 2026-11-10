class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

    def is_empty(self):
        return self.head is None


def run_linked_list():
    ll = LinkedList()

    letters = ['D', 'E', 'I', 'P', 'A', 'R', 'I', 'N', 'E']
    for letter in letters:
        ll.insert(letter)

    print("Initial Linked List:")
    # 4. Display all letters
    ll.display()
    print("-" * 30)

    while not ll.is_empty():
        ll.delete_first()
        print("After deleting first node:")
        ll.display()

    print("-" * 30)
    print("Linked list is now empty. Stop.")


if __name__ == "__main__":
    run_linked_list()