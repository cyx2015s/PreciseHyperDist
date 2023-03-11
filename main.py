import math
import random
from fractions import Fraction as Frc

debug = False
"""
comb(a, b) = comb(a - 1, b) * n // (n - m) = comb(a, b - 1) * (n - m + 1) // m
hyper(n, N, M, k) = Frc(comb(M, k) * comb(N - M, n - k), comb(N, n))
hyper(n + 1, N, M, k) = hyper(n, N, M, k) * Frc((N - M - n + k) * (n + 1), (n + 1 - k) * (N - n))
hyper(n, N + 1, M, k) = hyper(n, N, M, k) * Frc((N + 1 - M) * (N + 1 - n), (N + 1) * (N + 1 - M -n + k))
hyper(n, N, M + 1, k) = hyper(n, N, M, k) * Frc((M + 1) * (N - M - n + k), (M + 1 - k) * (N - M))
hyper(n, N, M, k + 1) = hyper(n, N, M, k) * Frc((M - k) * (n - k), (k + 1) * (N - M - n + k + 1))
"""


def fac(_n):
    res = 1
    for i in range(1, _n + 1):
        res *= i
    return res


def comb(_n, _m):
    return fac(_n) // fac(_m) // fac(_n - _m)


def hyper(_n, _N, _M, _k):
    return Frc(comb(_M, _k) * comb(_N - _M, _n - _k), comb(_N, _n))


def hyper_likelihood(_n, _N, _M, _k):
    ret = [
        Frc(k * (N + 1), M),
        Frc(n * M, k),
        Frc(k * (N + 1), n),
        Frc((n + 1) * (M + 1), (N + 2)),
    ]
    return tuple(ret)


def discretize(_x):
    return {math.floor(_x), math.ceil(_x - 1)}


# ans: list[tuple[Frc, int]] = [(hyper(500, i, 200, 15), i) for i in range(6665, 6669)]
# ans.sort()
# for item in ans:
#     print(item[1], ":", item[0], float(item[0]))
#
# print(float(ans[-1][0] - ans[-2][0]))
# # print(hyper(200, 2000, 200, 15))
#
#
# for k in range(14, 17):
#     for N in range(6666, 6668):
#         res = hyper(500, N, 200, k)
#         print(f"$$P(X={k}|n=200,N={N},M=500)=" + (
#                     "\\frac{%d}{%d}$$\n\n$$" % (res.numerator, res.denominator)) \
#                     + f"\\approx{float(res)}$$\n".replace(
#             "/", "}{"))
# print(comb(3, 1))

# for k in range(5):
#     print(hyper(1, 5, 2, k))

# print(hyper(200, 5000, 500, 20) == hyper(200, 4999, 500, 20))

n = random.randint(10, 15)
N = random.randint(30, 50)
M = random.randint(15, 25)
k = random.randint(5, 10)
args = n, N, M, k
print(args)
for key, item in enumerate(tuple(map(discretize, hyper_likelihood(n, N, M, k)))):
    for t in range(min(item) - 1, max(item) + 2):
        tmp_args = (args[:key] + (t,) + args[key + 1:])
        tmp_ret = hyper(*(args[:key] + (t,) + args[key + 1:]))
        print(tmp_args, tmp_ret, float(tmp_ret))
    print("-" * 10)

if debug:
    print(hyper(n, N, M, k))
    print(hyper(n + 1, N, M, k))
    print(hyper(n, N, M, k) * Frc((N - M - n + k) * (n + 1), (n + 1 - k) * (N - n)))
    print(hyper(n, N + 1, M, k))
    print(hyper(n, N, M, k) * Frc((N + 1 - M) * (N + 1 - n), (N + 1) * (N + 1 - M - n + k)))
    print(hyper(n, N, M + 1, k))
    print(hyper(n, N, M, k) * Frc((M + 1) * (N - M - n + k), (M + 1 - k) * (N - M)))
    print(hyper(n, N, M, k + 1))
    print(hyper(n, N, M, k) * Frc((M - k) * (n - k), (k + 1) * (N - M - n + k + 1)))
