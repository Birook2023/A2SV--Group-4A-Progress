#User function Template for python3

class Solution:
    def heapify(self,arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        
        if l < n and arr[i] < arr[l]:
            largest = l
     
        if r < n and arr[largest] < arr[r]:
            largest = r
     
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]

            self.heapify(arr, n, largest)
    
    def buildHeap(self,arr,n):
        startIdx = (n//2)-1
        
        for i in range(startIdx, -1, -1):
            self.heapify(arr, n, i)
   
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
