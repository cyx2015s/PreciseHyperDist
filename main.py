from fractions import Fraction as Frc


def fac(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def comb(n, m):
    return fac(n) // fac(m) // fac(n - m)


def hyper(n, N, M, k):
    return Frc(comb(M, k) * comb(N - M, n - k), comb(N, n))

