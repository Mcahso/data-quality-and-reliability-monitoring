# Python Interview — Complete Step-by-Step Guide

**For:** Sean MacRae panel · LC medium · base Python only  
**Use with:** [python_practice_stubs.py](python_practice_stubs.py) · test with `--problem N`

You said you forgot the functions — this guide rebuilds everything from scratch. Read one problem, code it, run tests, then move on.

---

## Part 0 — Python you must remember (15 min skim)

### Dict (hash map) — your #1 tool

```python
d = {}                          # empty dict
d["key"] = 1                    # set
d.get("key", 0)                 # safe read (0 if missing)
if "key" in d: ...              # membership test
d.setdefault("key", []).append(x)  # get or create list, then append

# Loop keys and values
for k, v in d.items():
    ...
```

**Use when:** "Have I seen this before?" → store `value → index` or `key → count`.

### Set — O(1) lookup, no duplicates

```python
seen = set()
seen.add(5)
5 in seen          # True/False
len(nums) != len(set(nums))  # duplicate check
```

### List basics

```python
nums.sort()                    # in-place sort
sorted(nums)                   # new sorted list
nums[1:4]                      # slice
[0] * 26                       # list of 26 zeros
"".join(sorted("eat"))         # "aet"
```

### Loop patterns

```python
for i, x in enumerate(arr):    # index + value
for i in range(1, len(arr)):   # start at 1 (compare to i-1)
for left in range(n):
    for right in range(left, n):  # nested = O(n²) — avoid if possible
```

### Variables to track in almost every problem

| Variable | Meaning |
|----------|---------|
| `best` / `result` | Best answer so far |
| `start` / `left` | Window or run start index |
| `cur` / `running` | Running sum, product, or streak |
| `seen` / `counts` | Dict or set of what you've visited |

---

## Part 0.5 — The 6 patterns (memorize these names)

| Pattern | When you hear… | Problems |
|---------|----------------|----------|
| **Single pass + state** | contiguous run, one scan | 1, 15 |
| **Hash map** | find pair, count, group | 2, 4, 6, 9, 12, 13 |
| **Sort then scan** | intervals, meetings | 3, 11 |
| **Sliding window** | substring, window of size k | 5, 10, 17 |
| **Prefix sum + dict** | subarray sum, count subarrays | 12 |
| **Prefix/suffix build** | product except self | 8 |
| **Kadane** | max subarray sum | 7 |
| **Set + sequence start** | consecutive numbers unsorted | 16 |
| **Two pointers** | palindrome, clean string | 14 |

---

## Study order (lock-in plan)

| Session | Problems | Time |
|---------|----------|------|
| **A** | 1, 6, 13, 9 | 2 hrs — dict & loops |
| **B** | 2, 4, 5 | 2 hrs — grouping & window |
| **C** | 7, 8, 15, 14 | 2 hrs — pass & pointers |
| **D** | 3, 11, 12 | 2 hrs — sort & prefix |
| **E** | 10, 16, 17 | 2 hrs — harder windows |
| **Mock** | Pick 5, 11, or 12 timed | 45 min |

---

# Problem 1 — Longest Contiguous Increasing Run

## What it's asking
Longest **consecutive slice** where each number is **strictly greater** than the one before. Not LeetCode LIS (that allows skips).

## Step-by-step

**Step 1 — Edge cases**
- `[]` → return `0`
- One element → return `1`

**Step 2 — Don't start loop at 0**
At `i=0`, there is no previous element. Start at `i=1` and compare `nums[i]` to `nums[i-1]`.

**Step 3 — Track two things**
- `start` = index where current increasing run began
- `best` = max run length seen (initialize to `1` if non-empty)

**Step 4 — Each index i ≥ 1**
- If `nums[i] > nums[i-1]`: run continues → update `best = max(best, i - start + 1)`
- Else: run breaks → new run starts at `i` → set `start = i`

**Step 5 — Return `best`**

## Dry-run: `[2, 3, 5, 4, 6, 7, 8]`

| i | nums[i] | vs prev | start | run len | best |
|---|---------|---------|-------|---------|------|
| 1 | 3 | ↑ | 0 | 2 | 2 |
| 2 | 5 | ↑ | 0 | 3 | 3 |
| 3 | 4 | break | 3 | 1 | 3 |
| 4 | 6 | ↑ | 3 | 2 | 3 |
| 5 | 7 | ↑ | 3 | 3 | 3 |
| 6 | 8 | ↑ | 3 | **4** | **4** |

## Solution

