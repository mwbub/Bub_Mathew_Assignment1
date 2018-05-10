
def prod(l):
    product = 1
    for n in l:
        product *= n
    return product

def choose(n,k):
    if not (n >= k >= 0):
        raise ValueError('must have n >= k >= 0')
    elif type(n) != int or type(k) != int:
        raise TypeError('n and k must have type int')
    elif k == 0:
        return 1
    else:
        x = range(k+1,n+1)
        y = range(1,n-k+1)
        return prod(x)//prod(y)
    
def bentCoin(p,n,k):
    prob = 0
    for i in range(k,n+1):
        prob += choose(n,i) * p**i * (1-p)**(n-i)
    return prob

