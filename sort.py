import os
import sys
import glob
import shutil


directory = input("Enter Directory :") # get directory



def scan():
    """ This Function Scan Recursively with clamAV and remove 
    malicious Files """
    service = os.popen("systemctl | grep clamd").read()
    if service:
        try:
            print("Start Scan Directory with clamAV")
            scan = os.popen(f"clamscan --infected --recursive --remove {directory}").read()
            return "Scan is Done "
        except:
            return "ERROR on File Scanning with clamAV"
    else:
        return "clamd Service is Down,Start it"



# Text 

def sort_text():
    files = glob.glob(f"{directory}/**/*.txt" , recursive=True)
    if files:
        textdir = os.path.join("/run/media/koosha/1632-930B/Documents/txt") # create Directory
        os.makedirs(textdir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , textdir): # Move Files
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No text Files Found"



# Documents(Microsoft-word & Excel & powerpoint)

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



# Document

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




# PDF

def sort_document_pdf():
    files = glob.glob(f"{directory}/**/*.pdf" , recursive=True)
    if files:
        documentdir = os.path.join("/run/media/koosha/1632-930B/Documents/pdf")
        os.makedirs(documentdir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , documentdir):
                    return "Files Moved "
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No PDF Files Found"

# Powerpoint

def sort_document_powerpoint():
    files = glob.glob(f"{directory}/**/*.ppt" , recursive=True)
    if files:
        documentdir = os.path.join("/run/media/koosha/1632-930B/Documents/ppt")
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
        return "No PowerPoint Files Found"



# Excel

def sort_document():
    files = glob.glob(f"{directory}/**/*.xlsx" , recursive=True)
    if files:
        documentdir = os.path.join("/run/media/koosha/1632-930B/Documents/xlsx")
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
        return "No Excel Files Found"



# Excel

def sort_document():
    files = glob.glob(f"{directory}/**/*.csv" , recursive=True)
    if files:
        documentdir = os.path.join("/run/media/koosha/1632-930B/Documents/csv")
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
        return "No Excel Files Found"





# MultiMedia

def sort_mp3():
    files = glob.glob(f"{directory}/**/*.mp3" , recursive=True)
    if files:
        mp3dir = os.path.join("/run/media/koosha/1632-930B/media/mp3")
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





def sort_mp4():
    files = glob.glob(f"{directory}/**/*.mp4" , recursive=True)
    if files:
        mp4dir = os.path.join("/run/media/koosha/1632-930B/media/mp4")
        os.makedirs(mp4dir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , mp4dir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No mp4 Files Found"


def sort_mkv():
    files = glob.glob(f"{directory}/**/*.mkv" , recursive=True)
    if files:
        mkvdir = os.path.join("/run/media/koosha/1632-930B/media/mkv")
        os.makedirs(mkvdir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , mkvdir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No mkv Files Found"




def sort_avi():
    files = glob.glob(f"{directory}/**/*.avi" , recursive=True)
    if files:
        avidir = os.path.join("/run/media/koosha/1632-930B/media/avi")
        os.makedirs(avidir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , avidir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No avi Files Found"




# Backup Files

def sort_bkf():
    files = glob.glob(f"{directory}/**/*.bkf" , recursive=True)
    if files:
        bkfdir = os.path.join("/run/media/koosha/1632-930B/Backup/bkf")
        os.makedirs(bkfdir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , bkfdir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No Backup Files Found"



def sort_gz():
    files = glob.glob(f"{directory}/**/*.gz" , recursive=True) # Linux Backup Format
    if files:
        gzdir = os.path.join("/run/media/koosha/1632-930B/Backup/gz")
        os.makedirs(gzdir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , gzdir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No Backup Files Found"



# Templates


def sort_html():
    files = glob.glob(f"{directory}/**/*.html" , recursive=True) # Linux Backup Format
    if files:
        htmldir = os.path.join("/run/media/koosha/1632-930B/templates/html")
        os.makedirs(htmldir , exist_ok = True)
        for file in files:
            try:
                if shutil.move(file , htmldir):
                    return "Files Moved"
                else:
                    return "No File Moved"
            except:
                return "All Files Moved or Detect Files in Destination Directory"
    else:
        return "No html Files Found"



# Menu

def print_menu():
    print("choose what you want FS do?")
    print("1.Sort Files with Scan")
    print("2.Sort Files without Scan")
    print("3.Exit")
    return ""


if __name__ == "__main__":
    menu_choice = 0
    words = "Sort Files Simply and Fast:\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    print(print_menu())

    while menu_choice != 3:
        print("Type in your choice:")
        # check if the menu_choice is different from the 3 allowed
        while True:
            try:
                menu_choice = int(input('>'))
            except ValueError:
                pass
            if (menu_choice > 0 or menu_choice < 7):
                break
        if menu_choice == 1:
            if scan():
                print(sort_text())
                print(sort_document())
                print(sort_document_doc())
                print(sort_document_pdf())
                print(sort_document_powerpoint())
                print(sort_mp3())
                print(sort_mp4())
                print(sort_gz())
                print(sort_bkf())
                print(sort_avi())
                print(sort_mkv())
            else:
                print("Error on Executing Scan Function")
        elif menu_choice == 2:
            print("")
        elif menu_choice == 3:
            sys.exit(0)
        else:
            print(print_menU())
 














