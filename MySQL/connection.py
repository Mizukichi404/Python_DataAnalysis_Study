# MySQLdbのインポート
import MySQLdb

# データベースへの接続とカーソルの生成
connection = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='test',
    db='python_db')
cursor = connection.cursor()

# ここに実行したいコードを入力します
cursor.execute("SELECT * FROM m_users")

# 保存を実行
connection.commit()

# 接続を閉じる
connection.close()
