import numpy as np

a = np.array([1,2,3])

a

print(a)

type(a)

a.shape

b = np.array([[1, 2, 3], [4, 5, 6]])

b
b.shape

c1 = np.array([0, 1, 2, 3, 4, 5])
c1

c2 = c1.reshape((2, 3))
c2

c3 = c2.ravel()
c3

c4 = c2.flatten() #copy を返す
c4
