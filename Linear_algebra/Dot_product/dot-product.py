import numpy as np

def unit_vector(v):
    norm = np.linalg.norm(v)
    if norm != 0:
        return v/norm
    else:
        return 0

v = np.random.rand(3, 1)
u = v/np.linalg.norm(v)
print(u)

V = np.random.rand(3, 30)
U = []
for i in range(30):
    U.append(unit_vector(V[ : ,i]))

Dot = []
for i in range(30):
    Dot = np.dot(u.T, U[i])
avg = np.sum(Dot)/30
print(avg)