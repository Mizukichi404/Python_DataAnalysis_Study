import numpy as np

a = np.array([1, 5, 4])
a1 = np.array([1, 5, 4])

print(a)
print(a1)
np.concatenate([a, a1])

b = np.array([[1, 2, 8], [4, 5, 8]])
b
b1 = np.array([[10], [20]])
b1
np.concatenate([b, b1], axis=1)
np.hstack([b, b1])

b2 = np.array([30, 60, 45])
b2

#vstack関数で行を増やす
b3 = np.vstack([b, b2])
b3

#分割
#hsplit関数で列方向に分割する
#第2引数に2を指定し、一つ目の配列firstが2列になる
#二つ目の配列secondは一列になる
first, second = np.hsplit(b3, [2])
first
second

#vsplit関数で行方向に分割する
first1, second1 = np.vsplit(b3, [2])
first1
second1


'''転置
二次元配列の行と列を入れ替えること転置という。
転置にはTを使う
'''
b
b.T
'''次元追加
一次元配列aを2次元配列にする
'''
a
#行方向を指定するスライシングにnp.newaxisを指定し次元を1つ増やす
a[np.newaxis, :]
#列方向を指定するスライシングにnp.newaxisを指定する
a[:, np.newaxis]
