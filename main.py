
import streamlit as st
from pathlib import Path
import shutil
import os

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


def main():
    st.set_page_config(page_title="File Sorter", page_icon="🗂️", layout="centered")

    # Sidebar content
    st.sidebar.title("📘 Instructions")
    st.sidebar.markdown("""
        1. Paste the full folder path (e.g. `C:/Users/xxxx/Downloads`)
        2. Click **Continue** to start organising
        3. Then choose if you want further document sorting
        """)
    st.sidebar.markdown("---")


    st.title("📂Personal File Organiser")
    

    file_path = st.text_input("Enter Your File Path")
    button = st.button("Continue")

    #First Stage Sorting
    if button:
        main_dir = file_path
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
        st.success("First Stage of Sorting Complete")

        st.session_state["rep_dir2"] = str(rep_dir2)

    #Second Stage Sorting
    if "rep_dir2" in st.session_state:
        st.subheader("Second Stage Sorting of Documents")
        option = st.text_input("Enter 'yes' for further sorting, else 'no' : ",
                               key="doc_sort_input").upper()
        option_button = st.button("Continue", key="option_button")
        if option_button:
            if option == "YES":
                SortingDocuments(Path(st.session_state["rep_dir2"]))
                st.success("Completed!! Thank You.")
            elif option == "NO":
                st.subheader("Thank You!")
            elif option:
                st.warning("Invalid input, PLease Try Again")



main()




