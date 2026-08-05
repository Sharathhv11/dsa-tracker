# Jump Game

## Problem Information
- **Platform:** LeetCode
- **Language:** python
- **Runtime:** 23 ms
- **Memory:** 13.2 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution iterates backward from the second-to-last element to the beginning. It keeps track of the furthest reachable index (target). If the current index plus its value can reach or surpass the target, the target is updated to the current index. This greedy approach ensures that if the first index can reach the final target, it returns true. The single loop results in O(N) time complexity, and no extra data structures are used, leading to O(1) space complexity.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
