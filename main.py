# Naveen Prabaharan
# 12/10/23

# This python script will organize the files from the given folder into different subfolders for easier access to them later. 

import os
import shutil
# Image Extensions
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# Video Extensions
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# Audio Extensions
audio_extensions = [".aac", ".aiff", ".ape", ".au", ".flac", ".gsm", ".it", ".m3u", ".m4a", ".mid", ".mod", ".mp3", ".mpa", ".ogg", ".pls", ".ra", ".s3m", ".sid", ".wav", ".wma", ".xm"]

# Document Extensions
document_extensions = [".docx", ".doc", ".ebook", ".log", ".md", ".msg", ".odt", ".org", ".pages", ".pdf", ".rtf", ".rst", ".tex", ".txt", ".wpd", ".wps",
                       ".pptx", ".ppt", ".odp", ".ods", ".xls", ".xlsx", ".csv", ".tsv", ".ics", ".vcf"]
# Program Extensions
executable_extensions = [".msi", ".bin", ".command", ".sh", ".bat", ".crx", ".bash", ".csh", ".fish", ".ksh", ".zsh", ".exe"]

# Archive Extensions
archive_extensions = [".apk", ".ar", ".bz2", ".cab", ".cpio", ".deb", ".dmg", ".egg", ".gz", ".iso", ".jar", ".lha", ".mar", ".pea", ".rar", ".rpm", ".s7z",
                      ".shar", ".tar", ".tbz2", ".tgz", ".tlz", ".war", ".whl", ".xpi", ".zip", ".zipx", ".zst", ".xz", ".pak", ".7z"]

path = "C:\\Users\\nphn6\\Downloads"
obj = os.scandir(path)
 
# List all files and directories 
# in the specified path
print("Files and Directories in '% s':" % path)
print("=======================================================")

for file in obj:
    if file.is_dir():
        shutil.move(file, "E:\Downloads")

print("=======================================================")
 
 
# entry.is_file() will check
# if entry is a file or not and
# entry.is_dir() method will
# check if entry is a
# directory or not. 
 
 
# To Close the iterator and
# free acquired resources
# use scandir.close() method
obj.close()

