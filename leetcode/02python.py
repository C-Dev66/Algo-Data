class Solution:
    def moveZeroes(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[count] = nums[i]
                count += 1
        # After this loop, nums = [1,3,12,3,12]
        
        if n >1:
            for i in range(n-count,n):
                nums[i] = 0

            #print(nums)
        
        # After this loop, nums = [1,3,12,0,0]

        
        return nums

nums = [0,1,0,3,12]

ll = Solution()
print(ll.moveZeroes(nums))




''
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
**********
'''
n = int(input("Write the number:"))
print("*")
print("**")
for i in range(n-2):
    print("*"," "*i, "*")
print("*"*n)

'''
n = int(input("Enter row number:  "))
for row in range(n+1):
    for col in range(row+1):
        if row ==n or col ==0 or col ==row:
            print("*",end="")
        else:
            print(end=" ")
    print() 
'''
