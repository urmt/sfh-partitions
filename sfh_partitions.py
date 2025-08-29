"""
partitions.py
Mathematical utilities for the Sentience-Field Hypothesis (SFH)
Hardy–Ramanujan partition function implementations.

Implements:
- Exact integer partition counts via dynamic programming
- Hardy–Ramanujan asymptotic approximation
- Ramanujan congruences (forbidden configurations)
"""

import math
from functools import lru_cache


# -----------------------------
# 1. Exact integer partitions
# -----------------------------
@lru_cache(maxsize=None)
def partition_exact(n: int) -> int:
    """
    Returns the exact number of integer partitions of n
    using Euler’s recurrence (pentagonal number theorem).
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    total = 0
    k = 1
    while True:
        pent1 = k * (3 * k - 1) // 2
        pent2 = k * (3 * k + 1) // 2
        if pent1 > n:
            break
        sign = -1 if (k % 2 == 0) else 1
        total += sign * partition_exact(n - pent1)
        if pent2 <= n:
            total += sign * partition_exact(n - pent2)
        k += 1
    return total


# -----------------------------
# 2. Hardy–Ramanujan asymptotic
# -----------------------------
def partition_asymptotic(n: int) -> float:
    """
    Returns the Hardy–Ramanujan asymptotic approximation for p(n).
    p(n) ~ (1 / (4n√3)) * exp(pi * sqrt(2n/3))
    """
    if n <= 0:
        return 0.0
    return (1 / (4 * n * math.sqrt(3))) * math.exp(math.pi * math.sqrt(2 * n / 3))


# -----------------------------
# 3. Ramanujan congruences
# -----------------------------
def is_forbidden_configuration(n: int) -> bool:
    """
    Check whether n falls into Ramanujan's congruence forbidden forms:
    - p(5k+4) ≡ 0 (mod 5)
    - p(7k+5) ≡ 0 (mod 7)
    - p(11k+6) ≡ 0 (mod 11)

    Returns True if the configuration is forbidden.
    """
    if n % 5 == 4:
        return True
    if n % 7 == 5:
        return True
    if n % 11 == 6:
        return True
    return False


# -----------------------------
# 4. Utility wrapper
# -----------------------------
def partition_info(n: int) -> dict:
    """
    Returns a dictionary summarizing:
    - exact partition number
    - asymptotic approximation
    - forbidden configuration status
    """
    return {
        "n": n,
        "exact": partition_exact(n),
        "asymptotic": partition_asymptotic(n),
        "forbidden": is_forbidden_configuration(n),
    }


if __name__ == "__main__":
    # Demo run
    for Q in [10, 50, 100]:
        print(partition_info(Q))
