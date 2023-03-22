# Largest subarray with 0 sum
# GFG

def maxLen(self, n, arr):
        #Code here
        
        ps = dict()
        
        max_ele = 0
        curr_sum = 0
        for i in range(n):
            
            curr_sum+=arr[i]
            if curr_sum == 0:
                max_ele = i + 1
            
            elif curr_sum in ps:
                max_ele = max(max_ele, i - ps[curr_sum])
            
            elif curr_sum not in ps:
                ps[curr_sum] = i 
                
        return max_ele