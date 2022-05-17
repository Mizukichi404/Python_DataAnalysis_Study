import numpy as np
import sys

sys.maxsize

a = np.array([1, 2, 3])

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

a.dtype

d = np.array([1, 2], dtype=np.int16)
d.dtype
d.astype(np.float16)

a
a[0]
a[1:]
a[-1]

b
b[0]
b[1, 0]
b[:, 2]
b[1, :]
b[0, 1:]
b[:, 0:2]
