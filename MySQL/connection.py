# MySQLdbのインポート
import MySQLdb

# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='test',
    db='python_db',
    #テーブル内部で日本語を扱うための追加
    charset='utf8'
)
cursor = connection.cursor()

# ここに実行したいコードを入力します
cursor.execute("SELECT * FROM m_users")

#fetchall()で全件取り出し
rows = cursor.fetchall()
#fetchone()で1件ずつ取り出し
rows = cursor.fetchone()
#テーブルのデータがemptyのため、'NoneType'object is not iterableのエラーがでる
print(rows)

# 保存を実行
connection.commit()

# 接続を閉じる
connection.close()