```python
def longest_increasing_run(nums):
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

**Time:** O(n) · **Space:** O(1)

## Common mistakes
- Using `input[i-1]` when `i==0` (Python wraps to last index!)
- Returning length of **last** run only without tracking `best`

---

# Problem 2 — Group Anagrams

## What it's asking
Put words that are rearrangements of each other in the same bucket.

## Step-by-step

**Step 1 — Anagrams share the same "signature"**
Two words are anagrams ↔ same letters ↔ same sorted string OR same letter counts.

**Step 2 — Pick a key (no imports needed)**
- Easy: `key = "".join(sorted(word))`
- Faster: `counts = [0]*26`, increment `counts[ord(c)-ord('a')]`, use `tuple(counts)` as key

**Step 3 — Dict of key → list of words**
```python
groups = {}
for word in strs:
    key = ...
    if key not in groups:
        groups[key] = []
    groups[key].append(word)
```

**Step 4 — Return `list(groups.values())`**

## Dry-run: `"eat", "tea", "bat"`

| word | key (sorted) | groups |
|------|--------------|--------|
| eat | aet | {aet: [eat]} |
| tea | aet | {aet: [eat, tea]} |
| bat | abt | {aet: [...], abt: [bat]} |

## Solution (sorted key — simplest)

```python
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

## Solution (count key — O(n·k), no sort)

```python
def group_anagrams(strs):
    groups = {}
    for s in strs:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        key = tuple(counts)
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
```

## Common mistakes
- Using list as dict key (must use tuple or string)
- Forgetting anagrams can have different lengths only if different words entirely

---

# Problem 3 — Merge Intervals

## What it's asking
Combine overlapping `[start, end]` ranges. Touching counts as overlap: `[1,4]` + `[4,5]` → `[1,5]`.

## Step-by-step

**Step 1 — Sort by start time**
```python
intervals.sort(key=lambda x: x[0])
```

**Step 2 — Initialize with first interval**
```python
merged = [intervals[0][:]]   # copy [start, end]
```

**Step 3 — For each next interval `[start, end]`**
- If `start <= merged[-1][1]`: overlap → extend end: `merged[-1][1] = max(merged[-1][1], end)`
- Else: no overlap → append new interval

**Step 4 — Return merged**

## Dry-run: `[[1,3],[2,6],[8,10],[15,18]]`

After sort (already sorted):
1. merged = [[1,3]]
2. [2,6]: 2 ≤ 3 → merge → [[1,6]]
3. [8,10]: 8 > 6 → append → [[1,6],[8,10]]
4. [15,18]: append → [[1,6],[8,10],[15,18]]

## Solution

```python
def merge_intervals(intervals):
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

**Time:** O(n log n) · **Space:** O(n)

## Common mistakes
- Forgetting `max()` on end when merging (e.g. [1,10] and [2,3] → end stays 10)
- Not sorting first

---

# Problem 4 — Top K Frequent Elements

## What it's asking
Which numbers appear most often? Return k of them.

## Step-by-step

**Step 1 — Count frequencies (plain dict)**
```python
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
```

**Step 2 — Get top k**
Option A (interview-friendly with small k):
```python
# Sort unique keys by count descending
items = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
return items[:k]
```

Option B (if you know Counter — one line):
```python
from collections import Counter
return [x for x, _ in Counter(nums).most_common(k)]
```

## Dry-run: `[1,1,1,2,2,3], k=2`
counts = {1:3, 2:2, 3:1} → top 2 → [1, 2]

## Solution (no imports)

```python
def top_k_frequent(nums, k):
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    ranked = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    return ranked[:k]
```

**Time:** O(n log u) where u = unique count · **Space:** O(u)

---

# Problem 5 — Longest Substring Without Repeating Characters

## What it's asking
Longest **contiguous** substring with all unique characters.

## Step-by-step (sliding window)

**Step 1 — Window = `[start .. i]` inclusive**
Expand `i` right each iteration. Shrink `start` when duplicate found.

**Step 2 — Track last index of each character**
```python
last = {}   # char -> most recent index
```

**Step 3 — At index i with character ch**
- If `ch` was seen at `last[ch]` **and** `last[ch] >= start`: duplicate inside window → move start to `last[ch] + 1`
- Set `last[ch] = i`
- Update `best = max(best, i - start + 1)`

**Why `last[ch] >= start`?** Old occurrence **outside** current window doesn't count.

## Dry-run: `"abcabcbb"`

| i | ch | start | window | best |
|---|-----|-------|--------|------|
| 0 | a | 0 | a | 1 |
| 1 | b | 0 | ab | 2 |
| 2 | c | 0 | abc | 3 |
| 3 | a | 1 | bca | 3 |
| ... | | | | 3 |

## Solution

```python
def length_of_longest_substring(s):
    last = {}
    start = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best
