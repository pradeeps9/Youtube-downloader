from pytube import YouTube


yt = YouTube("https://www.youtube.com/watch?v=INRjTwJS99Y&list=PL5Q7nKvqetYmtreULPjF17AkyeU9eDB_C&index=27")

# now we will find its thumbnail Url and title
titleOfVid = yt.title
print(titleOfVid)
thumbnailUrl = yt.thumbnail_url
print(thumbnailUrl)

print(*yt.streams.filter(only_audio=True), sep="\n")

downloadA = yt.streams.filter(only_audio=True).first()
downloadA.download()


