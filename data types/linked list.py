class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_duplicates(head):
    seen = set()
    current = head
    prev = None

    while current:
        if current.val not in seen:
            seen.add(current.val)
            prev = current
        else:
            prev.next = current.next
        current = current.next

    return head


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

print("Original Path:")
print_list(head)

head = remove_duplicates(head)

print("Purified Path:")
print_list(head)

