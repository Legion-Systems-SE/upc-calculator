"""
Tension — digit-sequence curvature operators.

Encodes any real number as a digit sequence, computes first and second
differences (discrete velocity and acceleration), and provides dot
product and tension test operations for comparing digit curvature
between two numbers.

This is a minimal extraction of the operators used by the UPC test
suite.  The full tension differential engine lives in the Resonant
Field Engine repository.

Authors: Mattias Hammarsten (framework), Claude/Anthropic (implementation)
"""

from typing import Optional


def encode(value, length: Optional[int] = None) -> list[int]:
    """Extract significant digits from a number.

    For integers: returns all digits.
    For reals (pass as string to preserve precision): strips the
    decimal point and returns significant digits.

    If length is specified, truncates or zero-pads to that length.

    >>> encode('3.14159', 5)
    [3, 1, 4, 1, 5]
    >>> encode(299792458)
    [2, 9, 9, 7, 9, 2, 4, 5, 8]
    >>> encode('0.00729', 4)
    [7, 2, 9, 0]
    """
    if isinstance(value, int):
        digits = [int(d) for d in str(abs(value))]
    elif isinstance(value, str):
        cleaned = value.lstrip("-").replace(".", "")
        if value.startswith("0.") or value.startswith("-0."):
            cleaned = cleaned.lstrip("0")
        digits = [int(d) for d in cleaned]
    elif isinstance(value, float):
        return encode(repr(value), length)
    else:
        raise TypeError(f"unsupported type: {type(value)}")

    if length is not None:
        digits = digits[:length]
        while len(digits) < length:
            digits.append(0)

    return digits


def delta1(seq: list[int]) -> list[int]:
    """First difference (discrete velocity).

    >>> delta1([3, 1, 4, 1, 5])
    [-2, 3, -3, 4]
    """
    return [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]


def delta2(seq: list[int]) -> list[int]:
    """Second difference (discrete acceleration / curvature).

    >>> delta2([3, 1, 4, 1, 5])
    [5, -6, 7]
    """
    d1 = delta1(seq)
    return [d1[i + 1] - d1[i] for i in range(len(d1) - 1)]


def dot(d2_a: list[int], d2_b: list[int]) -> Optional[int]:
    """Dot product of two second-difference sequences.

    Returns None if lengths differ.

    >>> dot([5, -6, 7], [1, 2, -1])
    [-5 + (-12) + (-7)] = None  # different example
    >>> dot([1, 2], [3, 4])
    11
    """
    if len(d2_a) != len(d2_b):
        return None
    return sum(a * b for a, b in zip(d2_a, d2_b))


def tension_of(v: int) -> Optional[int]:
    """Second difference of a 3-digit integer's digits.

    For |v| in [100, 999], extracts digits d0 d1 d2 and returns
    d0 - 2*d1 + d2.  This is the discrete Laplacian of the 3-element
    sequence [d0, d1, d2].

    Returns None if |v| is not a 3-digit number.

    D2 = 0 means the digits form an arithmetic progression ("tonic").

    >>> tension_of(123)   # 1 - 2*2 + 3 = 0
    0
    >>> tension_of(135)   # 1 - 2*3 + 5 = 0
    0
    >>> tension_of(222)   # 2 - 2*2 + 2 = 0
    0
    >>> tension_of(499)   # 4 - 2*9 + 9 = -5
    -5
    """
    if abs(v) < 100 or abs(v) >= 1000:
        return None
    d = [int(x) for x in str(abs(v))]
    return d[0] - 2 * d[1] + d[2]
