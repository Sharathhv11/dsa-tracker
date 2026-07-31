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
The solution uses a two-pointer approach. One pointer `i` iterates from the beginning, and another pointer `r` iterates from the end. If an element at `i` matches `val`, it's swapped with the element at `r`, and `r` is decremented. Otherwise, `i` is incremented. This ensures all elements not equal to `val` are moved to the beginning of the array. Since each element is visited at most once, the time complexity is O(N), and no extra space is used, resulting in O(1) space complexity.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
