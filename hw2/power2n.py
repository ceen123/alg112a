# 方法 1
n = 5
result = power2n(n)
print(f"2^{n} = {result}")



# 方法 2a：用遞迴
def power2n(n):
    if n == 0:
        return 1
    else:
        return 2 * power2n(n - 1)
n = 5
result = power2n(n)
print(f"2^{n} = {result}")



# 方法2b：用遞迴
def power2n(n):
    if n == 0:
        return 1
    else:
        return 2 * power2n(n - 1)
n = 5
result = power2n(n)
print(f"2^{n} = {result}")



# 方法 3：用遞迴+查表
def power2n(n, a={}):
    if n == 0:
        return 1
    elif n in a:
        return a[n]
    else:
        result = 2 * power2n(n - 1, a)
        a[n] = result
        return result
n = 5
result = power2n(n)
print(f"2^{n} = {result}")
