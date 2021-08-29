# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:28:27 2021

@author: lisheng
"""


class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            hash_map[value] = index
        for index1, value in enumerate(nums):
            if target - value in hash_map:
                index2 = hash_map[target - value]
                if index1 != index2:
                    return [index1, index2]
                
