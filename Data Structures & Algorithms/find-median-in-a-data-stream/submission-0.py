import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # find max
        self.large = [] # find min
        

    def addNum(self, num: int) -> None:
        if not self.small and not self.large:
            heapq.heappush(self.small, -num)
            return
        
        if num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) - len(self.large) > 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

        

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 != 0:
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        
        