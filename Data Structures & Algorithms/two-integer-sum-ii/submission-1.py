class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        res=[]
        for i in range(n):
            for j in range(i+1,n):
                if target - numbers[i]== numbers[j]:
                    res.append(i+1)
                    res.append(j+1)
        return res
                    
                
                
        

            

