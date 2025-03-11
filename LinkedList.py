class Solution:
    def constructLL(self, arr):
        self.head = Node(arr[0])
        curr = self.head
        
        for i in range(1,len(arr)):
            curr.next = Node(arr[i])
            curr = curr.next
         
        return self.head