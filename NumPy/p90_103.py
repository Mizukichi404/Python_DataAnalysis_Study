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

a
a[2] = 4
a

b
b[1, 2] = 7
b
b[:, 2] = 8
b

a1 = a
a1

a1[1] = 5
a1

a

a2 = a.copy()
a2

a2[0] = 6
a2

a

c2
c2[0, 0] = 0
c4 = c2.flatten()
c3[0] = 6
c4[1] = 7

c3
c4
c2
py_list1 = [0, 1]
py_list2 = py_list1[:]
py_list2[0] = 2
print(py_list1)
print(py_list2)

np_array1 = np.array([0, 1])
np_array2 = np_array1[:]
np_array2[0] = 2
print(np_array1)
print(np_array2)
