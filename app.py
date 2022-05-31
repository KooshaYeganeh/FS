import os
import sys
import re
import glob
import time
import logging
import datetime




def scan():
	directory = input("Enter Directory to Scan with ClamAV")
	#TODO : if systemctl status clamav-freshclam is up then continue
	scan = os.popen(f"clamscan --recursive --infected --remove {directory}").read()
	return scan



def sort_with_scan():
    directory = input("Enter Directory to Scan with ClamAV & Sort Files")
    try:
        scan = os.popen(f"clamscan --infected --recursive --remove {directory}").read()
        if scan:
            docfiles=glob.glob(f"{directory}/**/*.doc" , recursive=True)
            if docfiles:
                documentdir = os.path.join(f"{directory}/Documents")
                os.makedirs(documentdir,exist_ok=True)
                for docfile in docfiles:
                    shutil.move(docfile,documentdir)
            docxfiles=glob.glob(f"{directory}/**/*.docx" , recurive=True)
            if docxfiles:
                documentdir = os.path.join(f"{directory}/Documents")
                os.makedirs(documentdir,exist_ok=True)
                for docxfile in docxfiles:
                    shutil.move(docxfile,documentdir)
            mp3files=glob.glob(f"{directory}/**/*.mp3" , recursive=True)
            if mp3files:
                mp3dir = os.path.join(f"{directory}/Mp3")
                od.makedirs(mp3dir , exist_ok = True)
                for mp3file in mp3files:
                    shutil.move(mp3file,mp3dir)

            mp4files=glob.glob(f"{directory}/**/*.mp4" , recursive=True)
            if mp4files:
                mp4dir = os.path.join(f"{directory}/Mp4")
                od.makedirs(mp4dir , exist_ok = True)
                for mp4file in mp4files:
                    shutil.move(mp4file,mp4dir)

            avifiles=glob.glob(f"{directory}/**/*.avi" , recursive=True)
            if avifiles:
                avidir = os.path.join(f"{directory}/AVI")
                od.makedirs(avidir , exist_ok = True)
                for avifile in avifiles:
                    shutil.move(avifile,avidir)

            mkvfiles=glob.glob(f"{directory}/**/*.mkv" , recursive=True)
            if mkvfiles:
                mkvdir = os.path.join(f"{directory}/MKV")
                od.makedirs(mkvdir , exist_ok = True)
                for mkvfile in mkvfiles:
                    shutil.move(mkvfile,mkvdir)

            pdffiles=glob.glob(f"{directory}/**/*.pdf" , recursive=True)
            if pdffiles:
                pdfdir = os.path.join(f"{directory}/PDF")
                od.makedirs(pdfdir , exist_ok = True)
                for pdffile in pdffiles:
                    shutil.move(pdffile,pdfdir)

            pptfiles=glob.glob(f"{directory}/**/*.ppt" , recursive=True)
            if pptfiles:
                pptdir = os.path.join(f"{directory}/Mp3")
                od.makedirs(pptdir , exist_ok = True)
                for pptfile in pptfiles:
                    shutil.move(pptfile,pptdir)

            csvfiles=glob.glob(f"{directory}/**/*.csv" , recursive=True)
            if csvfiles:
                csvdir = os.path.join(f"{directory}/Mp3")
                od.makedirs(csvdir , exist_ok = True)
                for csvfile in csvfiles:
                    shutil.move(csvfile,csvdir)

            xlsxfiles=glob.glob(f"{directory}/**/*.xlsx" , recursive=True)
            if xlsxfiles:
                xlsxdir = os.path.join(f"{directory}/Mp3")
                od.makedirs(xlsxdir , exist_ok = True)
                for xlsxfile in xlsxfiles:
                    shutil.move(xlsxfile,xlsxdir)

            txtfiles=glob.glob(f"{directory}/**/*.txt" , recursive=True)
            if txtfiles:
                txtdir = os.path.join(f"{directory}/Mp3")
                od.makedirs(txtdir , exist_ok = True)
                for txtfile in txtfiles:
                    shutil.move(txtfile,txtdir)

            bkffiles =glob.glob(f"{directory}/**/*.bkf" , recursive=True)
            if bkffiles:
                bkfdir = os.path.join(f"{directory}/Mp3")
                od.makedirs(bkfdir , exist_ok = True)
                for bkffile in bkffiles:
                    shutil.move(bkffile,bkfdir)

            tarfiles = glob.glob(f"{directory}/**/*.tar" , recursive=True)
            if tarfiles:
                tardir = os.path.join(f"{directory}/Mp3")
                od.makedirs(tardir , exist_ok = True)
                for tarfile in tarfiles:
                    shutil.move(tarfile,tardir)

            zipfiles = glob.glob(f"{directory}/**/*.zip" , recursive=True)
            if zipfiles:
                zipdir = os.path.join(f"{directory}/Mp3")
                od.makedirs(zipdir , exist_ok = True)
                for zipfile in zipfiles:
                    shutil.move(zipfile,zipdir)
    except:
        print("ERROR on File Scanning.")



























def print_menu():
    print("choose what you want KYGnus-FS do?")
    print("1.Scan")
    print("2.Sort with Scan")
    print("3.Sort Without Scan")
    print("4.Exit")
    return ""


if __name__ == "__main__":
    menu_choice = 0
    print(create_logo())
    words = "KYGnus-FS,Sort Files Easily:\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(print_menu())

    while menu_choice != 4:
        print("Type in your choice:")
        while True:
            try:
                menu_choice = int(input('>'))
            except ValueError:
                pass
            if (menu_choice > 0 or menu_choice < 7):
                break
        if menu_choice == 1:
            print("menu1")
