"""
SoFi Python interview — practice stubs (solve yourself, then check python_drill.py).

Run tests:   python3 sofi-prep/python_practice_stubs.py --problem 5
Show prompt: python3 sofi-prep/python_practice_stubs.py --prompt 5
All tests:   python3 sofi-prep/python_practice_stubs.py --all

Hints + hidden answers: python_walkthrough.md
"""

from __future__ import annotations

import argparse
import textwrap
from typing import Callable


def longest_increasing_run(nums: list[int]) -> int:
    """Problem 1 — Longest Contiguous Increasing Run

    Given an integer array nums, return the length of the longest contiguous
    strictly increasing subarray. Each element must be greater than the previous
    (equal values do not extend the run).

    Examples:
        >>> longest_increasing_run([2, 3, 5, 4, 6, 7, 8])
        4
        >>> longest_increasing_run([5, 4, 3])
        1
        >>> longest_increasing_run([])
        0

    Constraints:
        - 0 <= len(nums) <= 10^5
        - -10^9 <= nums[i] <= 10^9
    """
    if not nums:
        return 0
    start = 0
    best = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            best = max(best, i - start + 1)
        else:
            start = i
    return best

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Problem 2 — Group Anagrams (LC 49)

    Given an array of strings, group the anagrams together. Return groups in
    any order.

    Example:
        Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

    Constraints:
        - 1 <= len(strs) <= 10^4
        - 0 <= len(strs[i]) <= 100
        - strs[i] consists of lowercase English letters
    """
    raise NotImplementedError


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Problem 3 — Merge Intervals (LC 56)

    Given intervals[i] = [start_i, end_i], merge all overlapping intervals.

    Examples:
        Input:  [[1, 3], [2, 6], [8, 10], [15, 18]]
        Output: [[1, 6], [8, 10], [15, 18]]

        Input:  [[1, 4], [4, 5]]
        Output: [[1, 5]]

    Constraints:
        - 1 <= len(intervals) <= 10^4
        - 0 <= start_i <= end_i <= 10^4
    """
    raise NotImplementedError


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Problem 4 — Top K Frequent Elements (LC 347)

    Return the k most frequent elements. Any order is OK. Answer is unique.

    Example:
        Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
        Output: [1, 2]

    Constraints:
        - 1 <= len(nums) <= 10^5
        - -10^3 <= nums[i] <= 10^3
        - 1 <= k <= number of unique elements
    """
    raise NotImplementedError


def length_of_longest_substring(s: str) -> int:
    """Problem 5 — Longest Substring Without Repeating Characters (LC 3)

    Return the length of the longest substring without repeating characters.

    Examples:
        Input:  s = "abcabcbb"  ->  3
        Input:  s = "bbbbb"     ->  1
        Input:  s = ""          ->  0

    Constraints:
        - 0 <= len(s) <= 5 * 10^4
    """
    raise NotImplementedError


def two_sum(nums: list[int], target: int) -> list[int]:
    """Problem 6 — Two Sum (LC 1)

    Return indices of the two numbers that add up to target. Exactly one
    solution exists; do not use the same element twice.

    Example:
        Input:  nums = [2, 7, 11, 15], target = 9
        Output: [0, 1]

    Constraints:
        - 2 <= len(nums) <= 10^4
        - Exactly one valid answer exists
    """
    raise NotImplementedError


def max_subarray(nums: list[int]) -> int:
    """Problem 7 — Maximum Subarray (LC 53)

    Find the contiguous subarray with the largest sum and return that sum.

    Examples:
        Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  ->  6  ([4,-1,2,1])
        Input:  nums = [1]  ->  1

    Constraints:
        - 1 <= len(nums) <= 10^5
        - -10^4 <= nums[i] <= 10^4
    """
    raise NotImplementedError


def product_except_self(nums: list[int]) -> list[int]:
    """Problem 8 — Product of Array Except Self (LC 238)

    Return answer[i] = product of all nums except nums[i]. O(n) time, no division.

    Example:
        Input:  nums = [1, 2, 3, 4]
        Output: [24, 12, 8, 6]

    Constraints:
        - 2 <= len(nums) <= 10^5
        - -30 <= nums[i] <= 30
    """
    raise NotImplementedError


def is_anagram(s: str, t: str) -> bool:
    """Problem 9 — Valid Anagram (LC 242)

    Return True if t is an anagram of s.

    Examples:
        Input:  s = "anagram", t = "nagaram"  ->  True
        Input:  s = "rat", t = "car"          ->  False

    Constraints:
        - 1 <= len(s), len(t) <= 5 * 10^4
        - Lowercase English letters only
    """
    raise NotImplementedError


def character_replacement(s: str, k: int) -> int:
    """Problem 10 — Longest Repeating Character Replacement (LC 424)

    Change at most k characters to any uppercase letter. Return the length of
    the longest substring that can be made all one letter.

    Examples:
        Input:  s = "ABAB", k = 2      ->  4
        Input:  s = "AABABBA", k = 1   ->  4

    Constraints:
        - 1 <= len(s) <= 10^5
        - Uppercase English letters
        - 0 <= k <= len(s)
    """
    raise NotImplementedError


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    """Problem 11 — Meeting Rooms II (LC 253)

    Return the minimum number of conference rooms required.

    Examples:
        Input:  [[0, 30], [5, 10], [15, 20]]  ->  2
        Input:  [[7, 10], [2, 4]]              ->  1

    Constraints:
        - 1 <= len(intervals) <= 10^4
        - 0 <= start_i < end_i <= 10^6
    """
    raise NotImplementedError


def subarray_sum(nums: list[int], k: int) -> int:
    """Problem 12 — Subarray Sum Equals K (LC 560)

    Count contiguous subarrays whose sum equals k.

    Examples:
        Input:  nums = [1, 1, 1], k = 2  ->  2
        Input:  nums = [1, 2, 3], k = 3  ->  2  ([1,2] and [3])

    Constraints:
        - 1 <= len(nums) <= 2 * 10^4
        - -10^3 <= nums[i] <= 10^3
    """
    raise NotImplementedError


def contains_duplicate(nums: list[int]) -> bool:
    """Problem 13 — Contains Duplicate (LC 217)

    Return True if any value appears at least twice.

    Examples:
        Input:  [1, 2, 3, 1]  ->  True
        Input:  [1, 2, 3, 4]  ->  False

    Constraints:
        - 1 <= len(nums) <= 10^5
    """
    raise NotImplementedError


def is_palindrome(s: str) -> bool:
    """Problem 14 — Valid Palindrome (LC 125)

    After lowercasing and removing non-alphanumeric chars, check if s reads
    the same forward and backward.

    Examples:
        Input:  "A man, a plan, a canal: Panama"  ->  True
        Input:  "race a car"                       ->  False

    Constraints:
        - 1 <= len(s) <= 2 * 10^5
    """
    raise NotImplementedError


def max_profit(prices: list[int]) -> int:
    """Problem 15 — Best Time to Buy and Sell Stock (LC 121)

    At most one transaction (buy once, sell once). Return max profit, or 0.

    Examples:
        Input:  [7, 1, 5, 3, 6, 4]  ->  5  (buy 1, sell 6)
        Input:  [7, 6, 4, 3, 1]     ->  0

    Constraints:
        - 1 <= len(prices) <= 10^5
        - 0 <= prices[i] <= 10^4
    """
    raise NotImplementedError


def longest_consecutive(nums: list[int]) -> int:
    """Problem 16 — Longest Consecutive Sequence (LC 128)

    Return length of longest consecutive elements sequence. Must run in O(n).

    Examples:
        Input:  [100, 4, 200, 1, 3, 2]  ->  4  ([1,2,3,4])
        Input:  []                       ->  0

    Constraints:
        - 0 <= len(nums) <= 10^5
    """
    raise NotImplementedError


def check_inclusion(s1: str, s2: str) -> bool:
    """Problem 17 — Permutation in String (LC 567)

    Return True if s2 contains a permutation of s1 (same chars, same counts).

    Examples:
        Input:  s1 = "ab", s2 = "eidbaooo"  ->  True  ("ba" is a permutation)
        Input:  s1 = "ab", s2 = "eidboaoo"  ->  False

    Constraints:
        - 1 <= len(s1), len(s2) <= 10^4
        - Lowercase English letters
    """
    raise NotImplementedError


PROBLEMS: list[tuple[str, Callable, list]] = [
    (
        "longest_increasing_run",
        longest_increasing_run,
        [
            ([2, 3, 5, 4, 6, 7, 8], 4),
            ([], 0),
            ([1], 1),
            ([5, 4, 3], 1),
        ],
    ),
    (
        "group_anagrams",
        group_anagrams,
        [
            (["eat", "tea", "tan", "ate", "nat", "bat"], lambda r: len(r) == 3),
        ],
    ),
    (
        "merge_intervals",
        merge_intervals,
        [
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
        ],
    ),
    (
        "top_k_frequent",
        top_k_frequent,
        [
            (([1, 1, 1, 2, 2, 3], 2), {1, 2}),
        ],
    ),
    (
        "length_of_longest_substring",
        length_of_longest_substring,
        [
            ("abcabcbb", 3),
            ("bbbbb", 1),
            ("", 0),
        ],
    ),
    (
        "two_sum",
        two_sum,
        [
            (([2, 7, 11, 15], 9), [0, 1]),
        ],
    ),
    (
        "max_subarray",
        max_subarray,
        [
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),
        ],
    ),
    (
        "product_except_self",
        product_except_self,
        [
            ([1, 2, 3, 4], [24, 12, 8, 6]),
        ],
    ),
    (
        "is_anagram",
        is_anagram,
        [
            (("anagram", "nagaram"), True),
            (("rat", "car"), False),
        ],
    ),
    (
        "character_replacement",
        character_replacement,
        [
            (("ABAB", 2), 4),
            (("AABABBA", 1), 4),
        ],
    ),
    (
        "min_meeting_rooms",
        min_meeting_rooms,
        [
            ([[0, 30], [5, 10], [15, 20]], 2),
            ([[7, 10], [2, 4]], 1),
        ],
    ),
    (
        "subarray_sum",
        subarray_sum,
        [
            (([1, 1, 1], 2), 2),
            (([1, 2, 3], 3), 2),
        ],
    ),
    (
        "contains_duplicate",
        contains_duplicate,
        [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
        ],
    ),
    (
        "is_palindrome",
        is_palindrome,
        [
            ("A man, a plan, a canal: Panama", True),
            ("race a car", False),
        ],
    ),
    (
        "max_profit",
        max_profit,
        [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
        ],
    ),
    (
        "longest_consecutive",
        longest_consecutive,
        [
            ([100, 4, 200, 1, 3, 2], 4),
            ([], 0),
        ],
    ),
    (
        "check_inclusion",
        check_inclusion,
        [
            (("ab", "eidbaooo"), True),
            (("ab", "eidboaoo"), False),
        ],
    ),
]


def _check(name: str, fn: Callable, cases: list) -> None:
    for case in cases:
        if isinstance(case[1], set):
            args, expected = case
            result = fn(*args) if isinstance(args, tuple) else fn(args)
            ok = set(result) == expected
        elif callable(case[1]):
            args, pred = case
            result = fn(args)
            ok = pred(result)
        elif isinstance(case[0], tuple) and not isinstance(case[0][0], list):
            args, expected = case
            result = fn(*args)
            ok = result == expected
        else:
            args, expected = case
            result = fn(args) if not isinstance(args, tuple) else fn(*args)
            ok = result == expected
        status = "OK" if ok else f"FAIL got {result!r}"
        print(f"  {name} {case[0]!r}: {status}")


def _print_prompt(problem_num: int) -> None:
    name, fn, _ = PROBLEMS[problem_num - 1]
    doc = fn.__doc__ or "(no prompt)"
    print(f"=== Problem {problem_num}: {name} ===\n")
    print(textwrap.dedent(doc).strip())
    print()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="SoFi Python practice — prompts are in each function docstring."
    )
    parser.add_argument("--problem", type=int, help="Run tests for problem 1-17")
    parser.add_argument("--prompt", type=int, help="Print prompt for problem 1-17")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.prompt:
        _print_prompt(args.prompt)
        return

    if args.problem:
        name, fn, cases = PROBLEMS[args.problem - 1]
        print(f"=== {args.problem}. {name} ===")
        if fn.__doc__:
            print(textwrap.indent(textwrap.dedent(fn.__doc__).strip(), "  "))
            print()
        _check(name, fn, cases)
        return

    if args.all:
        for i, (name, fn, cases) in enumerate(PROBLEMS, 1):
            print(f"=== {i}. {name} ===")
            _check(name, fn, cases)
        return

    print("SoFi Python practice — prompts are in each function docstring.\n")
    for i, (name, fn, _) in enumerate(PROBLEMS, 1):
        title = (fn.__doc__ or "").split("\n")[0].strip()
        print(f"  {i:2}. {name}  —  {title}")
    print("\nUsage:")
    print("  python3 sofi-prep/python_practice_stubs.py --prompt 1")
    print("  python3 sofi-prep/python_practice_stubs.py --problem 1")


if __name__ == "__main__":
    main()
