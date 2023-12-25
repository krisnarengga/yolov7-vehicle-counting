import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=1jN8EsFlpFk')
print('download...')
yt.streams.filter().get_highest_resolution().download(filename='off-peak1.mp4')
# 下載最高畫質影片，如果沒有設定 filename，則以原本影片的 title 作為檔名
print('ok!')