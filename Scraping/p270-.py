import requests

r = requests.get("https://codezine.jp/") # URLにアクセスする
print(type(r))
print(r.status_code) # ステータスコードを確認

text = r.text # HTMLのソースコードを取得する
for line in text.split("\n"):
    if "<title>" in line or "<h1>" in line:
        print(line.strip())

from bs4 import BeautifulSoup

# HTMLを解析したオブジェクトを生成
soup = BeautifulSoup(text, "html.parser")
print(soup.title) # <title>タグの情報を取得
print(soup.h1) # <h1>タグの情報を取得
# h1タグの中のaタグの中のimgタグの中のalt属性
print(soup.h1.a.img["alt"])

atags = soup.find_all("a") # すべてのaタグを取得
print("aタグの数：", len(atags)) # aタグの数を取得
for atag in atags[:5]:
    print("タイトル：", atag.text) # aタグのテキストを取得
    print("リンク：", atag["href"]) # aタグのリンクを取得
    
