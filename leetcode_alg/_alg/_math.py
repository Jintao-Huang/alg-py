# Author: Jintao Huang
# Email: huangjintao@mail.ustc.edu.cn
# Date:

from .._types import *


def fast_pow(x: int, y: int, mod: int) -> int:
    res = 1
    while y > 0:
        if y % 2 == 0:
            y //= 2
            x *= x
            x %= mod
        else:
            y -= 1
            res *= x
            res %= mod
    return res


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def find_primes(n: int) -> bytearray:
    """[2..n]的质数. 
    return: is_prime, len=n+1. 
        e.g. is_prime[0..1]=False, is_prime[2]=True 
    """
    assert n >= 2
    is_prime = bytearray([True])
    is_prime *= (n+1)
    is_prime[0], is_prime[1] = False, False
    #
    for x in range(2, int(sqrt(n))+1):
        if is_prime[x] == False:
            continue
        is_prime[x*x:n+1:x] = bytearray([False]) * ceil((n+1-x*x)/x)
    return is_prime
