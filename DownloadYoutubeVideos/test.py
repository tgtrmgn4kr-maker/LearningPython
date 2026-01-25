from pytubefix import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

print(yt.streams[1])
print(type(yt.streams[1]))
print(type(yt.streams))
print(type(str(yt.streams[1])))
if 'res="2160p"' in str(yt.streams[1]):
    print(True)
print([0]*5)

