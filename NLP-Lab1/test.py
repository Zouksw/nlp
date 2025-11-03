from typing import Final

def fibonacci(n: int) -> int:
    """
    计算第 n 个斐波那契数。

    参数:
        n (int): 需要计算的斐波那契数的索引（从 0 开始）。

    返回:
        int: 第 n 个斐波那契数。

    异常:
        TypeError: 如果 n 不是整数。
        ValueError: 如果 n 是负数。
    """

    # 检查 n 是否为整数
    if not isinstance(n, int):
        raise TypeError("n 必须是整数")
    # 检查 n 是否为非负数
    if n < 0
        raise ValueError("n 必须是非负整数")

    a: Final[int] = 0  # F(0)
    b: Final[int] = 1  # F(1)

    # 处理 n 为 0 或 1 的特殊情况
    if n == 0:
        return a
    if n == 1:
        return b

    # 迭代计算斐波那契数
    prev, curr = a, b
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr