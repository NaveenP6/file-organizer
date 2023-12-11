# Naveen Prabaharan
# 12/10/23

# This python script will organize the files from the given folder into different subfolders for easier access to them later. 

import os
import sys
import datetime
import shutil
from pathlib import Path

# Image Extensions
image_extensions = (".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico")
# Video Extensions
video_extensions = (".3g2", ".3gp", ".aaf", ".asf", ".avchd", ".avi", ".drc", ".flv", ".m2v", ".m4p", ".m4v", ".mkv", ".mng", ".mov", ".mp2", ".mp4", ".mpe", ".mpeg", ".mpg",
                         ".mpv", ".mxf", ".nsv", ".ogv", ".ogm", ".ogx", ".qt", ".rm", ".rmvb", ".roq", ".srt", ".svi", ".vob", ".webm", ".wmv", ".yuv")
# Audio Extensions
audio_extensions = (".aac", ".aiff", ".ape", ".au", ".flac", ".gsm", ".it", ".m3u", ".m4a", ".mid", ".mod", ".mp3", ".mpa", ".ogg", ".pls", ".ra", ".s3m", ".sid", ".wav", ".wma", ".xm")

# Document Extensions
document_extensions = (".docx", ".doc", ".ebook", ".log", ".md", ".msg", ".odt", ".org", ".pages", ".pdf", ".rtf", ".rst", ".tex", ".txt", ".wpd", ".wps",
                       ".pptx", ".ppt", ".odp", ".ods", ".xls", ".xlsx", ".csv", ".tsv", ".ics", ".vcf")
# Program Extensions
executable_extensions = (".msi", ".bin", ".command", ".sh", ".bat", ".crx", ".bash", ".csh", ".fish", ".ksh", ".zsh", ".exe")

# Archive Extensions
archive_extensions = (".apk", ".ar", ".bz2", ".cab", ".cpio", ".deb", ".dmg", ".egg", ".gz", ".iso", ".jar", ".lha", ".mar", ".pea", ".rar", ".rpm", ".s7z",
                      ".shar", ".tar", ".tbz2", ".tgz", ".tlz", ".war", ".whl", ".xpi", ".zip", ".zipx", ".zst", ".xz", ".pak", ".7z")

path = "" # This can be changed to the directory of your choice depending on where you store your files

# moveFile function Sorts files in directory by file type, organizes the files in a different folders
def moveFiles():
    for files in os.listdir(path):
        if files.endswith(image_extensions):
            if os.path.exists(f"{path}\\Images") == True:
                pass
            else:
                os.mkdir(f"{path}\\Images")

            shutil.move(f"{path}\\{files}", f"{path}\\Images")
        elif files.endswith(video_extensions):
            if os.path.exists(f"{path}\\Video") == True:
                pass
            else:
                os.mkdir(f"{path}\\Video")

            shutil.move(f"{path}\\{files}", f"{path}\\Video")
        elif files.endswith(audio_extensions):
            if os.path.exists(f"{path}\\Audio") == True:
                pass
            else:
                os.mkdir(f"{path}\\Audio")

            shutil.move(f"{path}\\{files}", f"{path}\\Audio")
        elif files.endswith(document_extensions):
            if os.path.exists(f"{path}\\Docs") == True:
                pass
            else:
                os.mkdir(f"{path}\\Docs")

            shutil.move(f"{path}\\{files}", f"{path}\\Docs")
        elif files.endswith(executable_extensions):
            if os.path.exists(f"{path}\\Programs") == True:
                pass
            else:
                os.mkdir(f"{path}\\Programs")

            shutil.move(f"{path}\\{files}", f"{path}\\Programs")
        elif files.endswith(archive_extensions):
            if os.path.exists(f"{path}\\Zipped") == True:
                pass
            else:
                os.mkdir(f"{path}\\Zipped")

            shutil.move(f"{path}\\{files}", f"{path}\\Zipped")
        else:
            print(f"UNKOWN: {files}")
            continue

    print("-----Organized Files-----")
moveFiles()