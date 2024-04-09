class Soulution:
    nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
    def rearrangeArray(nums):
        temp = []
        for i in range(int(len(nums)/2)):
            if nums[i] < 0:
                temp.append(nums[i])
                nums.pop(i)
        print(temp)
        print(nums)
        for j in range(len(temp)):
            nums.insert(j+1, temp[j])
        return nums
    print(rearrangeArray(nums))
