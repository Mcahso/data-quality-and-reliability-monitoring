# Python Interview Prompts

Work through these independently. Implement in your own file or in `python_practice_stubs.py`.

**Verify:** `python3 sofi-prep/python_practice_stubs.py --problem N`

---

## Problem 1 — Longest Contiguous Increasing Run

Implement:

```python
def longest_increasing_run(nums: list[int]) -> int:
```

Given an integer array `nums`, return the length of the longest **contiguous strictly increasing** subarray.

Each element in the subarray must be **greater than** the previous element (equal values do not extend the run).

**Example 1**

```
Input:  nums = [2, 3, 5, 4, 6, 7, 8]
Output: 4
```

**Example 2**

```
Input:  nums = [5, 4, 3]
Output: 1
```

**Example 3**

```
Input:  nums = []
Output: 0
```

**Constraints**

- `0 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Problem 2 — Group Anagrams

Implement:

```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
```

Given an array of strings, group the anagrams together. You may return the groups in any order.

**Example 1**

```
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
```

**Constraints**

- `1 <= len(strs) <= 10^4`
- `0 <= len(strs[i]) <= 100`
- `strs[i]` consists of lowercase English letters

---

## Problem 3 — Merge Intervals

Implement:

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
```

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return the result.

**Example 1**

```
Input:  intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
```

**Example 2**

```
Input:  intervals = [[1, 4], [4, 5]]
Output: [[1, 5]]
```

**Constraints**

- `1 <= len(intervals) <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

---

## Problem 4 — Top K Frequent Elements

Implement:

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
```

Return the `k` most frequent elements. You may return the answer in any order. It is guaranteed that the answer is unique.

**Example 1**

```
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]
```

**Constraints**

- `1 <= len(nums) <= 10^5`
- `-10^3 <= nums[i] <= 10^3`
- `k` is in the range `[1, number of unique elements]`

---

## Problem 5 — Longest Substring Without Repeating Characters

Implement:

```python
def length_of_longest_substring(s: str) -> int:
```

Given a string `s`, find the length of the longest substring without repeating characters.

**Example 1**

```
Input:  s = "abcabcbb"
Output: 3
```

**Example 2**

```
Input:  s = "bbbbb"
Output: 1
```

**Example 3**

```
Input:  s = ""
Output: 0
```

**Constraints**

- `0 <= len(s) <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces

---

## Problem 6 — Two Sum

Implement:

```python
def two_sum(nums: list[int], target: int) -> list[int]:
```

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

You may assume exactly one solution exists, and you may not use the same element twice. Return the indices in any order.

**Example 1**

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

**Constraints**

- `2 <= len(nums) <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid answer exists

---

## Problem 7 — Maximum Subarray

Implement:

```python
def max_subarray(nums: list[int]) -> int:
```

Given an integer array `nums`, find the contiguous subarray with the largest sum and return that sum.

**Example 1**

```
Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum 6.
```

**Example 2**

```
Input:  nums = [1]
Output: 1
```

**Constraints**

- `1 <= len(nums) <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Problem 8 — Product of Array Except Self

Implement:

```python
def product_except_self(nums: list[int]) -> list[int]:
```

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`.

You must write an algorithm that runs in O(n) time and **without using division**.

**Example 1**

```
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

**Constraints**

- `2 <= len(nums) <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix fits in a 32-bit integer

---

## Problem 9 — Valid Anagram

Implement:

```python
def is_anagram(s: str, t: str) -> bool:
```

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

**Example 1**

```
Input:  s = "anagram", t = "nagaram"
Output: True
```

**Example 2**

```
Input:  s = "rat", t = "car"
Output: False
```

**Constraints**

