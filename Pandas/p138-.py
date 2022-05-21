import requests

r = requests.get('https://codezine.jp/') # URLにアクセスする
print(type(r))
print(r.status_code)    # ステータスコードを確認

text = r.text    # HTMLのソースコードを取得する
for line in text.split('\n'):
    if '<title>' in line or '<h1>' in line:
        print(line.strip())
