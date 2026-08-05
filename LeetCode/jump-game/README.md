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
The solution iterates backward through the array once. In each iteration, it checks if the current index can reach the current 'target' index. If it can, it updates the 'target' to the current index. The goal is to see if the starting index (0) can become the 'target'. This single pass makes the time complexity linear, and it uses only a few variables, resulting in constant space complexity.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
