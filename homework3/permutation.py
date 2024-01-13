def perm(n):
    def permNext(n, p, used):
        if len(p) == n:
            yield list(p)
        else:
            for x in range(n):
                if not used[x]:
                    p.append(x)
                    used[x] = True
                    yield from permNext(n, p, used)
                    used[x] = False
                    p.pop()

    return permNext(n, [], [False] * n)


for p in perm(3):
    print(p)
