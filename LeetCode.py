class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nodup = set(nums)
        if len(nums) == len(nodup):
            return False

        return True

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        strs_dict = {}
        result_list = []

        for char in strs:
            sorted_str = ''.join(sorted(char))
            if sorted_str not in strs_dict:
                strs_dict[sorted_str] = [char]
            else:
                strs_dict[sorted_str].append(char)
        result_list.extend(strs_dict.values())
        return result_list

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return ([num_indices[complement], i])
            num_indices[num] = i

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_indices = {}  # Rakamların indekslerini saklayacak bir sözlük
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_indices:  # Eşleşen sayı önceden görülmüş mü?
                return [num_indices[complement] + 1, i + 1]  # İndeksleri döndür
            num_indices[num] = i  # Rakamı ve indeksi sakla
        return []

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == len(t):
            for i in s:
                if i in t:
                    t = t.replace(i, '', 1)
                else:
                    return False
        else:
            return False
        return True

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        pal_s = s[::-1]
        if s == pal_s:
            return True
        else:
            return False