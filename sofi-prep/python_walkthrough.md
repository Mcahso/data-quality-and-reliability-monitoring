# Python Problems — Guided Walkthrough

Work top to bottom. **Do not open the answer** until you've tried each hint level.

| File | Purpose |
|------|---------|
| [python_prompts.md](python_prompts.md) | Problem statements only |
| This file | Framing + hints + hidden solutions |
| [python_practice_stubs.py](python_practice_stubs.py) | Your code |
| [python_drill.py](python_drill.py) | Full solutions (spoiler) |

**Interview opener (say this every time):** restate the problem → confirm input/output → list edge cases → brute force → optimize → state complexity → dry-run one example.

---

## Problem 1 — Longest Contiguous Increasing Run

```python
def longest_increasing_run(nums: list[int]) -> int:
```

**Example:** `[2, 3, 5, 4, 6, 7, 8]` → `4` (the run `[4, 6, 7, 8]`)

### Frame it

| Question | Why it matters |
|----------|----------------|
| Contiguous or can we skip elements? | **Contiguous only** — this is not classic LIS |
| Strictly increasing or non-decreasing? | **Strict** — `[1, 1, 2]` breaks at the second `1` |
| Return length or the subarray itself? | Length only |
| Empty input? | Return `0` |

**Pattern:** single-pass loop with a running window.

**Edge cases:** `[]`, `[1]`, all decreasing, all equal (each gives length 1 except empty → 0).

### Hint 1
Track where the **current run started**. When does a run break?

### Hint 2
Compare `nums[i]` to `nums[i - 1]`. Start your loop at index **1**, not 0 — there is no previous element at index 0.

### Hint 3
Keep `start` (index where current run began) and `best` (max length seen). On break, reset `start = i`. On extend, update `best = max(best, i - start + 1)`.

### Dry-run checkpoint
Walk through `[2, 3, 5, 4, 6, 7, 8]` aloud. When `i = 3` (value 4), what happens to `start`?

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def longest_increasing_run(nums: list[int]) -> int:
    if not nums:
        return 0
    start = 0
    best = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            best = max(best, i - start + 1)
        else:
            start = i
    return best
```

**Complexity:** O(n) time, O(1) space.

**Common bug:** Using `input[i-1]` when `i == 0` (wraps to last element in Python).

</details>

---

## Problem 2 — Group Anagrams

```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Case sensitive? | Lowercase only per constraints |
| Empty strings? | Possible — `""` anagrams with `""` |
| Order of groups / within group? | Any order |

**Pattern:** hash map — all anagrams share the same **canonical key**.

**Edge cases:** single string, all unique, all anagrams of each other.

### Hint 1
Two strings are anagrams if they have the **same character counts**. What can you use as a dict key?

### Hint 2
Options for key: (a) sorted string — `"".join(sorted(s))`, (b) tuple of counts — `tuple(sorted(Counter(s).items()))`.

### Hint 3
`defaultdict(list)`: for each string, compute key → append to `buckets[key]`. Return `list(buckets.values())`.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
from collections import Counter, defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    buckets: dict[tuple, list[str]] = defaultdict(list)
    for s in strs:
        key = tuple(sorted(Counter(s).items()))
        buckets[key].append(s)
    return list(buckets.values())
```

**Complexity:** O(n · k log k) with sort-key; O(n · k) with count-key; k = max word length.

</details>

---

## Problem 3 — Merge Intervals

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Inclusive endpoints? | `[1,4]` and `[4,5]` **touch** → merge to `[1,5]` |
| Already sorted? | Don't assume — sort by start first |
| Empty input? | Return `[]` |

**Pattern:** sort + linear scan.

**Edge cases:** one interval, no overlaps, all overlap into one.

### Hint 1
If intervals are sorted by **start time**, overlapping intervals appear **adjacent**.

### Hint 2
Keep a `merged` list. For each new interval: if `start <= merged[-1][1]`, extend end; else append new interval.

### Hint 3
After sorting, compare against the **last merged** interval only — not all previous ones.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

**Complexity:** O(n log n) time, O(n) space.

</details>

---

## Problem 4 — Top K Frequent Elements

```python
def top_k_frequent(nums: list[int], k: int) -> list[int]:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Return values or (value, count) pairs? | Values only |
| Tie-breaking? | Guaranteed unique answer |
| k larger than unique count? | Won't happen per constraints |

