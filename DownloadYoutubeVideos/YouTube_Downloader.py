import argparse
import platform
import re
import subprocess
from pytubefix import YouTube, exceptions, streams
from os import path, makedirs, remove

def pyTube_folder():    #To check what the operating system is and then make a directory to storage files 
    sys = platform.system()
    home = path.expanduser('~')

    if sys == 'Darwin':  #Mac
        folder = path.join(home, 'Movies', 'PyTube')
    else:                #Windows, Linux
        folder = path.join(home, 'Videos', 'PyTube')

    makedirs(folder, exist_ok=True)

    return folder  #Users\user\Videos\PyTube

def merge_files(video_path, audio_path, output_path):
    command = [
        "ffmpeg",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        output_path
    ]
    subprocess.run(command)
    remove(video_path)
    remove(audio_path)

    print("Merge complete.")

def download_audio(yt, folder): #To download audio
    audio = yt.streams.get_audio_only()
    if audio:
        print('Downloading audio file...')
        return audio.download(output_path=folder, 
                              filename_prefix='audio_')
    else:
        print('Error: No audio file exists')
        return None
    
def download_video(yt, res, folder, filename):

    progressive = yt.streams.filter(resolution=res, progressive=True).first()

    if progressive:
        print(f"Downloading {res} (progressive)...")
        progressive.download(output_path=folder, filename=filename)
        print("Download complete.")
        return

    # 如果沒有 progressive

    video = yt.streams.filter(resolution=res, adaptive=True).first()

    if not video:
        print("No matching stream found.")
        return
    
    print("No progressive stream found. Using adaptive + ffmpeg merge.")
    print(f'Downloading {res} video file (adaptive)')
    
    video_path = video.download(output_path=folder, filename_prefix='video_')
    audio_path = download_audio(yt, folder)

    output_path = path.join(folder, filename)

    merge_files(video_path,audio_path,output_path)

    return  



def onProgress(stream, chunk, remains):
    total = stream.filesize
    if total > 0:
        percent = (total - remains) / total * 100
    print(f'Downloading...{percent:06.2f}%', end='\r')


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
        
         
        target_res = None

        resolution_map = {'sd': '480p',            #resolution options
                          'hd': '720p',
                          'fhd': '1080p',
                          'qhd': '1440p',
                          'uhd': '2160p'
                          }

        desired_res = None

        for key, value in resolution_map.items():     
            if getattr(args, key):
                desired_res = value
                break


        available_resolutions = sorted(
            {
            stream.resolution
            for stream in yt.streams.filter(file_extension='mp4')
            if stream.resolution is not None
            },
            key=lambda x: int(x.replace("p", ""))
            )


        if desired_res and desired_res in available_resolutions:
            target_res = desired_res
        else:
            print("Available resolutions:")

            for idx, res in enumerate(available_resolutions, start=1):
                print(f"{idx}) {res}")

            try:
                choice = input("Select resolution number (default=1): ")

                if choice.strip() == "":
                    target_res = available_resolutions[0]
                else:
                    choice = int(choice)
                    target_res = available_resolutions[choice - 1]

            except (ValueError, IndexError):
                print("Invalid selection. Using default.")
                target_res = available_resolutions[0]

        global output_filename
        output_filename = f"{yt.title} ({target_res}).mp4"
        download_video(yt, target_res, download_folder, output_filename)


    except exceptions.PytubeFixError as e:
        print(f'\nPytube errors: {e}')

    except Exception as e:
        print(f'\nUnpredicted errors: {e}')

if __name__ == '__main__':
    main()