```

**Time:** O(n) · **Space:** O(min(n, alphabet))

## Common mistakes
- Moving start to `last[ch]` instead of `last[ch] + 1`
- Not checking `last[ch] >= start`

---

# Problem 6 — Two Sum

## What it's asking
Two indices where `nums[i] + nums[j] == target`. Exactly one answer.

## Step-by-step

**Step 1 — Brute force:** double loop O(n²) — say it, then improve.

**Step 2 — One pass hash map**
For each value `v` at index `i`, you need `need = target - v`.
If `need` is already in map → return `[seen[need], i]`.
Else store `seen[v] = i`.

**Order matters:** Check **before** insert (so you don't use same index twice).

## Dry-run: `[2,7,11,15], target=9`

| i | v | need | seen before | action |
|---|-----|------|-------------|--------|
| 0 | 2 | 7 | {} | seen={2:0} |
| 1 | 7 | 2 | {2:0} | 2 in seen → return [0,1] |

## Solution

```python
def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        need = target - v
        if need in seen:
            return [seen[need], i]
        seen[v] = i
    return []
```

**Time:** O(n) · **Space:** O(n)

---

# Problem 7 — Maximum Subarray (Kadane)

## What it's asking
Largest sum of any contiguous subarray.

## Step-by-step

**Step 1 — Key insight**
At each position, either extend the previous subarray or start fresh at current element.

**Step 2 — Two variables**
- `cur` = best sum ending **at current index**
- `best` = best sum anywhere

**Step 3 — Recurrence**
```python
cur = max(x, cur + x)   # extend or restart
best = max(best, cur)
```

## Dry-run: `[-2,1,-3,4,-1,2,1,-5,4]`

| x | cur (after) | best |
|---|-------------|------|
| -2 | -2 | -2 |
| 1 | 1 | 1 |
| -3 | -2 | 1 |
| 4 | 4 | 4 |
| -1 | 3 | 4 |
| 2 | 5 | 5 |
| 1 | 6 | **6** |

## Solution

```python
def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

**Time:** O(n) · **Space:** O(1)

## Common mistakes
- Initializing best to 0 when all numbers are negative (use `nums[0]`)

---

# Problem 8 — Product of Array Except Self

## What it's asking
`output[i]` = product of all elements **except** `nums[i]`. No division. O(n).

## Step-by-step

**Step 1 — Observe**
Answer at i = (product of everything left of i) × (product of everything right of i).

**Step 2 — Pass 1 (left products)**
```python
out = [1] * n
prefix = 1
for i in range(n):
    out[i] = prefix      # product before i
    prefix *= nums[i]
```

**Step 3 — Pass 2 (right products)**
```python
suffix = 1
for i in range(n-1, -1, -1):
    out[i] *= suffix
    suffix *= nums[i]
```

## Dry-run: `[1,2,3,4]`

After pass 1: out = [1, 1, 2, 6]  (prefix products)  
After pass 2: out = [24, 12, 8, 6]

## Solution

```python
def product_except_self(nums):
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

**Time:** O(n) · **Space:** O(1) excluding output

---

# Problem 9 — Valid Anagram

## What it's asking
Same letters, same counts?

## Step-by-step

**Step 1 — Quick fail:** different lengths → False

**Step 2 — Count letters in s, subtract for t**
```python
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1
for ch in t:
    if ch not in counts:
        return False
    counts[ch] -= 1
    if counts[ch] < 0:
        return False
return True
```

**Shortcut:** `sorted(s) == sorted(t)` (O(n log n) but fine for interview)

## Solution (sort)

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

## Solution (count)

```python
def is_anagram(s, t):
    if len(s) != len(t):
        return False
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        counts[ch] = counts.get(ch, 0) - 1
        if counts[ch] < 0:
            return False
    return True
```

---

# Problem 10 — Longest Repeating Character Replacement

## What it's asking
Change at most `k` chars so a substring becomes all one letter. Return max length.

## Step-by-step

**Step 1 — Window `[start..end]` is valid if:**
```
window_size - count_of_most_frequent_char_in_window <= k
```
Everything else in the window can be "fixed" with replacements.

**Step 2 — Expand end, shrink start when invalid**
```python
while (end - start + 1) - max_freq > k:
    counts[s[start]] -= 1
    start += 1
