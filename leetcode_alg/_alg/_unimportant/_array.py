from ..._types import *


def reverse(nums: Union[List[int], bytearray]) -> None:
    # 使用l.reverse(); ba.reverse()
    lo, hi = 0, len(nums)-1
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1


def euclidean_dist(x1: int, y1: int, x2: int, y2: int,
                   square: bool = False) -> float:
    # 使用math.dist
    d1, d2 = x2 - x1, y2 - y1
    res = d1*d1 + d2*d2
    if square:
        return res
    #
    res = sqrt(res)
    return res


def manhattan_dist(x1: int, y1: int, x2: int, y2: int) -> float:
    d1, d2 = x2 - x1, y2 - y1
    return abs(d1) + abs(d2)


def prefix_sum(nums: List[int], initial: Optional[int] = None) -> List[int]:
    """使用itertools.accumulate"""
    res = []
    if initial is not None:
        res.append(initial)
    n = len(nums)
    if n == 0:
        return res
    _start = 0
    if len(res) == 0:
        res.append(nums[0])
        _start = 1
    for i in range(_start, n):
        res.append(res[-1]+nums[i])
    return res