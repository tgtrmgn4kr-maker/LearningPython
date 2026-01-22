# DirsAndFiles Practice

This directory contains practice scripts for learning how to operate
files and directories in Python.

## What I practiced
- Using `os` and `os.path` to inspect directories
- Creating and checking folders safely
- Copying and moving files with `shutil`
- Handling command-line arguments with `argparse`

## Notes
- `os.path.exists()` is safer than assuming a directory exists
- Always test file operations on a copy first
- Windows file locks can affect delete operations

## Files
- `check_dirs.py`: check and create directories
- `find_dirs.py`: walk through directory trees
- `shutil_move_a_picture.py`: practice moving files
