class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        temp = head 
        while temp and temp.next:
            if temp.val == temp.next.val:
                duplicate_node = temp.next
                temp.next = temp.next.next
                del duplicate_node
            else:
                temp = temp.next
        return head

# Helper function to create a linked list from a Python list
def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list back to a Python list for easy printing
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Input list
head_list = [1, 1, 2, 3, 3]

# Create linked list from the input list
head = create_linked_list(head_list)

# Run the solution
sln = Solution()
new_head = sln.deleteDuplicates(head)

# Convert the resulting linked list back to a list and print it
print(linked_list_to_list(new_head))