```

**Step 3 — Track `max_freq`** = highest count of any single char in current window.

## Dry-run: `"AABABBA", k=1`

Best window often `"AABA"` or similar → length 4.

## Solution

```python
def character_replacement(s, k):
    counts = {}
    start = 0
    max_freq = 0
    best = 0
    for end, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        max_freq = max(max_freq, counts[ch])
        while (end - start + 1) - max_freq > k:
            counts[s[start]] -= 1
            start += 1
        best = max(best, end - start + 1)
    return best
```

**Time:** O(n) · **Space:** O(26)

---

# Problem 11 — Meeting Rooms II

## What it's asking
Minimum rooms so no meetings overlap.

## Step-by-step (two-pointer on sorted starts/ends)

**Step 1 — Separate and sort**
```python
starts = sorted(i[0] for i in intervals)
ends = sorted(i[1] for i in intervals)
```

**Step 2 — Simulate timeline**
- If next meeting **starts** before next meeting **ends** → need new room
- Else → a room freed up → reuse it

**Step 3 — Track max concurrent rooms**

```python
rooms = 0
needed = 0
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

## Dry-run: `[[0,30],[5,10],[15,20]]`

starts = [0,5,15], ends = [10,20,30]
- 0 < 10 → rooms=1
- 5 < 10 → rooms=2 (peak)
- 15 < 20 → rooms=2
- etc.

## Solution

```python
def min_meeting_rooms(intervals):
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

**Time:** O(n log n)

---

# Problem 12 — Subarray Sum Equals K

## What it's asking
**Count** subarrays with sum exactly k. Array can have **negatives** → sliding window fails.

## Step-by-step (prefix sum + dict)

**Step 1 — Prefix sum**
`prefix[j]` = sum of nums[0..j].  
Subarray sum from i+1 to j = `prefix[j] - prefix[i]`.

**Step 2 — Want `prefix[j] - prefix[i] = k`**
→ look for `prefix[i] = prefix[j] - k` in past counts.

**Step 3 — Algorithm**
```python
counts = {0: 1}   # empty prefix before start
prefix = 0
total = 0
for x in nums:
    prefix += x
    total += counts.get(prefix - k, 0)
    counts[prefix] = counts.get(prefix, 0) + 1
