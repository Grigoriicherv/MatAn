import random
import matplotlib.pyplot as plt

# calculates integral sum
def integral_sum(a, b, n, t, f):
    step = (b - a) / n
    w = [a + i * step for i in range(n+1)]
    dx = (b - a) / n
    x_arr = []
    tabl = {
        'left': lambda i: w[i],
        'right': lambda i: w[i+1],
        'midpoint': lambda i: (w[i] + w[i+1]) / 2,
        'random': lambda i: random.uniform(w[i], w[i+1])
    }
    for i in range(n):
        x = tabl.get(t)(i)
        x_arr.append(x)
    f = [f(x) * dx for x in x_arr]
    return sum(f)
# select a, b, n, t, and func
def func(x):
    return 2**x
a, b = -1, 2
n = 10
t = 'right'

k = integral_sum(a, b, n, t, func)
# calculates values of func
x = [a + i * (b - a) / 10000 for i in range(10001)]
y = [func(xi) for xi in x]
# building graph and axes
plt.plot(x, y, label='func')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# adding rectangles
for i in range(n):
    step = (b - a) / n
    xi = a + i * step  
    tabl = {
        'left': lambda : plt.Rectangle((xi, 0), step, func(xi), alpha=0.5, color='orange'),
        'right': lambda : plt.Rectangle((xi, 0), step, func(xi + step), alpha=0.5, color='orange'),
        'random': lambda : plt.Rectangle((xi, 0), step, func(random.uniform(xi, xi + step)), alpha=0.5, color='orange'),
        'midpoint': lambda : plt.Rectangle((xi, 0), step, func(xi + step/2), alpha=0.5, color='orange') 
    }
    rect = tabl.get(t)()
    plt.gca().add_patch(rect)

plt.title(f'Integral_sums')
plt.legend(labels=[f'func', f'a={a}, b={b}, n={n}, t={t}, k={k}'])

plt.show()
