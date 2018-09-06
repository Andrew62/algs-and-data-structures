class MyCircularDeque:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.k = k
        self.q = []

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.q.insert(0, value)
            return True
        return False
        

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.q.append(value)
            return True
        return False

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.q.pop(0)
            return True
        return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if not self.isEmpty():
            self.q.pop(-1)
            return True
        return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.q.pop(0)
        return None

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if not self.isEmpty():
            return self.q.pop(-1)
        return None
        

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return len(self.q) == 0
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return len(self.q) == self.k
        