import numpy as np

np.arange(10)
np.arange(1, 11)
np.arange(1, 11, 2)

f = np.random.random((3, 2))
f
np.random.seed(123)
np.random.random((3, 2))

np.random.seed(123)
np.random.rand(4, 2)

np.random.seed(123)
np.random.randint(1, 10)

np.random.seed(123)
np.random.randint(1, 10, (3, 3))
np.random.seed(123)
np.random.uniform(0.0, 5.0, size=(2, 3))

np.random.seed(123)
np.random.uniform(size=(4, 3))
np.random.seed(123)
np.random.randn(4, 2)

np.zeros(3)
np.zeros((2, 3))
np.ones(2)
np.ones((3,4))

np.eye(3)
np.full(3, 3.14)
np.full((2, 4), np.pi)
np.nan
np.array([1, 2, np.nan])

np.linspace(0, 1, 5)
np.linspace(0, np.pi, 21)

l = np.array([2, 2, 6, 1, 3])
np.diff(l)
