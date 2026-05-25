"""
SoFi Borrow interview — Python drill (LC medium patterns).
Solutions for all 17 problems in 09-python-leetcode-questions.md

Run: python3 sofi-prep/python_drill.py [--warmup | --problem N | --all]
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from typing import Callable


# --- 1. Longest contiguous strictly increasing subsequence length ---


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


# --- 2. Group Anagrams (LC 49) ---


def group_anagrams(strs: list[str]) -> list[list[str]]:
    buckets: dict[tuple[tuple[str, int], ...], list[str]] = defaultdict(list)
    for s in strs:
        key = tuple(sorted(Counter(s).items()))
        buckets[key].append(s)
    return list(buckets.values())


# --- 3. Merge Intervals (LC 56) ---


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


# --- 4. Top K Frequent Elements (LC 347) ---


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    return [x for x, _ in Counter(nums).most_common(k)]


# --- 5. Longest Substring Without Repeating Characters (LC 3) ---


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


# --- 6. Two Sum (LC 1) ---


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, v in enumerate(nums):
        need = target - v
        if need in seen:
            return [seen[need], i]
        seen[v] = i
    return []


# --- 7. Maximum Subarray (LC 53) ---


def max_subarray(nums: list[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


# --- 8. Product of Array Except Self (LC 238) ---


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


# --- 9. Valid Anagram (LC 242) ---


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# --- 10. Longest Repeating Character Replacement (LC 424) ---


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


# --- 11. Meeting Rooms II (LC 253) ---


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


# --- 12. Subarray Sum Equals K (LC 560) ---


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


# --- 13. Contains Duplicate (LC 217) ---


def contains_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))


# --- 14. Valid Palindrome (LC 125) ---


def is_palindrome(s: str) -> bool:
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]


# --- 15. Best Time to Buy and Sell Stock (LC 121) ---


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0
    low = prices[0]
    best = 0
    for p in prices[1:]:
        best = max(best, p - low)
        low = min(low, p)
    return best


# --- 16. Longest Consecutive Sequence (LC 128) ---


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


# --- 17. Permutation in String (LC 567) ---


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


TESTS: list[tuple[str, Callable]] = [
    ("longest_increasing_run", longest_increasing_run),
    ("group_anagrams", group_anagrams),
    ("merge_intervals", merge_intervals),
    ("top_k_frequent", top_k_frequent),
    ("length_of_longest_substring", length_of_longest_substring),
    ("two_sum", two_sum),
    ("max_subarray", max_subarray),
    ("product_except_self", product_except_self),
    ("is_anagram", is_anagram),
    ("character_replacement", character_replacement),
    ("min_meeting_rooms", min_meeting_rooms),
    ("subarray_sum", subarray_sum),
    ("contains_duplicate", contains_duplicate),
    ("is_palindrome", is_palindrome),
    ("max_profit", max_profit),
    ("longest_consecutive", longest_consecutive),
    ("check_inclusion", check_inclusion),
]

CASES: dict[str, list] = {
    "longest_increasing_run": [
        ([2, 3, 5, 4, 6, 7, 8], 4),
        ([1], 1),
        ([5, 4, 3], 1),
        ([], 0),
    ],
    "group_anagrams": [(["eat", "tea", "tan", "ate", "nat", "bat"], 3)],
    "merge_intervals": [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
    ],
    "top_k_frequent": [(([1, 1, 1, 2, 2, 3], 2), {1, 2})],
    "length_of_longest_substring": [("abcabcbb", 3), ("bbbbb", 1), ("", 0)],
    "two_sum": [(([2, 7, 11, 15], 9), [0, 1])],
    "max_subarray": [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1)],
    "product_except_self": [([1, 2, 3, 4], [24, 12, 8, 6])],
    "is_anagram": [(("anagram", "nagaram"), True), (("rat", "car"), False)],
    "character_replacement": [(("ABAB", 2), 4), (("AABABBA", 1), 4)],
    "min_meeting_rooms": [
        ([[0, 30], [5, 10], [15, 20]], 2),
        ([[7, 10], [2, 4]], 1),
    ],
    "subarray_sum": [(([1, 1, 1], 2), 2), (([1, 2, 3], 3), 2)],
    "contains_duplicate": [([1, 2, 3, 1], True), ([1, 2, 3, 4], False)],
    "is_palindrome": [("A man, a plan, a canal: Panama", True), ("race a car", False)],
    "max_profit": [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)],
    "longest_consecutive": [([100, 4, 200, 1, 3, 2], 4), ([], 0)],
    "check_inclusion": [(("ab", "eidbaooo"), True), (("ab", "eidboaoo"), False)],
}


def run_tests(name: str, fn: Callable) -> None:
    for case in CASES[name]:
        if name == "group_anagrams":
            result = fn(case[0])
            ok = len(result) == case[1]
        elif name == "top_k_frequent":
            result = fn(*case[0])
            ok = set(result) == case[1]
        elif isinstance(case[0], tuple) and name in {
            "two_sum",
            "is_anagram",
            "character_replacement",
            "subarray_sum",
            "check_inclusion",
        }:
            result = fn(*case[0])
            ok = result == case[1]
        else:
            result = fn(case[0])
            ok = result == case[1]
        status = "OK" if ok else f"FAIL got {result!r}"
        print(f"  {name} {case[0]!r}: {status}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--warmup", action="store_true", help="Run problem 1 only")
    parser.add_argument("--problem", type=int, help="Run problem 1-17")
    parser.add_argument("--all", action="store_true", help="Run all tests")
    args = parser.parse_args()

    if args.warmup:
        run_tests("longest_increasing_run", longest_increasing_run)
        return

    if args.problem:
        name, fn = TESTS[args.problem - 1]
        print(f"=== {args.problem}. {name} ===")
        run_tests(name, fn)
        return

    if args.all:
        for name, fn in TESTS:
            print(f"=== {name} ===")
            run_tests(name, fn)
        return

    print("SoFi Python drill — 17 problems (see 09-python-leetcode-questions.md):")
    for i, (name, _) in enumerate(TESTS, 1):
        print(f"  {i:2}. {name}")
    print("\nUsage: python3 sofi-prep/python_drill.py --all | --warmup | --problem 3")


if __name__ == "__main__":
    main()
