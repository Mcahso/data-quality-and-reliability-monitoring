# SoFi Python Interview — LeetCode Question Bank

**Panel:** Sean MacRae · **Level:** LC Medium (plus a few Easy warm-ups)  
**Skills tested:** functions, loops, lists, dicts, strings, hash maps, sliding window, two pointers

**Practice workflow:**
1. Solve from this doc without looking at solutions.
2. Check against `python_practice_stubs.py` tests: `python3 sofi-prep/python_practice_stubs.py --problem N`
3. Compare to `python_drill.py` when stuck.

---

## Study order (Sat → Tue)

| Day | Problems |
|-----|----------|
| **Sat** | 1, 2, 3, 4 |
| **Sun** | 5, 6, 7, 8 |
| **Mon** | 9, 10, 11, 12 + timed mock on 5 or 9 |
| **Tue AM** | Warm-up #1 or #13, then review patterns |

---

## Tier A — Core (must do)

### 1. Longest Contiguous Increasing Run (Custom)

**Pattern:** Single pass, loop logic  
**Not on LeetCode** — same family as your [practice.ipynb](../practice.ipynb)

Given an integer array `nums`, return the length of the **longest contiguous strictly increasing** subarray.

```
Input:  nums = [2, 3, 5, 4, 6, 7, 8]
Output: 4
Explanation: [4, 6, 7, 8]
```

```
Input:  nums = [5, 4, 3]
Output: 1
```

**Constraints:** `0 <= len(nums) <= 10^5`

**Edge cases:** empty list → 0; single element → 1; all equal → 1 (strictly increasing means no plateaus count)

**Target complexity:** O(n) time, O(1) space

---

### 2. Group Anagrams — [LC 49](https://leetcode.com/problems/group-anagrams/)

**Pattern:** Dict + hash bucket

Given `strs`, group anagrams together. Return groups in any order.

```
Input:  strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Constraints:** `1 <= strs.length <= 10^4`, lowercase letters

**Approach hint:** Key = sorted string OR char-count tuple

**Target:** O(n · k log k) sort-key or O(n · k) count-key; k = max word length

---

### 3. Merge Intervals — [LC 56](https://leetcode.com/problems/merge-intervals/)

**Pattern:** Sort + loop

Given array of `[start, end]` intervals, merge all overlapping intervals.

```
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

```
Input:  intervals = [[1,4],[4,5]]
Output: [[1,5]]
```

**Constraints:** `1 <= intervals.length <= 10^4`

**Target:** O(n log n) time, O(n) space

---

### 4. Top K Frequent Elements — [LC 347](https://leetcode.com/problems/top-k-frequent-elements/)

**Pattern:** Counter + heap or bucket sort

Return the `k` most frequent integers. Any order OK.

```
Input:  nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Constraints:** Answer is unique; `1 <= k <= number of unique elements`

**Target:** O(n) average with bucket sort, or O(n log k) with heap

---

### 5. Longest Substring Without Repeating Characters — [LC 3](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

**Pattern:** Sliding window + dict

```
Input:  s = "abcabcbb"
Output: 3
Explanation: "abc"
```

```
Input:  s = "bbbbb"
Output: 1
```

**Constraints:** `0 <= s.length <= 5 * 10^4`

**Target:** O(n) time, O(min(n, alphabet)) space

---

### 6. Two Sum — [LC 1](https://leetcode.com/problems/two-sum/)

**Pattern:** Hash map

Return **indices** of two numbers that add to `target`. Exactly one solution; don't reuse same element.

```
Input:  nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Constraints:** `2 <= nums.length <= 10^4`

**Target:** O(n) time, O(n) space

---

### 7. Maximum Subarray — [LC 53](https://leetcode.com/problems/maximum-subarray/)

**Pattern:** Kadane's algorithm (DP / greedy)

Find contiguous subarray with the largest sum.

```
Input:  nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1]
```

**Constraints:** `1 <= nums.length <= 10^5`

**Target:** O(n) time, O(1) space

---

### 8. Product of Array Except Self — [LC 238](https://leetcode.com/problems/product-of-array-except-self/)

**Pattern:** Prefix / suffix products

Return array `output` where `output[i]` = product of all elements except `nums[i]`. **No division.** O(n) required.

```
Input:  nums = [1,2,3,4]
Output: [24,12,8,6]
```

**Constraints:** `2 <= nums.length <= 10^5`

**Follow-up Sean might ask:** "What if zeros exist?" (handle separately in dry-run)

---

## Tier B — Plan extras (do before Tuesday)

### 9. Valid Anagram — [LC 242](https://leetcode.com/problems/valid-anagram/)

**Pattern:** Counter / sort

```
Input:  s = "anagram", t = "nagaram"
Output: true

Input:  s = "rat", t = "car"
Output: false
```

**Target:** O(n) with Counter, O(n log n) with sort

---

### 10. Longest Repeating Character Replacement — [LC 424](https://leetcode.com/problems/longest-repeating-character-replacement/)

