import math
from mpmath import mp

def hardy_ramanujan_partition(Q):
    """Hardy-Ramanujan asymptotic partition function."""
    return (1 / (4 * Q * math.sqrt(3))) * math.exp(math.pi * math.sqrt(2 * Q / 3))

def qualic_partition(Q, C_weight=0.5):
    """
    Distribute qualic energy Q into coherence (C) and fertility (F).
    Returns partition probabilities.
    """
    C = int(Q * C_weight)
    F = Q - C
    total = hardy_ramanujan_partition(Q)
    return {
        "Q_total": Q,
        "C": C,
        "F": F,
        "partition_prob": hardy_ramanujan_partition(Q) / total
    }

if __name__ == "__main__":
    for Q in range(10, 101, 10):
        print(qualic_partition(Q))