- `1 <= len(s), len(t) <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters

---

## Problem 10 — Longest Repeating Character Replacement

Implement:

```python
def character_replacement(s: str, k: int) -> int:
```

You are given a string `s` and an integer `k`. You can choose any character and change it to any other uppercase English character at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing at most `k` replacements.

**Example 1**

```
Input:  s = "ABAB", k = 2
Output: 4
```

**Example 2**

```
Input:  s = "AABABBA", k = 1
Output: 4
```

**Constraints**

- `1 <= len(s) <= 10^5`
- `s` consists of uppercase English letters
- `0 <= k <= len(s)`

---

## Problem 11 — Meeting Rooms II

Implement:

```python
def min_meeting_rooms(intervals: list[list[int]]) -> int:
```

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the **minimum number of conference rooms** required.

**Example 1**

```
Input:  intervals = [[0, 30], [5, 10], [15, 20]]
Output: 2
```

**Example 2**

```
Input:  intervals = [[7, 10], [2, 4]]
Output: 1
```

**Constraints**

- `1 <= len(intervals) <= 10^4`
- `0 <= start_i < end_i <= 10^6`

---

## Problem 12 — Subarray Sum Equals K

Implement:

```python
def subarray_sum(nums: list[int], k: int) -> int:
```

Given an array of integers `nums` and an integer `k`, return the total number of contiguous subarrays whose sum equals `k`.

**Example 1**

```
Input:  nums = [1, 1, 1], k = 2
Output: 2
```

**Example 2**

```
Input:  nums = [1, 2, 3], k = 3
Output: 2
```

**Constraints**

- `1 <= len(nums) <= 2 * 10^4`
- `-10^3 <= nums[i] <= 10^3`
- `-10^7 <= k <= 10^7`

---

## Problem 13 — Contains Duplicate

Implement:

```python
def contains_duplicate(nums: list[int]) -> bool:
```

Given an integer array `nums`, return `True` if any value appears at least twice, and `False` if every element is distinct.

**Example 1**

```
Input:  nums = [1, 2, 3, 1]
Output: True
```

**Example 2**

```
Input:  nums = [1, 2, 3, 4]
Output: False
```

**Constraints**

- `1 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Problem 14 — Valid Palindrome

Implement:

```python
def is_palindrome(s: str) -> bool:
```

A phrase is a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `True` if it is a palindrome, or `False` otherwise.

**Example 1**

```
Input:  s = "A man, a plan, a canal: Panama"
Output: True
```

**Example 2**

```
Input:  s = "race a car"
Output: False
```

**Constraints**

- `1 <= len(s) <= 2 * 10^5`
- `s` consists of printable ASCII characters

---

## Problem 15 — Best Time to Buy and Sell Stock

Implement:

```python
def max_profit(prices: list[int]) -> int:
```

You are given an array `prices` where `prices[i]` is the price on day `i`. You may complete at most **one** transaction: buy one share and sell one share.

Return the maximum profit you can achieve. If you cannot achieve any profit, return `0`.

**Example 1**

```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6).
```

**Example 2**

```
Input:  prices = [7, 6, 4, 3, 1]
Output: 0
```

**Constraints**

- `1 <= len(prices) <= 10^5`
- `0 <= prices[i] <= 10^4`

---

## Problem 16 — Longest Consecutive Sequence

Implement:

```python
def longest_consecutive(nums: list[int]) -> int:
```

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

**Example 1**

```
Input:  nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].
```

**Example 2**

```
Input:  nums = []
Output: 0
```

**Constraints**

- `0 <= len(nums) <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

---

## Problem 17 — Permutation in String

Implement:

```python
def check_inclusion(s1: str, s2: str) -> bool:
```

Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.

In other words, one of `s1`'s permutations is a substring of `s2`.

**Example 1**

```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: True
Explanation: s2 contains "ba", a permutation of "ab".
```

**Example 2**

```
Input:  s1 = "ab", s2 = "eidboaoo"
Output: False
```

**Constraints**

- `1 <= len(s1), len(s2) <= 10^4`
- `s1` and `s2` consist of lowercase English letters
