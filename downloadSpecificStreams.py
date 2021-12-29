from pytube import YouTube
from pytube.contrib.playlist import Playlist
from pytube.extract import playlist_id

yt = YouTube("https://www.youtube.com/watch?v=INRjTwJS99Y&list=PL5Q7nKvqetYmtreULPjF17AkyeU9eDB_C&index=27")

# now we will find its thumbnail Url and title
# titleOfVid = yt.title
# print(titleOfVid)
# thumbnailUrl = yt.thumbnail_url
# print(thumbnailUrl)

# -----For advance use case we will add a few arguments when creating a YouTube Object 
# yt = YouTube("https://www.youtube.com/watch?v=INRjTwJS99Y&list=PL5Q7nKvqetYmtreULPjF17AkyeU9eDB_C&index=27", on_progress_callback=progress_func,
# on_complete_callback=complete_func,
# proxies=myproxy)

'''
on_progress_callback=progress_func, ==> The on_progress_callback function will run whenever a chunk is downloaded from a video, and is called with three arguments: the stream, the data chunk, and the bytes remaining in the video. This could be used, for example, to display a progress bar

on_complete_callback=complete_func, ==> The on_complete_callback function will run after a video has been fully downloaded, and is called with two arguments: the stream and the file path. This could be used, for example, to perform post-download processing on a video like trimming the length of it.

proxies=myproxy

--------------------Note that you have to write progress_func, complete_func, myproxy functions yourself 
'''


# returns a list of video formats that video have
st = yt.streams
# print(*st, sep="\n")  # Will print every item in the list in the New Line 

# print(st, sep="\n")

#Progressive Formats (progressive streams have the video and audio in a single file)
stp = st.filter(progressive=True)
# print(*stp, sep="\n")

# DASH Formats 
std = st.filter(adaptive=True)
# print(*std, sep="\n")

# Lets try to filter out all audio streams available
# Audio Only files always have progressive false Beacause they contain Only audio files :)
sta = st.filter(only_audio=True)
# print(*sta, sep="\n")

# Filtering for MP4 streams
stmp4 = st.filter(file_extension='mp4')
stPMp4 = st.filter(progressive=True, file_extension='mp4') # -------This video have only 2 format for these filters

# print(*stPMp4, sep="\n", end="\n\n")  
# print(*stmp4, sep="\n")




#---------------------------------------------DOWNLOAD--------------------------------------------
''' 
Now we can download video which filered out 
from this video streams in any format we want 
'''
downloadst = st.get_by_itag(22) # we can download any stream by putting its 'itag' in ()
# downloadst.download()        # File will download in the same directory 

# Download only MP4
downloadstmp4 = st.filter(progressive=True, resolution="720p").first()
# downloadstmp4.download()

# Download only Audio
downloadstA = st.filter(progressive=True, only_audio=True, ).first()
# downloadstA.download()




#-----------------------------------------------CAPTIONS---------------------------------------------
# finding captions in the vid
yt1 = YouTube("https://www.youtube.com/watch?v=i5QV-9LGqcM")
titleOfVid = yt1.title
print(titleOfVid)
thumbnailUrl = yt1.thumbnail_url
print(thumbnailUrl)
# print(yt.captions)

# caption = yt1.captions.get_by_language_code('a.en')

# Captions converted into SRT Format
# print(caption.generate_srt_captions())      # Will print complete captions from the video



#-------------------------------------------PLAYLIST---------------------------------------------
'''Now We will get to its Playlist first step is to import playlist from pytube'''
# import pytube    # We can import whole pytube module or just what we needed here 'Playlist'
from pytube import Playlist

# Creting playlist object with playlist link
p = Playlist("https://www.youtube.com/playlist?list=PL5Q7nKvqetYmtreULPjF17AkyeU9eDB_C")

# Creting playlist object with video from the playlist
# p = Playlist(yt)
purl = p.video_urls
# print(*purl, sep="\n")

# Downloding playlists
ptitle = p.title

for video in p.videos:
    print(video.title, video.watch_url)
    print("Downloading : " + video.title)
    # video.streams.first().download()




# --------------------EXCEPTION DURING DOWNLOAING UNAVAILABLE VIDEO-------------------- 
'''
---------------------------------------
from pytube import Playlist, YouTube
>>> playlist_url = 'https://youtube.com/playlist?list=special_playlist_id'
>>> p = Playlist(playlist_url)
>>> for url in p.video_urls:
...     try:
...         yt = YouTube(url)
...     except VideoUnavailable:
...         print(f'Video {url} is unavaialable, skipping.')
...     else:
...         print(f'Downloading video: {url}')
...         yt.streams.first().download()
---------------------------------------
'''