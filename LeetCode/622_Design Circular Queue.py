'''
Design your implementation of the circular queue. 
The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle 
and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. 
But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
'''
#sol1: 68 ms	14.7 MB
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = list(-1 for _ in range(k))
        self.index=0
        self.maximum = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.index < self.maximum:
            self.queue[self.index] = value
            self.index+=1
            return True
        return False
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.index==0:
            return False
        self.queue[:self.index-1] = self.queue[1:self.index]
        self.index -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.index==0:
            return -1
        return self.queue[0]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.index==0:
            return -1
        return self.queue[self.index-1]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.index ==0:
            return True
        return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.index==self.maximum:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()