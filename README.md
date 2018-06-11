# dotmatrix_64x48_weather

## 概要
w-dee氏のマゾクロック3用のソフトウェアです。
マーキー機能を使って、30分毎にYahoo!天気から天気を取得してマゾクロックに設定します。

## セットアップ
### インストール
* sudo apt install python3
* pip install mojimoji

### ソースを自分の環境用に修正
* setWeather.pyの下記の部分を修正してください。
```python
# 自分の環境に合わせる
MAZO_IP = '192.168.11.7'
WEATHER_URL = 'https://rss-weather.yahoo.co.jp/rss/days/5610.xml'
```

## 実行
```
python3 setWeather.py
```

## サーバー化
raspberry piなどのLinux環境でデーモンとして実行させる。

```bash
sudo vim /etc/rc.local
```
で、
```
python3 [setWeather.pyを置いたパス] &
```
などとすると良い。
