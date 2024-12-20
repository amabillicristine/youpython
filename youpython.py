import yt_dlp

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'format': 'best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=mUiYzXvjGlk'])
    
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://youtu.be/nlix8b65X2Q'])
    
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://youtu.be/MayyQ84sWA0'])
    
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://youtu.be/AEzTFKQnmUs'])
    
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://youtu.be/s1txZzj-zV0'])
    
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://youtu.be/N9ykautGS58'])
    
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://youtu.be/9hf3BvVF9hI'])

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://youtu.be/VIRdXxhmpBA'])
    
