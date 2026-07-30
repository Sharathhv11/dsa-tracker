# Check If Array Is Sorted And Rotated

## Problem Information
- **Platform:** LeetCode
- **Language:** python
- **Runtime:** 1 ms
- **Memory:** 12.3 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The code iterates through the array once, comparing each element with the next (circularly). It counts the number of 'breaks' in the non-decreasing order. A sorted and rotated array can have at most one such break. The time complexity is O(N) due to the single pass, and space complexity is O(1) as only a few variables are used.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
