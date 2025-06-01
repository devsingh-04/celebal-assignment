class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")
        if n <= 0:
            raise Exception("Index must be 1 or greater.")

        if n == 1:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1
        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise Exception("Index out of range.")

        prev.next = current.next

if __name__ == "__main__":
    ll = LinkedList()
    # Sample testing:
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    print("Initial list:")
    ll.print_list()

    print("Deleting node 2:")
    ll.delete_nth_node(2)
    ll.print_list()

    print("Trying to delete node 5 (out of range):")
    try:
        ll.delete_nth_node(5)
    except Exception as e:
        print(e)