**Pattern:** frequency count → select top k.

### Hint 1
First step: count frequencies. Python's `Counter` has a built-in for top items.

### Hint 2
`Counter(nums).most_common(k)` returns `[(val, count), ...]`. Extract just the values.

### Hint 3
Alternative for interviews: bucket sort by frequency index (O(n)) — only mention if asked to beat O(n log n).

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    return [x for x, _ in Counter(nums).most_common(k)]
```

**Complexity:** O(n log u) with heap/most_common; O(n) with bucket sort; u = unique elements.

</details>

---

## Problem 5 — Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s: str) -> int:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Empty string? | Return 0 |
| Substring = contiguous? | Yes |
| Character set? | Any chars — use dict, not fixed-size array, unless asked |

**Pattern:** sliding window + last-seen index map.

**Edge cases:** `""`, `"bbbbb"`, all unique chars.

### Hint 1
Use two pointers (`start`, `end`) or a single `start` with `end` iterating. Window is valid when **no duplicate** inside.

### Hint 2
When you see a repeat of char `c`, move `start` to **after the previous occurrence** of `c` — but only if that occurrence is inside the current window.

### Hint 3
Store `last[ch] = index`. If `ch in last and last[ch] >= start`, set `start = last[ch] + 1`. Update `best` each step.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def length_of_longest_substring(s: str) -> int:
    last: dict[str, int] = {}
    start = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best
```

**Complexity:** O(n) time, O(min(n, alphabet)) space.

**Dry-run:** `"abcabcbb"` — window grows to `"abc"`, then `'a'` repeats → shrink start past first `'a'`.

</details>

---

## Problem 6 — Two Sum

```python
def two_sum(nums: list[int], target: int) -> list[int]:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Return values or indices? | **Indices** |
| Exactly one solution? | Yes — no need to handle zero or many |
| Same element twice? | Not allowed |

**Pattern:** hash map of `{value: index}`.

### Hint 1
For each `v` at index `i`, you need `target - v`. Have you seen the complement before?

### Hint 2
One pass: check if `need in seen` **before** adding current value (avoids using same index twice).

### Hint 3
`seen[v] = i` after the check.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, v in enumerate(nums):
        need = target - v
        if need in seen:
            return [seen[need], i]
        seen[v] = i
    return []
```

**Complexity:** O(n) time, O(n) space.

</details>

---

## Problem 7 — Maximum Subarray

```python
def max_subarray(nums: list[int]) -> int:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| All negative? | Return the **least negative** single element |
| Empty array? | Constraint says length ≥ 1 |
| Return sum or indices? | Sum only |

**Pattern:** Kadane's algorithm — greedy/DP.

### Hint 1
At each element, decide: extend the current subarray or start fresh at this element?

### Hint 2
`cur = max(x, cur + x)` — if extending makes it worse than `x` alone, restart.

### Hint 3
Track `best = max(best, cur)` globally. Initialize both with `nums[0]`.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def max_subarray(nums: list[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

**Complexity:** O(n) time, O(1) space.

**Say aloud:** "Negative running sum never helps future extensions — drop it."

</details>

---

## Problem 8 — Product of Array Except Self

```python
def product_except_self(nums: list[int]) -> list[int]:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Division allowed? | **No** |
| Zeros in array? | Product becomes zero for all but that index — handle in dry-run |
| O(n) required? | Yes — prefix/suffix trick |

**Pattern:** prefix products left-to-right, suffix products right-to-left.

### Hint 1
Brute force O(n²) won't pass. For index `i`, answer = (product of all left) × (product of all right).

### Hint 2
First pass: fill `out[i]` with prefix product **before** `i`. Second pass: multiply by suffix product **after** `i`.

### Hint 3
Use scalar variables `prefix` and `suffix` — no extra arrays needed beyond output.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [1] * n
    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]
    return out
```

**Complexity:** O(n) time, O(1) extra space (output doesn't count).

</details>

---

## Problem 9 — Valid Anagram

```python
def is_anagram(s: str, t: str) -> bool:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Different lengths? | Immediately `False` |
| Unicode? | Lowercase ASCII only |

**Pattern:** Counter or sort comparison.

### Hint 1
Quick reject: if `len(s) != len(t)`, return False.

