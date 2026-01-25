import pytubefix
from pytubefix import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

try:
    print(yt.title)
    print(yt.streams) #Information in the video
    print(yt.streams.filter(resolution='2160p')[1])
    video = yt.streams.filter(resolution='2160p')[1]
    video.download(output_path='.\\DownloadYoutubeVideos')  #video with no audio
    audio = yt.streams.get_audio_only()
    audio.download(output_path='.\\DownloadYoutubeVideos')
    for i in yt.streams:
        print(f'\n{i}')
except FileNotFoundError as e:
    print(f'ErrorsOccured: {e}')
    print('The file cannot be find. Please check if you have permission to access files')
except pytubefix.exceptions.RegexMatchError as e:
    print(f'ErrorsOccured: {e}') 
    print('Check your Network Connection and the YouTube url')
except Exception as e:
    print(f'ErrorOccured: {e}')




''' Sample information
<Stream: itag="18"               'classification number'     
         mime_type="video/mp4"   'content type'
        res="360p"               'resolution'
        fps="25fps"              'frame per second'
        vcodec="avc1.42001E"     'video code'
        acodec="mp4a.40.2"       'audio code' 
        progressive="True"       'progressive stream'
        sabr="False"             'Segmented Adaptive Bitrate streaming'
        type="video"             'type'
        >

<Stream: itag="401" 
        mime_type="video/mp4" 
        res="2160p" 
        fps="25fps" 
        vcodec="av01.0.12M.08" 
        progressive="False" 
        sabr="False" 
        type="video"
        >
'''