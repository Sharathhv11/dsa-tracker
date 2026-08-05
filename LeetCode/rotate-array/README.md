# Rotate Array

## Problem Information
- **Platform:** LeetCode
- **Language:** python
- **Runtime:** 735 ms
- **Memory:** 23.4 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution uses a reverse-based approach. It reverses the entire array, then reverses the first k elements, and finally reverses the remaining n-k elements. Each reversal operation takes O(N) time, and since these operations are performed sequentially, the total time complexity is O(N). The space complexity is O(1) as the rotation is done in-place without using any extra data structures proportional to the input size.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
