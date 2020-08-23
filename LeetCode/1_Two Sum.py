#3316 ms 14.8 MB
#sol1) 모든 리스트원소를 순회하며 target-해당원소 값이 리스트에 있는지 확인(배열 전체 다시 확인) => O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for e,n in enumerate(nums):
            for e2 in range(0,e): #이 방법 대신 nums.index(target-n)으로 하면 1512 ms 15 MB
                if nums[e2] == target-n:
                    return [e2,e]
 
#56 ms	15.3 MB	
#sol2) dictionary에 담아서 검색시간 단축 => O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for e,n in enumerate(nums):
            if target-n in dic:
                return [dic[target-n], e]
            dic[n]=e
                   