import random
import matplotlib.pyplot as plt

def integral_sum(a, b, n, t, f):
    step = (b - a) / n  
    w = [a + i * step for i in range(n+1)]
    dx = (b - a) / n 
    x_vals = []
    for i in range(n):
        if t == 'left':
            x = w[i]
        elif t == 'right':
            x = w[i+1]
        elif t == 'midpoint':
            x = (w[i] + w[i+1]) / 2 
        elif t == 'random':
            x = random.uniform(w[i], w[i+1])
        x_vals.append(x)
    f_vals = [f(x) * dx for x in x_vals] 
    return sum(f_vals)

def func(x):
    return 2**x

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axs = axs.flatten()

params = [
    {'a': -1, 'b': 2, 'n': 10000, 't': 'left'},
    {'a': -1, 'b': 2, 'n': 10000, 't': 'right'},
    {'a': -1, 'b': 2, 'n': 10000, 't': 'midpoint'},
    {'a': -1, 'b': 2, 'n': 10000, 't': 'random'},
]

for i, param in enumerate(params):
    a, b, n, t = param['a'], param['b'], param['n'], param['t']
    approximation = integral_sum(a, b, n, t, func)
    
    x = [a + i * (b - a) / 1000 for i in range(1001)]
    y = [func(xi) for xi in x]

    axs[i].plot(x, y, label='Function')
    axs[i].axhline(y=0, color='k', linewidth=0.5)
    axs[i].axvline(x=0, color='k', linewidth=0.5)

    for j in range(n):
        step = (b - a) / n
        xi = a + j * step  
        if t == 'left':
            rect = plt.Rectangle((xi, 0), step, func(xi), alpha=0.5, color='orange')
        elif t == 'right':
            rect = plt.Rectangle((xi, 0), step, func(xi + step), alpha=0.5, color='orange')
        elif t == 'random':
            rect = plt.Rectangle((xi, 0), step, func(random.uniform(xi, xi + step)), alpha=0.5, color='orange')
        else:
            rect = plt.Rectangle((xi, 0), step, func(xi + step/2), alpha=0.5, color='orange')   

        axs[i].add_patch(rect)

    axs[i].set_title(f'a={a}, b={b}, n={n}, t={t}, sum={approximation:.5f}')
    axs[i].legend()
fig.savefig('n10000.png')
plt.show()

