import numpy as np

N = 250

X = np.random.randint(0, 100, (N, N))
Y = np.random.randint(0, 100, (N, N+1))

result = np.dot(X, Y)

print(result)
