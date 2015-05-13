from itertools import groupby, imap
from prime_decomposition import decompose


def decompose_me(n):
    return imap(
        lambda (k, v): (k, reduce(lambda x, y: x+1, v, 0)),
        groupby(
            decompose(n)
        )
    )


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in xrange(1, int(n**0.5) + 1) if n % i == 0)))


def d_me(n):
    s = 1
    for fac, num in decompose_me(n):
        s *= (fac**(num+1) - 1) / (fac - 1)
    return s


def d(n):
    return sum(factors(n))


def dsum(n, func):
    s = 0
    for i in xrange(1, n+1):
        s += func(i)
    return s


def main():
    print list(decompose_me(1000))
    print factors(1000)
    assert d_me(1000) == d(1000)

    import time
 
    for fn in [d, d_me]:
        start = time.time()
        print dsum(1000000, fn)
        print "=> {:.2f}s".format( time.time()-start )


if __name__ == '__main__':
    main()