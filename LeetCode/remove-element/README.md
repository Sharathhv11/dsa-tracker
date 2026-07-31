# Remove Element

## Problem Information
- **Platform:** LeetCode
- **Language:** java
- **Runtime:** 0 ms
- **Memory:** 43.3 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution uses a two-pointer approach. The left pointer `i` iterates through the array, and the right pointer `r` starts from the end. When an element equal to `val` is found at `nums[i]`, it's swapped with the element at `nums[r]`, and `r` is decremented. This process ensures that all elements not equal to `val` are moved to the beginning of the array, resulting in O(N) time complexity. No extra space is used beyond a few variables, hence O(1) space complexity.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
