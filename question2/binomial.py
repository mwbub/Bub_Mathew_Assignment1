import matplotlib.pyplot as plt
import numpy as np

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

fig, ax = plt.subplots(1,3)
N = [10,100,1000]
p = 0.25
n = 4
k = 1

for i in range(3):
    x = np.random.random((N[i], n))
    y = (x < p).sum(1)
    s = (y >= k).sum()
    patches, texts, autotexts = ax[i].pie([s, N[i]-s], autopct = '%.1f%%')
    [autotexts[j].set_fontsize(15) for j in range(2)]
    ax[i].set_title('$N = ' + str(N[i]) + '$', fontsize = 15)

fig.subplots_adjust(left = 0, right = 2.1, bottom = 0, top = 1, wspace = 0.1)
fig.suptitle('Fraction of Successes in $N$ Attempts', 
             fontsize = 20, x = 1.05, y = 1.2)
ax[2].legend(labels = ['Successes', 'Failures'])

print('Theoretically, the fraction of successes should be:', bentCoin(p,n,k))