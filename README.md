LearningPython
===
This repository is for recording my learning progress

## DirsAndFiles Practice

This directory contains practice scripts for learning how to operate
files and directories in Python.

### What I practiced
- Using `os` and `os.path` to inspect directories
- Creating and checking folders safely
- Copying and moving files with `shutil`
- Handling command-line arguments with `argparse`

### Notes
- `os.path.exists()` is safer than assuming a directory exists
- Always test file operations on a copy first
- Windows file locks can affect delete operations

### Files
- `check_dirs.py`: check and create directories
- `find_dirs.py`: walk through directory trees
- `shutil_move_a_picture.py`: practice moving files

## Pip_and_Environment Practice

This directory contains practice scripts for learning how to operate packages
and virtual environments in Python.

### What I practiced
- Using Anaconda to manage my environments and packages
- Using `conda env list` to check the existing environments
- Using `conda create -n (env) python=3.x` to create a new environment
- Using `conda remove -n (env)` to remove existing environment
- Using `conda activate (env)` to activate certain environment
- Using `pip install xxx` or `pip uninstall xxx` to install or uninstall packages  
- Another way to create a new environment:  
    1. Creating a new directory  
    2. Inputting `cd PATH` to change path
    3. Inputting `python -m venv (name of virtual environment)` to create a new environment 
- Using `conda env export > environment.yml` to generate a file which records the environment of the project
- Using `conda env create -f environment.yml` to reproduce the environment

### Notes
- It' more professional to write `environment.yml` yourself to avoid installing useless packages

### Files
- `Chicken_and_VirtualEnvironment.py`: try to install 'sympy' and use it
- `environment.yml`: record a environment which can run `Chicken_and_VirtualEnvironment.py`

## DownloadYoutubeVideos

This directory contains practice scripts for learning how to download video and audio from YouTube with pytubefix in Python

### What I practiced
- Using `argparse` to process the command-line arguments entered by the user.
- Checking the user's operating system and then making a directory properly to store files downloaded by `YouTube_Downloader.py`
- Using `pytubefix` to analyze formats of audio and video and then download them
- Using `subprocess.run()` to run a command which is written in `YouTube_Downloader.py`
- Using `getattr()` to check if the resolution that the user chose is available
- Writing a function `sanitize_filename()` to prevent from errors occuring because of illegal characters in Windows  
- Using `try except` to monitor the errors occured during running

### Notes
- Write more comment to make your code more readable

### Files
- `Download_Video.py`: To understand how to use `pytubefix`
- `YouTube_Downloader.py`: To make a available file to download files from YouTube
