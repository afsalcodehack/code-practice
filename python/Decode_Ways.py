class Solution:
    result = []

    def decode_ways(self, nums, _str, i):
        if len(nums) == i:
            print(self.result)
            return

        self.result.append(_str)

        self.decode_ways(nums, nums[i], i + 1)

        self.result = self.result[:-1]

        if i < len(nums) - 2:
            self.decode_ways(nums, nums[i:i+2], i+2)


service = Solution()
service.decode_ways("1234", '', 0)
