# Python / ML Panel Guide — Sean MacRae

## Coding communication script

1. **Restate** problem + examples + edge cases (empty list, single element, duplicates).
2. **Brute force** in 1 sentence → **optimal** approach.
3. **State** time/space complexity before coding.
4. **Code** cleanly; use descriptive names.
5. **Dry-run** on `[2,3,5,4,6,7,8]` or given example.
6. **Test** edge cases aloud.

## 17 problems mapped to `python_drill.py`

| # | Pattern | Function | LeetCode |
|---|---------|----------|----------|
| 1 | Contiguous run | `longest_increasing_run` | Custom |
| 2 | Hash + bucket | `group_anagrams` | [49](https://leetcode.com/problems/group-anagrams/) |
| 3 | Sort + merge | `merge_intervals` | [56](https://leetcode.com/problems/merge-intervals/) |
| 4 | Counter | `top_k_frequent` | [347](https://leetcode.com/problems/top-k-frequent-elements/) |
| 5 | Sliding window | `length_of_longest_substring` | [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| 6 | Hash map | `two_sum` | [1](https://leetcode.com/problems/two-sum/) |
| 7 | Kadane | `max_subarray` | [53](https://leetcode.com/problems/maximum-subarray/) |
| 8 | Prefix/suffix | `product_except_self` | [238](https://leetcode.com/problems/product-of-array-except-self/) |
| 9 | Counter | `is_anagram` | [242](https://leetcode.com/problems/valid-anagram/) |
| 10 | Sliding window | `character_replacement` | [424](https://leetcode.com/problems/longest-repeating-character-replacement/) |
| 11 | Sort + sweep | `min_meeting_rooms` | [253](https://leetcode.com/problems/meeting-rooms-ii/) |
| 12 | Prefix + dict | `subarray_sum` | [560](https://leetcode.com/problems/subarray-sum-equals-k/) |
| 13 | Set | `contains_duplicate` | [217](https://leetcode.com/problems/contains-duplicate/) |
| 14 | Two pointers | `is_palindrome` | [125](https://leetcode.com/problems/valid-palindrome/) |
| 15 | Single pass | `max_profit` | [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| 16 | Set | `longest_consecutive` | [128](https://leetcode.com/problems/longest-consecutive-sequence/) |
| 17 | Sliding window | `check_inclusion` | [567](https://leetcode.com/problems/permutation-in-string/) |

Full statements: [09-python-leetcode-questions.md](09-python-leetcode-questions.md)

## Tue morning timed mock (45 min)

1. Pick problem **5**, **11**, or **12** (not #1 — you know it well).
2. 5 min: clarify + approach out loud.
3. 25 min: implement without looking at solutions.
4. 10 min: test + optimize.
5. 5 min: "How would this change at SoFi scale?" (streaming, partitioned data).

## Study schedule (Sat–Mon)

| Day | Do |
|-----|-----|
| Sat | Problems 1–4 (implement in `python_practice_stubs.py`) |
| Sun | Problems 5–8 + ML file aloud |
| Mon | Problems 9–12 + timed mock on 5 or 11 |
| Tue AM | Warm-up #13 or #15; skim 9–12 |

## Verbal tradeoffs (if Sean extends the problem)

- **Scale:** "At millions of rows we'd aggregate in SQL/Snowflake first."
- **Streaming:** "For event streams, keep a hash map of last index per character."
- **Testing:** "Unit test empty, single element, all decreasing."
