def power2n_1(n):
    return 2 ** n


def power2n_2a(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return power2n_2a(n - 1) + power2n_2a(n - 1)


def power2n_2b(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return 2 * power2n_2b(n - 1)

# 方法 3: Recursion with memoization
dp = [None] * 10000

def power2n_3(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif dp[n] is not None:
        return dp[n]
    else:
        dp[n] = power2n_3(n - 1) + power2n_3(n - 1)
        return dp[n]

# Testing the functions
print(power2n_1(10))
print(power2n_2a(10))
print(power2n_2b(10))
print(power2n_3(10))
