def mean(xs):
    return sum(xs) / len(xs)


def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2]


def clamp(x, lo, hi):
    return max(lo, min(hi, x))