### Hint 2
`Counter(s) == Counter(t)` is one line and O(n).

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

**Complexity:** O(n) time, O(1) space (fixed alphabet).

</details>

---

## Problem 10 — Longest Repeating Character Replacement

```python
def character_replacement(s: str, k: int) -> int:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| What counts as a replacement? | Change any char to any char, max `k` times |
| Goal? | Longest substring that **can become** all one letter |
| Uppercase only? | Yes |

**Pattern:** sliding window + "window length − most frequent char count ≤ k".

### Hint 1
For any window, chars to replace = `window_size - count_of_dominant_char`. If that exceeds `k`, shrink from the left.

### Hint 2
Track char counts in the window and `max_freq` (count of most common char in window).

### Hint 3
While `(end - start + 1) - max_freq > k`: decrement `s[start]` count, increment `start`.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
from collections import defaultdict

def character_replacement(s: str, k: int) -> int:
    counts: dict[str, int] = defaultdict(int)
    start = 0
    max_freq = 0
    best = 0
    for end, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])
        while (end - start + 1) - max_freq > k:
            counts[s[start]] -= 1
            start += 1
        best = max(best, end - start + 1)
    return best
```

**Complexity:** O(n) time — each char enters/leaves window once.

**Intuition:** You keep the majority char, replace everything else.

</details>

---

## Problem 11 — Meeting Rooms II

```python
def min_meeting_rooms(intervals: list[list[int]]) -> int:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| `[start, end)` or inclusive end? | Typical LC: **end is exclusive** for sweep; overlapping if `start < other_end` |
| Empty? | Return 0 |

**Pattern:** sort starts and ends separately, two-pointer sweep **or** min-heap of end times.

### Hint 1
Imagine meetings on a timeline. When a meeting **ends**, its room frees up for the next starting meeting.

### Hint 2
Sort all start times and all end times separately. Compare smallest unused start vs smallest unused end.

### Hint 3
If `starts[s] < ends[e]`: need a new room (`rooms += 1`). Else: reuse a room (`rooms -= 1`, advance `e`). Track max `rooms`.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    rooms = needed = 0
    s = e = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            rooms += 1
            needed = max(needed, rooms)
            s += 1
        else:
            rooms -= 1
            e += 1
    return needed
```

**Complexity:** O(n log n) time, O(n) space.

**Alternative:** min-heap of end times — mention if interviewer prefers event simulation.

</details>

---

## Problem 12 — Subarray Sum Equals K

```python
def subarray_sum(nums: list[int], k: int) -> int:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Negative numbers? | Yes — sliding window **doesn't work**; use prefix sums |
| Count subarrays, not find one? | Count total |
| Empty subarray? | Usually not counted unless sum is 0 and problem allows |

**Pattern:** prefix sum + hash map counting prior prefixes.

### Hint 1
Subarray sum `i..j` = `prefix[j] - prefix[i-1]`. You want `prefix[j] - prefix[i] = k` → look for `prefix[i] = prefix[j] - k`.

### Hint 2
As you walk, maintain `counts[prefix_sum]` = how many times you've seen that prefix.

### Hint 3
Initialize `counts[0] = 1` (empty prefix). For each element: `prefix += x`; add `counts[prefix - k]` to answer; increment `counts[prefix]`.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    prefix = 0
    counts: dict[int, int] = defaultdict(int)
    counts[0] = 1
    total = 0
    for x in nums:
        prefix += x
        total += counts[prefix - k]
        counts[prefix] += 1
    return total
```

**Complexity:** O(n) time, O(n) space.

**Dry-run:** `[1,1,1], k=2` — prefixes 1, 2, 3; at prefix 2, one prior prefix with sum 0 → one subarray `[1,1]` at indices 0-1; at prefix 3, one with sum 1 → indices 1-2.

</details>

---

## Problem 13 — Contains Duplicate

```python
def contains_duplicate(nums: list[int]) -> bool:
```

### Frame it
Simple existence check. Tradeoff: set O(n) space vs sort O(1) extra space.

### Hint 1
If you've seen a number before, return True. What structure gives O(1) lookup?

### Hint 2
`len(nums) != len(set(nums))` is the shortest correct answer.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))
```

**Complexity:** O(n) time, O(n) space.

</details>

---

## Problem 14 — Valid Palindrome

```python
def is_palindrome(s: str) -> bool:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| What counts as alphanumeric? | `str.isalnum()` |
| Case? | Ignore — lowercase before compare |

