# Naveen Prabaharan
# 12/10/23

# This python script will organize the files from the given folder into different subfolders for easier access to them later. 

import os
import time
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

path = "C:\\Users\\nphn6\\Downloads" # This can be changed to the directory of your choice depending on where you store your files

# moveFiles function moves files into the correct directory
def moveFiles(path, files, folder):
    if not os.path.exists(f"{path}\\{folder}"):
        os.mkdir(f"{path}\\{folder}")

    shutil.move(f"{path}\\{files}", f"{path}\\{folder}")


def main():

    print("Starting...")
    print(" ")

    time.sleep(3)

    for files in os.listdir(path):
        if files.endswith(image_extensions):
            moveFiles(path, files, "Images")

        elif files.endswith(video_extensions):
            moveFiles(path, files, "Video")

        elif files.endswith(audio_extensions):
            moveFiles(path, files, "Audio")

        elif files.endswith(document_extensions):
            moveFiles(path, files, "Docs")

        elif files.endswith(executable_extensions):
            moveFiles(path, files, "Programs")

        elif files.endswith(archive_extensions):
            moveFiles(path, files, "Zipped")
        
        else:
            print(f"UNKOWN: {files}", datetime.datetime.now().strftime("%H:%M:%S"))
            continue

    print(" ")
    print("-----Organized Files-----", datetime.datetime.now().strftime("%H:%M:%S"))
main()