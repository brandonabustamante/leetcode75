"""*****************************************************************************

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Solution:
TODO Add solution description
*****************************************************************************"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        new_node = ListNode(val)
        if self.next is None:
            self.next = new_node
        else:
            current = self.next
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self
        elements = []
        while current:
            elements.append(current.val)
            current = current.next
        print("LinkedList:", elements)


def mergeTwoList(list1, list2):
    output = ListNode()
    tail = output

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return output.next


def main():
    list1 = ListNode(1)
    list1.append(2)
    list1.append(3)

    list2 = ListNode(1)
    list2.append(3)
    list2.append(4)

    output = mergeTwoList(list1, list2)
    print(output.display())


if __name__ == "__main__":
    main()