return total
```

**Why counts[0]=1?** Subarray starting at index 0 has prefix[j] = k.

## Dry-run: `[1,1,1], k=2`

| x | prefix | want prefix-k= | counts before | add to total |
|---|--------|----------------|---------------|--------------|
| 1 | 1 | -1 | {0:1} | 0 |
| 1 | 2 | 0 | {0:1,1:1} | 1 |
| 1 | 3 | 1 | {0:1,1:1,2:1} | 1 |

Total = 2 ✓

## Solution

```python
def subarray_sum(nums, k):
    counts = {0: 1}
    prefix = 0
    total = 0
    for x in nums:
        prefix += x
        total += counts.get(prefix - k, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return total
```

**Time:** O(n) · **Space:** O(n)

---

# Problem 13 — Contains Duplicate

## What it's asking
Any value twice?

## Step-by-step

**Option A — Set while iterating**
```python
seen = set()
for x in nums:
    if x in seen:
        return True
    seen.add(x)
return False
```

**Option B — One liner**
```python
return len(nums) != len(set(nums))
```

## Solution

```python
def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

**Time:** O(n) · **Space:** O(n)

---

# Problem 14 — Valid Palindrome

## What it's asking
Ignore non-alphanumeric, ignore case, check palindrome.

## Step-by-step

**Step 1 — Clean string**
```python
clean = []
for ch in s:
    if ch.isalnum():
        clean.append(ch.lower())
```

**Step 2 — Compare to reverse**
```python
return clean == clean[::-1]
```

**Alternative — two pointers (O(1) extra space)**
```python
left, right = 0, len(s) - 1
while left < right:
    while left < right and not s[left].isalnum():
        left += 1
    while left < right and not s[right].isalnum():
        right -= 1
    if s[left].lower() != s[right].lower():
        return False
    left += 1
    right -= 1
return True
```

## Solution (clean + reverse)

```python
def is_palindrome(s):
    clean = [ch.lower() for ch in s if ch.isalnum()]
    return clean == clean[::-1]
```

---

# Problem 15 — Best Time to Buy and Sell Stock

## What it's asking
One buy, one sell, max profit. Can't sell before buy.

## Step-by-step

**Step 1 — Track lowest price seen so far** (`low`)

**Step 2 — At each price, profit if sold today = `price - low`**

**Step 3 — Update `best = max(best, price - low)` then `low = min(low, price)`**

## Dry-run: `[7,1,5,3,6,4]`

| price | low | profit today | best |
|-------|-----|--------------|------|
| 7 | 7 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 5 | 1 | 4 | 4 |
| 3 | 1 | 2 | 4 |
| 6 | 1 | **5** | **5** |

## Solution

```python
def max_profit(prices):
    if not prices:
        return 0
    low = prices[0]
    best = 0
    for p in prices[1:]:
        best = max(best, p - low)
        low = min(low, p)
    return best
```

**Time:** O(n) · **Space:** O(1)

---

# Problem 16 — Longest Consecutive Sequence

## What it's asking
Longest run like 1,2,3,4 in **unsorted** array. Must be O(n).

## Step-by-step

**Step 1 — Put all in set** for O(1) lookup.

**Step 2 — Only start counting from sequence beginnings**
If `n-1` is in set, `n` is NOT the start of a sequence — skip it.

**Step 3 — Walk up from each start**
```python
length = 1
while n + length in num_set:
    length += 1
best = max(best, length)
```

## Dry-run: `[100,4,200,1,3,2]`

Set = {100,4,200,1,3,2}  
Start at 1 (0 not in set): 1,2,3,4 → length 4  
100, 200: length 1 each  
Best = 4

## Solution

```python
def longest_consecutive(nums):
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

**Time:** O(n) — each number visited at most twice

## Common mistakes
- Sorting (O(n log n) — fails requirement)
- Counting from every element without skipping non-starts (still works but slower)

---

# Problem 17 — Permutation in String

## What it's asking
Does `s2` contain a **contiguous** substring that is a permutation of `s1`? Same length, same char counts.

## Step-by-step (fixed-size sliding window)

**Step 1 — If len(s1) > len(s2):** False

**Step 2 — Count chars needed from s1**
```python
need = {}
for ch in s1:
    need[ch] = need.get(ch, 0) + 1
required = len(need)   # number of distinct chars
```

**Step 3 — Slide window of size len(s1) over s2**
Track `window` counts and `formed` = how many chars have matching count to `need`.

**Step 4 — When window too big, shrink from left**

**Step 5 — If `formed == required`, return True**

## Solution

```python
def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    need = {}
    for ch in s1:
        need[ch] = need.get(ch, 0) + 1

    window = {}
    required = len(need)
    formed = 0
    left = 0

    for right, ch in enumerate(s2):
        window[ch] = window.get(ch, 0) + 1
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

**Time:** O(n) · **Space:** O(26)

---

# Interview day script (say this every problem)

1. **Restate:** "So I need to return … given …"
2. **Examples:** Walk through provided example
3. **Edge cases:** empty, single element, duplicates, negatives
4. **Brute force:** Name it + complexity
5. **Optimize:** Name pattern ("hash map", "sliding window", …)
6. **Code:** Talk while writing
7. **Test:** Dry-run one tricky case
8. **Complexity:** Time and space

---

# Quick reference — full solutions (copy after you try)

All solutions also in [python_drill.py](python_drill.py). Test with:

```bash
python3 sofi-prep/python_practice_stubs.py --problem N
python3 sofi-prep/python_practice_stubs.py --all
```

| # | Function | Pattern | Time |
|---|----------|---------|------|
| 1 | longest_increasing_run | single pass | O(n) |
| 2 | group_anagrams | hash bucket | O(n·k log k) |
| 3 | merge_intervals | sort + merge | O(n log n) |
| 4 | top_k_frequent | count + sort | O(n log u) |
| 5 | length_of_longest_substring | sliding window | O(n) |
| 6 | two_sum | hash map | O(n) |
| 7 | max_subarray | Kadane | O(n) |
| 8 | product_except_self | prefix/suffix | O(n) |
| 9 | is_anagram | count/sort | O(n) |
| 10 | character_replacement | sliding window | O(n) |
| 11 | min_meeting_rooms | sort + sweep | O(n log n) |
| 12 | subarray_sum | prefix + dict | O(n) |
| 13 | contains_duplicate | set | O(n) |
| 14 | is_palindrome | two pointers | O(n) |
| 15 | max_profit | track min | O(n) |
| 16 | longest_consecutive | set + start | O(n) |
| 17 | check_inclusion | fixed window | O(n) |

---

# Night-before checklist

- [ ] Can write **two_sum** and **length_of_longest_substring** from memory
- [ ] Can explain **Kadane** in one sentence
- [ ] Know when sliding window **fails** (problem 12 — negatives)
- [ ] Know **prefix sum dict** template for subarray sum
- [ ] Run `--all` once; fix any red tests
- [ ] Disable Cursor Tab during mock

You’ve got this.
