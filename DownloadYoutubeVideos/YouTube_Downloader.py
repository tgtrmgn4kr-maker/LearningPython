import argparse
import platform
import re
from pytubefix import YouTube, exceptions, streams
from os import path, makedirs

def pyTube_folder():    #To check what the operating system is and then make a directory to storage files 
    sys = platform.system()
    home = path.expanduser('~')

    if sys == 'Darwin':  #Mac
        folder = path.join(home, 'Movies', 'PyTube')
    else:                #Windows, Linux
        folder = path.join(home, 'Videos', 'PyTube')

    makedirs(folder, exist_ok=True)

    return folder  #Users\user\Videos\PyTube

def download_audio(yt, folder): #To download audio
    audio = yt.streams.get_audio_only()
    if audio:
        print('Downloading audio file...')
        audio.download(output_path=folder, 
                       filename_prefix='audio_')
    else:
        print('Error: No audio file exists')
        return None
    
def download_video(yt, res, folder): #To download video
    video = yt.streams.filter(resolution=res,adaptive=True).first()
    if video:                        #If video is adaptive, just download it
        video.download(output_path=folder,
                       filename = output_filename)
        print('Download Complete')
        return
    else:
        video = yt.streams.filter(resolution=res,progressive=True).first() #If video is progressive, download the audio, too
        video.download(output_path=folder,
                       filename_prefix='video_')
        download_audio(yt, folder)
        if download_audio(yt, folder) == None: 
            print('The video has no audio')
            return 'video only'
        else:
            print('Video and audio are both downloaded')

def onProgress(stream, chunk, remains):
    total = stream.filesize
    if total > 0:
        percent = (total - remains) / total * 100
    print(f'Downloading...{percent:05.2f}', end='\r')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Enter a YouTube url')
    parser.add_argument('-sd', action='store_true', help='480p')
    parser.add_argument('-hd', action='store_true', help='720p')
    parser.add_argument('-fhd',action='store_true', help='1080p')
    parser.add_argument('-qhd',action='store_true', help='1440p')
    parser.add_argument('-uhd',action='store_true', help='2160p')
    parser.add_argument('-a',  action='store_true', help='Audio Only')

    args = parser.parse_args()
    download_folder = pyTube_folder()   ##Users\user\Videos\PyTube

    try:
        yt = YouTube(args.url, on_progress_callback=onProgress)

        if args.a:
            download_audio(yt, download_folder)
            return
        
        global output_filename 
        

        target_res = None
        desired_res = None

        if args.sd:     
            desired_res = '480p'
        elif args.hd:
            desired_res = '720p'
        elif args.fhd:
            desired_res = '1080p'
        elif args.qhd:
            desired_res = '1440p'
        elif args.uhd:
            desired_res = '2160p'

        video_res = [False]*5
        resolutions = [['480p',False],
                       ['720p',False],
                       ['1080p',False],
                       ['1440p',False],
                       ['2160p',False]]

        for i in yt.streams:
            if 'res="480p"' in str(yt.streams[i]):
                resolutions[0][1] = True
            elif 'res="720p"' in str(yt.streams[i]):
                resolutions[1][1] = True
            elif 'res="1080p"' in str(yt.streams[i]):
                resolutions[2][1] = True
            elif 'res="1440p"' in str(yt.streams[i]):
                resolutions[3][1] = True
            elif 'res="2160p"' in str(yt.streams[i]):
                resolutions[4][1] = True

        is_Find = False
        for i in range(5):
            if (desired_res in resolutions[i]) and (resolutions[i][1] == True): #If desired res is available, target_res = desired_res
                target_res = desired_res
                is_Find = True

        if not is_Find: #If desired res is not available, make a list and let user to choose another
            new_resolutions = []
            count = 0
            print(f'The resolution is unusable.')
            for i in range(5):
                if True in resolutions[i]:
                    new_resolutions.append(resolutions[i])
                    count += 1
                    print(f'{count+1}) {new_resolutions[0]}')

            val = int(input('Select one number(Default is "1"):'))
            try:
                if (val > 0) and (val <= len(new_resolutions)):
                    target_res = new_resolutions[val][0]
                else:
                    print('You seleted a invalid number, using "Default"')
                    target_res = new_resolutions[0][0]
            except ValueError:
                    target_res = new_resolutions[0][0]
            output_filename = f'{yt.title} ({target_res}).mp4'
            full_path = path.join(download_folder,output_filename)
            download_video(yt, target_res, download_folder)
            
            
    except exceptions.PytubeFixError as e:
        print(f'\nPytube errors: {e}')

    except Exception as e:
        print(f'\nUnpredicted errors: {e}')

if __name__ == '__main__':
    main()

