from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=WMweEpGlu_U")

print(yt.title)

yt.streams[0].download()

