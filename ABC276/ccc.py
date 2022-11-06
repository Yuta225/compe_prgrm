class Solution(object):
   def prevPermOpt1(self, A):
      n = len(A)
      for left in range(n-2,-2,-1):
         if left == -1:
            return A
         elif A[left]>A[left+1]:
            break
      element = 0
      index = 0
      for right in range(left+1,n):
         if A[right]<A[left] and A[right]>element:
            element = A[right]
            index = right
      temp = A[left]
      A[left] = A[index]
      A[index] = temp
      return A
ob = Solution()
N = int(input())
p = list(map(int,input().split()))
print(ob.prevPermOpt1(p))