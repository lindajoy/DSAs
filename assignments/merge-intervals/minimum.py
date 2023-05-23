def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize left and right pointer
        left, right = 0, len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break

                # Calculate the median value
                mid = (left + right) // 2
                result = min(nums[mid], result)

                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

        return result