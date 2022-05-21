import pandas as pd
ser = pd.Series([10, 20, 30, 40])
ser

'''DataFrame
DataFrameは２次元のデータ。DataFrameオブジェクトを作るにはDataFrameを使う。'''
df = pd.DataFrame(
[[10, "a", True],
[20, "b", False,],
[30, "c", False],
[40, "d", True]])
df

import numpy as np
df = pd.DataFrame(np.arange(100).reshape((25, 4)))
#作成した25行4列のデータを表示
df
#作成したデータの先頭5行を表示
df.head()
#作成したデータの末尾の5行を表示
df.tail()
#作成したデータのサイズを表示
df.shape

'''インデックス名、カラム名'''
df = pd.DataFrame(np.arange(6).reshape((3, 2)))
df
#作成したデータのインデックス名を設定
df.index = ["01", "02", "03"]
#作成したデータのカラム名を設定
df.columns = ["A", "B"]
#作成したデータの表示
df

#データ作成時にインデックスとカラムを設定する
named_df = pd.DataFrame(np.arange(6).reshape((3, 2)),
columns=["A列", "B列"],
index=["1行目", "2行目", "3行目"])
#作成したデータの表示
named_df

#辞書(dict)形式でDataFrameの作成
pd.DataFrame({"A列": [0, 2, 4], "B列": [1, 3, 5]})