**Pattern:** two pointers **or** filter + reverse.

### Hint 1
Clean the string first: keep only alphanumeric, lowercase.

### Hint 2
Compare cleaned list to its reverse. Two-pointer alternative: `left`, `right` skip non-alnum.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def is_palindrome(s: str) -> bool:
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]
```

**Complexity:** O(n) time, O(n) space for cleaned string; O(1) extra with two pointers.

</details>

---

## Problem 15 — Best Time to Buy and Sell Stock

```python
def max_profit(prices: list[int]) -> int:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| One transaction? | Buy once, sell once, sell after buy |
| No profit possible? | Return 0 |

**Pattern:** track minimum price seen so far.

### Hint 1
For each day, the best profit if you sell today = `price - min_price_so_far`.

### Hint 2
Update `low = min(low, p)` and `best = max(best, p - low)` in one pass.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    low = prices[0]
    best = 0
    for p in prices[1:]:
        best = max(best, p - low)
        low = min(low, p)
    return best
```

**Complexity:** O(n) time, O(1) space.

</details>

---

## Problem 16 — Longest Consecutive Sequence

```python
def longest_consecutive(nums: list[int]) -> int:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Must be O(n)? | Yes — sorting is O(n log n), not acceptable |
| Duplicates? | Don't double-count — use a set |

**Pattern:** set + only start counting from sequence **beginnings**.

### Hint 1
Put all numbers in a `set` for O(1) lookup.

### Hint 2
Only start a walk from `n` if `n - 1` is **not** in the set (otherwise you'd recount the same sequence).

### Hint 3
From each start, count `n, n+1, n+2, ...` while in set. Update global max.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n - 1 in num_set:
            continue
        length = 1
        while n + length in num_set:
            length += 1
        best = max(best, length)
    return best
```

**Complexity:** O(n) time — each element visited at most twice.

</details>

---

## Problem 17 — Permutation in String

```python
def check_inclusion(s1: str, s2: str) -> bool:
```

### Frame it

| Question | Why it matters |
|----------|----------------|
| Window size? | Fixed = `len(s1)` |
| Permutation = same char counts? | Yes |

**Pattern:** fixed-size sliding window + frequency match.

### Hint 1
If `len(s1) > len(s2)`, return False immediately.

### Hint 2
Track `need = Counter(s1)` and window counts. Window valid when counts match for all chars in `need`.

### Hint 3
Expand `right`; when window exceeds `len(s1)`, shrink from `left`. Track `formed` = number of chars whose window count equals need count.

<details>
<summary><strong>Answer (click to reveal)</strong></summary>

```python
from collections import Counter, defaultdict

def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    need = Counter(s1)
    window: dict[str, int] = defaultdict(int)
    required = len(need)
    formed = 0
    left = 0
    for right, ch in enumerate(s2):
        window[ch] += 1
        if ch in need and window[ch] == need[ch]:
            formed += 1
        if right - left + 1 > len(s1):
            left_ch = s2[left]
            if left_ch in need and window[left_ch] == need[left_ch]:
                formed -= 1
            window[left_ch] -= 1
            left += 1
        if formed == required:
            return True
    return False
```

**Complexity:** O(n) time, O(1) space (26 letters).

</details>

---

## Pattern cheat sheet (after you've attempted problems)

| Pattern | Problems |
|---------|----------|
| Single-pass window | 1, 15 |
| Hash map lookup | 6, 13 |
| Hash map bucket/group | 2, 4, 9 |
| Sort + scan | 3, 11 |
| Sliding window variable | 5, 10 |
| Sliding window fixed | 17 |
| Prefix sum + dict | 12 |
| Prefix/suffix array | 8 |
| Kadane | 7 |
| Set sequence start | 16 |
| Two pointers / clean string | 14 |

---

## How to use this in a mock

1. Read prompt from [python_prompts.md](python_prompts.md).
2. Do **Frame it** out loud (30 sec).
3. Try coding after Hint 1 only — then Hint 2 if stuck.
4. Run: `python3 sofi-prep/python_practice_stubs.py --problem N`
5. Open answer only to compare structure, not to memorize.

**Verify all:** `python3 sofi-prep/python_practice_stubs.py --all`
