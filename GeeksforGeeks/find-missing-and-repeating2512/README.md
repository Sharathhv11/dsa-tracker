# Missing And Repeating

## Problem Information
- **Platform:** GeeksforGeeks
- **Language:** python3
- **Runtime:** 0.83s
- **Memory:** 1111/1111 Test Cases
- **Tags:** None

## Complexity Analysis
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

## Explanation
The solution uses an in-place cyclic sort to place each number in its correct index. During this process, it identifies the duplicate number. After sorting, it iterates through the array to find the missing number by checking if the element at index i is i+1. Both operations take linear time, and no extra space is used.

---
*Generated automatically by [CodeStreak](https://github.com/Sharathhv11/CodeStreak-webApp).*
