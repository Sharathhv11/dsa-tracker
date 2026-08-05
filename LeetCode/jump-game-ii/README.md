# Jump Game Ii

## Problem Information
- **Platform:** LeetCode
- **Language:** java
- **Runtime:** 1 ms
- **Memory:** 45.3 MB
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
This solution uses a greedy approach. It maintains a 'reach' which is the farthest index reachable with the current number of jumps. In each iteration, it explores all indices within the current reach to find the maximum new reach, incrementing the jump count. This process continues until the end of the array is reached, resulting in O(N) time complexity as each element is visited at most once.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
