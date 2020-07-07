import pytest


def findPrimes(n):
    """
    Algo based on Sieve of Eratosthenes

    :param n: int
    :return: list of calculated prime numbers, that are found in (1,n]

    """
    prime = [False] * 2 + [True] * n

    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 2, p):
                prime[i] = False
        p += 1

    res = [p for p in range(2, n+1) if prime[p]]
    return res


def solve(A, B):
    """
    :param A: list
    :param B: list
    :return: list

    time complexity: O(A * B * F * log(log(F) )
    A - number of elements in seq A
    B - number of elements in seq B
    F - the highest frequency of a number that is both present in B and A

    space complexity: O(A * K * F )
    A - number of elements in A, without duplicates
    K - number of elements that are both in A and B
    F - the highest frequency of a number that is both present in B and A (used by findPrimes func)
    """

    A_set = set(A)              # helper hash set
    B_freq = {}                 # helper hash map
    found_primes = set()        # the helper hash set containing primes
    # the highest frequency of a number that is both present in B and A
    B_max_freq = 0
    C = []                      # result

    for n in B:
        if n not in A_set:
            pass
        elif n in B_freq:
            B_freq[n] += 1
            B_max_freq = max(B_max_freq, B_freq[n])
        else:
            B_freq[n] = 1

    found_primes = set(findPrimes(B_max_freq))

    def check(n):
        """
        Checks if given n is in B sequence, p times, where p is any prime number
        :param n:
        :return: bool
        """
        return True if B_freq.get(n, None) in found_primes else False

    for num in A:
        if not check(num):
            C.append(num)

    return C

# @pytest.mark.skip
@pytest.mark.parametrize('A, B, C',
                         [
                             ([2, 3, 9, 2, 5, 1, 3, 7, 10], [2, 1, 3, 4, 3, 10,
                                                             6, 6, 1, 7, 10, 10, 10], [2, 9, 2, 5, 7, 10]),
                             ([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1], []),
                             ([-21, 0, -1], [0, -1, 0, 3, 45, -33], [-21, -1]),
                             ([1], [2, 2, 2, 3, 3, 3, 3, 3], [1]),
                             ([5, 4, 3, 2, 1], [3, 4, 3, 5, 4, 0,
                                                3, 5, 3, 5, 3, 4, 3, 3], [2, 1]),

                             # A bunch of edge cases
                             ([2, 3, 9, 2, 5, 1, 3, 7, 10], [],
                              [2, 3, 9, 2, 5, 1, 3, 7, 10]),
                             ([], [2, 1, 3, 4, 3, 10, 6, 6, 1, 7, 10, 10, 10], []),
                             ([], [], [])
                         ]
                         )
def test_solve(A, B, C):
    assert solve(A, B) == C

# @pytest.mark.skip
@pytest.mark.parametrize('n, primeList',
                         [
                             (10, [2, 3, 5, 7]),
                             (4,  [2, 3]),
                             (0,  []),
                             (1,  []),
                             (3,  [2, 3]),
                             (-3, []),
                             (7, [2, 3, 5, 7]),
                             (100, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                    41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]),
                             (1000, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                                     449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])
                         ]
                         )
def test_findPrimes(n, primeList):
    assert findPrimes(n) == primeList
