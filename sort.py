import os
import sys
import glob
import shutil


directory = input("Enter Directory :")


def sort_text():
    files = glob.glob(f"{directory}/**/*.txt" , recursive=True)
    if files:
        textdir = os.path.join("/run/media/koosha/1632-930B/Documents/txt")
        os.makedirs(textdir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , textdir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No text Files Found"





def sort_document():
    files = glob.glob(f"{directory}/**/*.docx" , recursive=True)
    if files:
        documentdir = os.path.join("/run/media/koosha/1632-930B/Documents/docx")
        os.makedirs(documentdir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , documentdir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No document Files Found"





def sort_document_doc():
    files = glob.glob(f"{directory}/**/*.doc" , recursive=True)
    if files:
        documentdir = os.path.join("/run/media/koosha/1632-930B/Documents/doc")
        os.makedirs(documentdir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , documentdir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No document Files Found"


def sort_mp3():
    files = glob.glob(f"{directory}/**/*.mp3" , recursive=True)
    if files:
        mp3dir = os.path.join("/run/media/koosha/1632-930B/Documents/mp3")
        os.makedirs(mp3dir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , mp3dir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No mp3 Files Found"

