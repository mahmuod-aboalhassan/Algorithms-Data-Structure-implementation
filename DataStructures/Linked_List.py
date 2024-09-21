class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        """Method to print the values of the linked list starting from this node."""
        current = self
        while current:
            print(current.val, end='->' if current.next else '')
            current = current.next
        print()  # New line at the end

    def insert_node(self, idx, value):
        """Method to insert a new node with `value` at position `idx`."""
        if idx == 0:
            new_node = ListNode(value)
            new_node.next = self
            return new_node  # New head of the list

        current_node = self
        new_node = ListNode(value)
        idx_to = 0
        
        while current_node and idx_to < idx - 1:
            current_node = current_node.next
            idx_to += 1

        if current_node is None:
            print(f"Index {idx} is out of bounds.")
        else:
            new_node.next = current_node.next
            current_node.next = new_node
            print(f"Inserted node with value {value} at position {idx}.")
        
        return self  # Return head of the list
    # next implementing the Removing and replacing also 

# Example to create the list from the array
arr = [1, 2, 3, 4, 5, 6, 7]

# Initialize the "next_node" as None because the last node will have no next node
next_node = None

# We iterate over the array in reverse to construct the linked list
for val in reversed(arr):
    current_node = ListNode(val, next_node)
    next_node = current_node

# At the end of the loop, next_node will point to the head of the linked list
node = next_node

# Print the original list
print("Original list:")
node.print_list()

# Insert a new node with value 'inserted new node' at index 3
node = node.insert_node(3, 'inserted new node')

# Print the modified list
print("Modified list after insertion:")
node.print_list()
