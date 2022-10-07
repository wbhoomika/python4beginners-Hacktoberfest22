import os
import shutil

# Put full path of your Downloads folder
src = r""

dest_media = src +"\\Media_files"
dest_exe = src + "\\Installation_Files"
dest_img = src + "\\Image_Files"
dest_zip = src + "\\Zip"
dest_doc = src + "\\Documents"

# Checks through every file in the directory path specified by "src"

for file in os.listdir(src):
    extension = os.path.splitext(file)[1]
    if extension in [".exe", ".msi"]:
        if not os.path.exists(dest_exe):
            os.makedirs(dest_exe)
        if not os.path.exists(dest_exe+"\\"+file):
            shutil.move(src+"\\"+file, dest_exe)
        else:
            os.remove(dest_exe+"\\"+file)
            shutil.move(src+"\\"+file, dest_exe)

    elif extension in [".mp4", ".avi", ".mov", ".mp3", ".mkv"]:
        if not os.path.exists(dest_media):
            os.makedirs(dest_media)
        if not os.path.exists(dest_media+"\\"+file):
            shutil.move(src+"\\"+file, dest_media)
        else:
            os.remove(dest_media+"\\"+file)
            shutil.move(src+"\\"+file, dest_media)

    elif extension in [".jpg", ".jpeg", ".png", ".svg", ".jfif"]:
        if not os.path.exists(dest_img):
            os.makedirs(dest_img)
        if not os.path.exists(dest_img+"\\"+file):
            shutil.move(src+"\\"+file, dest_img)
        else:
            os.remove(dest_img+"\\"+file)
            shutil.move(src+"\\"+file, dest_img)

    elif extension in [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xlsx", ".csv", ".epub", ".odt", ".txt"]:
        if not os.path.exists(dest_doc):
            os.makedirs(dest_doc)
        if not os.path.exists(dest_doc+"\\"+file):
            shutil.move(src+"\\"+file, dest_doc)
        else:
            os.remove(dest_doc+"\\"+file)
            shutil.move(src+"\\"+file, dest_doc)

    elif extension in [".7z", ".zip", ".rar"]:
        if not os.path.exists(dest_zip):
            os.makedirs(dest_zip)
        if not os.path.exists(dest_zip+"\\"+file):
            shutil.move(src+"\\"+file, dest_zip)
        else:
            os.remove(dest_zip+"\\"+file)
            shutil.move(src+"\\"+file, dest_zip)
