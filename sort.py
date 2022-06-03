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
        try:
            textdir = os.path.join(f"{directory}/Documents/txt") # create Directory
            os.makedirs(textdir , exist_ok = True)
            for file in files:
                shutil.move(file , textdir) # Move Files
                print("Text File Moving is Done")
        except:
            print(f"ERROR on File Saving,This might be Same File in {textdir}")
    else:
        return "No text Files Found"



# Documents(Microsoft-word & Excel & powerpoint)

def sort_document():
    files = glob.glob(f"{directory}/**/*.docx" , recursive=True)
    if files:
        try:
            documentdir = os.path.join(f"{directory}/Documents/docx")
            os.makedirs(documentdir , exist_ok = True)
            for file in files:
                shutil.move(file , documentdir)
                print(f"All docx Files Moved to {documentdir}")
        except:
                print("ERROR on File Saving,This might be Same File in {textdir}")
    else:
        return "No docx document Files Found"



# Document

def sort_document_doc():
    files = glob.glob(f"{directory}/**/*.doc" , recursive=True)
    if files:
        try:
            documentdir = os.path.join(f"{directory}/Documents/doc")
            os.makedirs(documentdir , exist_ok = True)
            for file in files:
                shutil.move(file , documentdir)
                print("Files Moving Done")
        except:
                print(f"All Files Moved or Detect Files in {documentdir}")
    else:
        return "No document Files Found"




# PDF

def sort_document_pdf():
    files = glob.glob(f"{directory}/**/*.pdf" , recursive=True)
    if files:
        try:
            documentdir = os.path.join(f"{directory}/Documents/pdf")
            os.makedirs(documentdir , exist_ok = True)
            for file in files:
                shutil.move(file , documentdir)
                print("all pdf Files Moved ")
        except:
            print(f"All Files Moved or Detect Files in {documentdir}")
    else:
        return "No PDF Files Found"



# Powerpoint

def sort_document_powerpoint():
    files = glob.glob(f"{directory}/**/*.ppt" , recursive=True)
    if files:
        try:
            documentdir = os.path.join(f"{directory}/Documents/ppt")
            os.makedirs(documentdir , exist_ok = True)
            for file in files:
                shutil.move(file , documentdir)
                print(f"powerpoint Files Moved to {documentdir}")
        except:
            print(f"All Files Moved or Detect Files in {documentdir}")
    else:
        return "No PowerPoint Files Found"



# Excel

def sort_document():
    files = glob.glob(f"{directory}/**/*.xlsx" , recursive=True)
    if files:
        try:
            documentdir = os.path.join(f"{directory}/Documents/xlsx")
            os.makedirs(documentdir , exist_ok = True)
            for file in files:
                shutil.move(file , documentdir)
                print(f"xlsx Files Moved to {documentdir}")
        except:
            print(f"All Files Moved or Detect Files in {documentdir}")
    else:
        return "No Excel Files Found"



# Excel

def sort_document():
    files = glob.glob(f"{directory}/**/*.csv" , recursive=True)
    if files:
        try:
            documentdir = os.path.join(f"{directory}/Documents/csv")
            os.makedirs(documentdir , exist_ok = True)
            for file in files:
                shutil.move(file , documentdir)
                print(f"all csv Files is Moved to {documentdir}")
        except:
            print(f"All Files Moved or Detect Files in {documentdir}")
    else:
        return "No Excel Files Found"





# MultiMedia

def sort_mp3():
    files = glob.glob(f"{directory}/**/*.mp3" , recursive=True)
    if files:
        try:
            mp3dir = os.path.join(f"{directory}/media/mp3")
            os.makedirs(mp3dir , exist_ok = True)
            for file in files:
                shutil.move(file , mp3dir)
                print(f"All mp3 Files Moved to {mp3dir}")
        except:
            print("All Files Moved or Detect Files in Destination Directory")
    else:
        return f"No mp3 Files Found in {mp3dir}"





def sort_mp4():
    files = glob.glob(f"{directory}/**/*.mp4" , recursive=True)
    if files:
        try:
            mp4dir = os.path.join(f"{directory}/media/mp4")
            os.makedirs(mp4dir , exist_ok = True)
            for file in files:
                shutil.move(file , mp4dir)
                print(f"All Mp4 Files Moved to {mp4dir}")
        except:
            print(f"All Files Moved or Detect Files in {mp4dir}")
    else:
        return "No mp4 Files Found"


def sort_mkv():
    files = glob.glob(f"{directory}/**/*.mkv" , recursive=True)
    if files:
        try:
            mkvdir = os.path.join(f"{directory}/media/mkv")
            os.makedirs(mkvdir , exist_ok = True)
            for file in files:
                shutil.move(file , mkvdir)
                print(f"Files Moved")
        except:
            print(f"All Files Moved or Detect Files in {mkvdir}")
    else:
        return "No mkv Files Found"




def sort_avi():
    files = glob.glob(f"{directory}/**/*.avi" , recursive=True)
    if files:
        try:
            avidir = os.path.join(f"{directory}/media/avi")
            os.makedirs(avidir , exist_ok = True)
            for file in files:
                shutil.move(file , avidir)
                print(f"Files Moved to {avidir}")
        except:
                print(f"All Files Moved or Detect same Files in {avidir}")
    else:
        return "No avi Files Found"




# Backup Files

def sort_bkf():
    files = glob.glob(f"{directory}/**/*.bkf" , recursive=True)
    if files:
        try:
            bkfdir = os.path.join(f"{directory}/Backup/bkf")
            os.makedirs(bkfdir , exist_ok = True)
            for file in files:
                shutil.move(file , bkfdir)
                print("Files Moved")
        except:
            print(f"All Files Moved or Detect Files in {bkfdir}")
    else:
        return "No Backup Files Found"



def sort_gz():
    files = glob.glob(f"{directory}/**/*.gz" , recursive=True) # Linux Backup Format
    if files:
        try:
            gzdir = os.path.join(f"{directory}/Backup/gz")
            os.makedirs(gzdir , exist_ok = True)
            for file in files:
                shutil.move(file , gzdir)
                print(f"Files Moved to {gzdir}")
        except:
            print(f"All Files Moved or Detect Files in {gzdir}")
    else:
        return "No Backup Files Found"



# Templates


def sort_html():
    files = glob.glob(f"{directory}/**/*.html" , recursive=True) # Linux Backup Format
    if files:
        try:
            htmldir = os.path.join("/run/media/koosha/1632-930B/templates/html")
            os.makedirs(htmldir , exist_ok = True)
            for file in files:
                shutil.move(file , htmldir)
                print(f"Files Moved to {htmldir}")
        except:
            print(f"All Files Moved or Detect Files in {htmldir}")
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
 














