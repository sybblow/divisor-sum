from itertools import groupby, imap
from prime_decomposition import decompose


def decompose_me(n):
    return imap(
        lambda (k, v): (k, len(list(v))),
        groupby(
            decompose(n)
        )
    )


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def d(n):
    s = 1
    for fac, num in decompose_me(n):
        s *= (fac**(num+1) - 1) / (fac - 1)
    return s


def dsum(n):
    s = 0
    for i in xrange(1, n):
        s += d(i)
    return s


def main():
    print list(decompose_me(1000))
    print factors(1000)
    assert sum(factors(1000)) == d(1000)

    print dsum(1000)


if __name__ == '__main__':
    main()