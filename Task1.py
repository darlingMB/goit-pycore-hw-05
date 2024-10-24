# from functools import lru_cache


def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# @lru_cache(128)
# def lru_fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return lru_fibonacci(n - 1) + lru_fibonacci(n - 2)


def main():
    result = caching_fibonacci()
    print(result(15))


if __name__ == '__main__':
    main()