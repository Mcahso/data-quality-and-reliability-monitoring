"""
SoFi Python interview — practice stubs (solve yourself, then check python_drill.py).

Run tests:  python3 sofi-prep/python_practice_stubs.py --all
One problem: python3 sofi-prep/python_practice_stubs.py --problem 5
"""

from __future__ import annotations

import argparse
from typing import Callable


# --- 1. Longest contiguous strictly increasing run ---


def longest_increasing_run(nums: list[int]) -> int:
    raise NotImplementedError


# --- 2. Group Anagrams (LC 49) ---


def group_anagrams(strs: list[str]) -> list[list[str]]:
    raise NotImplementedError


# --- 3. Merge Intervals (LC 56) ---


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError


# --- 4. Top K Frequent (LC 347) ---


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError


# --- 5. Longest Substring Without Repeating (LC 3) ---


def length_of_longest_substring(s: str) -> int:
    raise NotImplementedError


# --- 6. Two Sum (LC 1) ---


def two_sum(nums: list[int], target: int) -> list[int]:
    raise NotImplementedError


# --- 7. Maximum Subarray (LC 53) ---


def max_subarray(nums: list[int]) -> int:
    raise NotImplementedError


# --- 8. Product Except Self (LC 238) ---


def product_except_self(nums: list[int]) -> list[int]:
    raise NotImplementedError


# --- 9. Valid Anagram (LC 242) ---


def is_anagram(s: str, t: str) -> bool:
    raise NotImplementedError


# --- 10. Longest Repeating Character Replacement (LC 424) ---


def character_replacement(s: str, k: int) -> int:
    raise NotImplementedError


# --- 11. Meeting Rooms II (LC 253) ---


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    raise NotImplementedError


# --- 12. Subarray Sum Equals K (LC 560) ---


def subarray_sum(nums: list[int], k: int) -> int:
    raise NotImplementedError


# --- 13. Contains Duplicate (LC 217) ---


def contains_duplicate(nums: list[int]) -> bool:
    raise NotImplementedError


# --- 14. Valid Palindrome (LC 125) ---


def is_palindrome(s: str) -> bool:
    raise NotImplementedError


# --- 15. Best Time to Buy and Sell Stock (LC 121) ---


def max_profit(prices: list[int]) -> int:
    raise NotImplementedError


# --- 16. Longest Consecutive Sequence (LC 128) ---


def longest_consecutive(nums: list[int]) -> int:
    raise NotImplementedError


# --- 17. Permutation in String (LC 567) ---


def check_inclusion(s1: str, s2: str) -> bool:
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=int, help="Run tests for problem 1-17")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.problem:
        name, fn, cases = PROBLEMS[args.problem - 1]
        print(f"=== {args.problem}. {name} ===")
        _check(name, fn, cases)
        return

    if args.all:
        for i, (name, fn, cases) in enumerate(PROBLEMS, 1):
            print(f"=== {i}. {name} ===")
            _check(name, fn, cases)
        return

    print("SoFi Python practice stubs — implement functions in this file.")
    print("See 09-python-leetcode-questions.md for full problem statements.\n")
    for i, (name, _, _) in enumerate(PROBLEMS, 1):
        print(f"  {i:2}. {name}")
    print("\nUsage: python3 sofi-prep/python_practice_stubs.py --problem 1")


if __name__ == "__main__":
    main()
