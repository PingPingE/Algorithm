'''
Given two sorted arrays nums1 and nums2 of size m and n respectively.

Return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).
'''
#merge sorting에서 merge부분 응용(while, if조건문 활용)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m,n = len(nums1), len(nums2)
        sorted_list = []
        mid = (m+n)//2
        s1,s2 = 0,0
        while s1<m and s2<n and len(sorted_list) <= mid :#볼 만큼만 보고 break
            if nums1[s1] < nums2[s2]:
                sorted_list.append(nums1[s1])
                s1 += 1
            else:
                sorted_list.append(nums2[s2])
                s2 += 1
    
        if len(sorted_list) == mid+1: #sorted_list가 충분히 채워졌는지 체크
                if (m+n)%2 == 0:
                    return (sorted_list[-1]+sorted_list[-2])/2
                else:
                    return sorted_list[-1]
    
        #아직 sorted_list가 충분히 채워지지 않은 경우
        while s1<m and len(sorted_list) <= mid:
            sorted_list.append(nums1[s1])
            s1 += 1
            
        while s2<n and len(sorted_list) <= mid:
            sorted_list.append(nums2[s2])
            s2+=1
        
        if (m+n)%2 == 0:
            return (sorted_list[-1]+sorted_list[-2])/2
        else:
            return sorted_list[-1]
            
 
            