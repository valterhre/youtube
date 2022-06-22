from pytube import Search
from pytube import YouTube
from pytube import Channel
s = Search('YouTube Rewind')
print(s.results)
def links(videos, img1=False):
    for res in videos:
        link=str(res)[41:-1]
        youtub='https://www.youtube.com/watch?v='+link
        yt=YouTube(youtub).title
        print(yt,'\n',youtub)
        if img1==True:
            img=f'https://i.ytimg.com/vi/{link}/maxresdefault.jpg'
            print(img)
def download(url):
    yt=YouTube(url)
    print(yt.title)
    print('Chose resolution:\n', '1:144\n','2:360\n', '3:480\n', '4:720\n')
    i=input()
    chose={'1':'144p','2':'360p','3':'480p','4':'720p','5':'1080p'}
    try:
        yt.streams.get_by_resolution(chose.get(i)).download()
    except:
        print('video has not those resolution')
        i=int(i)+1
        yt.streams.get_by_resolution(chose.get(i)).download()
        print(f'But we have resolution {chose.get(i)}')
chan=input()
c=Channel(f'https://www.youtube.com/c/{chan}')
links(c.videos, True)
url=input()
download(url)