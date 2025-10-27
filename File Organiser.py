import os
from pathlib import Path
import shutil



def SortingDocuments(path):
    with (os.scandir(path) as items):
        for item in items:
            if item.name.endswith((".pdf",".xlsx",".docx",".txt")):
                pdfs = path / "PDFs"
                docx = path / "DOCXs"
                xlsx = path / "XLSXs"
                txt = path / "TXTs"
                pdfs.mkdir(exist_ok=True)
                docx.mkdir(exist_ok=True)
                xlsx.mkdir(exist_ok=True)
                txt.mkdir(exist_ok=True)
                with os.scandir(path) as arrangements:
                    for entry in arrangements:
                        name = entry.name
                        name_lower = name.lower()
                        if name_lower.endswith(".pdf"):
                            shutil.move(os.path.join(path, name),os.path.join(pdfs,name))
                        elif name_lower.endswith(".docx"):
                            shutil.move(os.path.join(path, name), os.path.join(docx,name))
                        elif name_lower.endswith(".xlsx"):
                            shutil.move(os.path.join(path, name), os.path.join(xlsx,name))
                        else:
                            continue



print("Welcome to CLI PYTHON FILE ORGANISER")

main_dir = input("Enter the Folder path you want organised : ")
rep_dir1 = Path(main_dir + "/Downloaded images")
rep_dir2 = Path(main_dir + "/Downloaded documents")
rep_dir1.mkdir(exist_ok=True)
rep_dir2.mkdir(exist_ok=True)


with os.scandir(main_dir) as entries:
    for entry in entries:
        name = entry.name
        name_lower = name.lower()
        if name_lower.endswith(".docx") or name_lower.endswith(".pdf") or name_lower.endswith((".xlsx",".txt")):
            shutil.move(os.path.join(main_dir, name), os.path.join(rep_dir2, name))
        elif name_lower.endswith((".jpg",".jpeg",".jpeg",".png",".heic")):
            shutil.move(os.path.join(main_dir, name), os.path.join(rep_dir1, name))
        else:
            continue

print("First stage of sorting Completed!")
print(" ")

while True:
    option = input("Enter YES if you want DOCUMENT files further sorted according to types, else NO : ").upper()
    if option == "YES":
        SortingDocuments(rep_dir2)
        print("Completed!! Thank You.")
        break
    elif option == "NO":
        print("Thank You!")
        break
    else:
        print("Invalid input, PLease Try Again")








