def f(n):
    res = 0
    for i in range(11):
        res += (-n)**i
    return res


def B(xs, i, X):
    res = 0
    ni = 1
    di = 1
    for xj in [x for x in xs if x != xs[i]]:
        ni *= (X-xj)
        di *= (xs[i]-xj)
    res += ni/di
    return res


def L(xs, ys, X):
    res = 0
    for i in range(len(xs)):
        res += B(xs, i, X)*ys[i]
    return res


def answer():
    res = 0
    for i in range(1, 11):
        xs = list(range(1, i+1))
        ys = [f(j) for j in xs]
        res += L(xs, ys, i+1)
    return int(res)


if __name__ == '__main__':
    print(answer())
