## Problem: Minimum Number of Bit Flips to Convert Number

**Link:** [LeetCode #2220](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/)

---

### 📝 Problem Statement
Given two integers `start` and `goal`, determine the minimum number of bit flips required to convert `start` into `goal`.

---

### 💡 Approach

#### 1. Brute Force
- Iterate through all 32 bits of `start` and `goal`.
- Compare bits at each position.
- Count positions where they differ.
- **Time Complexity:** O(32)

#### 2. Optimized
- Compute `xor = start ^ goal`.  
  The XOR result will have bits set to `1` exactly where the two numbers differ.
- Count the number of set bits in `xor`.  
  This directly gives the number of flips needed.
- **Time Complexity:** O(number_of_set_bits)  

#### **Why it works:**  
XOR isolates the differing bits in one step, and counting set bits is faster than checking each bit individually.


### ⏳ Time & Space Complexity
- **Time Complexity:** O(number_of_set_bits)  
- **Space Complexity:** O(1)
