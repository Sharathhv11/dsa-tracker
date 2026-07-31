# Remove Element

## Problem Information
- **Platform:** LeetCode
- **Language:** java
- **Runtime:** 0 ms
- **Memory:** 43.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution uses two pointers, i and r, to iterate through the array. When an element equal to 'val' is found at index i, it's swapped with the element at index r, and r is decremented. This process continues until i crosses r, effectively moving all elements not equal to 'val' to the beginning of the array. Each element is visited at most once, resulting in O(N) time complexity and O(1) space complexity as no extra data structures are used.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
