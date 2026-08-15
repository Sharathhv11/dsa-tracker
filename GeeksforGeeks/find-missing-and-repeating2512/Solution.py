class Solution:
    def findTwoElement(self, arr):
        # code here
        n = len(arr)
        
        i = 0
        duplicate = -1
        missing = -1
        
        
        while( i < n ):
            num = arr[i]
            index = num - 1
            
            if( index == i ):
                i+=1
            else:
                if( arr[index] == arr[i] ):
                    duplicate = arr[i]
                    i+=1
                    continue
                arr[index],arr[i] = arr[i],arr[index]
                
        for i in range(n):
            if( arr[i] != i+1 ):
                missing = i+1
                
        return [duplicate,missing]
                
                
        
                
                
