class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k=[]
        i=0
        if len(nums1)>len(nums2):
            while i<len(nums1):
                for j in range(len(nums2)):
                    if nums1[i]==nums2[j] and nums1[i] not in k:
                        
                        k.append(nums1[i])
                i=i+1
            return k
        elif len(nums2)>len(nums1):
            i=0
            while i<len(nums2):
                for m in range(len(nums1)):
                    if nums1[m]==nums2[i] and nums2[i] not in k:
                        k.append(nums2[i])
                i+=1
            return k
        else:
            i=0
            j=0
            while i<len(nums1) and j<len(nums2):
                if nums1[i]==nums2[j] and nums1[i] not in k:
                    k.append(nums1[i])
                i+=1
                j+=1
            return k






        