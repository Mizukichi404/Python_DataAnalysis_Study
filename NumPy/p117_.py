import numpy as np

'''グリッドデータの作成
meshgrid関数は、二次元上の点に対応する等高線やヒートマップなどを描く時に使用する。
x,yの配列から、点の座標を生成する。
'''
m = np.arange(0, 4)
m
n = np.arange(4, 7)
n

#mとnを行方向と列方向に方眼上（グリッド）のデータを生成する
xx, yy = np.meshgrid(m, n)
xx
yy

'''NumPyの各機能'''
a = np.arange(3)
b = np.arange(-3, 3).reshape((2, 3))
c = np.arange(1, 7).reshape((2, 3))
d = np.arange(6).reshape((3, 2))
e = np.linspace(-1, 1, 10)
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)

print("a:", a.shape)
print("b:", b.shape)
print("c:", c.shape)
print("d:", d.shape)
print("e:", e.shape)
