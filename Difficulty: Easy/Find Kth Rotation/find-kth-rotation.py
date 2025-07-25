class Solution:
    def findKRotation(self, arr):
        def findRotationIndex(arr, low, high):
            if arr[low] <= arr[high]:
                return low  # Already sorted, no rotation
            
            while low <= high:
                mid = low + (high - low) // 2

                # Check if mid+1 is the smallest
                if mid < high and arr[mid] > arr[mid + 1]:
                    return mid + 1
                # Check if mid itself is the smallest
                if mid > low and arr[mid] < arr[mid - 1]:
                    return mid
                
                # Decide the direction
                if arr[mid] >= arr[low]:
                    low = mid + 1
                else:
                    high = mid - 1

        return findRotationIndex(arr, 0, len(arr) - 1)

        