**Pattern:** Sliding window + character replacement

You may replace at most `k` characters. Return length of longest substring containing the same letter.

```
Input:  s = "ABAB", k = 2
Output: 4
Explanation: Replace both 'A's or both 'B's → "AAAA" or "BBBB"

Input:  s = "AABABBA", k = 1
Output: 4
Explanation: "AABAB" → "AAAAB" with one replacement
```

**Constraints:** `1 <= s.length <= 10^5`, uppercase English letters

**Target:** O(n) sliding window

---

### 11. Meeting Rooms II — [LC 253](https://leetcode.com/problems/meeting-rooms-ii/)

**Pattern:** Sort + heap OR sort start/end separately

Given meeting intervals `[start, end)`, return **minimum number of conference rooms** required.

```
Input:  intervals = [[0,30],[5,10],[15,20]]
Output: 2

Input:  intervals = [[7,10],[2,4]]
Output: 1
```

**Target:** O(n log n)

**Related Easy warm-up:** [LC 252 Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) — can one person attend all?

---

### 12. Subarray Sum Equals K — [LC 560](https://leetcode.com/problems/subarray-sum-equals-k/)

**Pattern:** Prefix sum + hash map (dict)

Count number of contiguous subarrays that sum to `k`.

```
Input:  nums = [1,1,1], k = 2
Output: 2
```

```
Input:  nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [3]
```

**Target:** O(n) time, O(n) space

---

## Tier C — Warm-ups & backup (if time)

### 13. Contains Duplicate — [LC 217](https://leetcode.com/problems/contains-duplicate/) (Easy)

Return `true` if any value appears at least twice.

```
Input:  nums = [1,2,3,1]
Output: true
```

**Target:** O(n) with set

---

### 14. Valid Palindrome — [LC 125](https://leetcode.com/problems/valid-palindrome/) (Easy)

Alphanumeric only, ignore case.

```
Input:  s = "A man, a plan, a canal: Panama"
Output: true
```

**Pattern:** Two pointers, string cleaning

---

### 15. Best Time to Buy and Sell Stock — [LC 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy)

One transaction max. Return max profit.

```
Input:  prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy 1, sell 6
```

**Pattern:** Track min price, single pass

---

### 16. Longest Consecutive Sequence — [LC 128](https://leetcode.com/problems/longest-consecutive-sequence/) (Medium)

Longest consecutive elements sequence in **unsorted** array (O(n) required).

```
Input:  nums = [100,4,200,1,3,2]
Output: 4
Explanation: [1,2,3,4]
```

**Pattern:** Set + only start from sequence beginnings

---

### 17. Permutation in String — [LC 567](https://leetcode.com/problems/permutation-in-string/) (Medium)

Does `s2` contain a permutation of `s1`?

```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true
```

**Pattern:** Fixed-size sliding window + Counter

---

## Pattern quick reference

| Pattern | Problems |
|---------|----------|
| **Hash map** | 6, 12 |
| **Counter / dict grouping** | 2, 4, 9, 17 |
| **Sliding window** | 5, 10, 17 |
| **Two pointers** | 14 |
| **Sort + merge / sweep** | 3, 11 |
| **Prefix / suffix** | 8, 12 |
| **Kadane / DP** | 7 |
| **Single-pass loop logic** | 1, 15 |
| **Set lookups** | 13, 16 |

---

## Interview communication checklist (Sean)

Before coding each problem:

- [ ] Restate input/output with example
- [ ] Edge cases: empty, single element, duplicates, negatives, zeros
- [ ] Brute force → optimal
- [ ] State time/space complexity
- [ ] Dry-run one example line by line
- [ ] Mention scale: "At SoFi we'd compute aggregates in SQL first for event-level data"

---

## Timed mock (45 min — Monday or Tue AM)

Pick **one** you haven't memorized:

- **Option A:** #5 Longest Substring (sliding window)
- **Option B:** #11 Meeting Rooms II (sort + heap)
- **Option C:** #12 Subarray Sum Equals K (prefix + dict)

5 min clarify → 25 min code → 10 min test → 5 min extensions

---

## LeetCode links (copy-paste list)

```
https://leetcode.com/problems/two-sum/
https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://leetcode.com/problems/group-anagrams/
https://leetcode.com/problems/merge-intervals/
https://leetcode.com/problems/maximum-subarray/
https://leetcode.com/problems/product-of-array-except-self/
https://leetcode.com/problems/top-k-frequent-elements/
https://leetcode.com/problems/valid-anagram/
https://leetcode.com/problems/longest-repeating-character-replacement/
https://leetcode.com/problems/meeting-rooms-ii/
https://leetcode.com/problems/subarray-sum-equals-k/
https://leetcode.com/problems/contains-duplicate/
https://leetcode.com/problems/valid-palindrome/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/problems/longest-consecutive-sequence/
https://leetcode.com/problems/permutation-in-string/
```
