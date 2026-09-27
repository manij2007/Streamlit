import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PyPDF2 import PdfReader
import sqlite3
from datetime import datetime

HTML_BANNER_HOME = """
    <div style = "background-color : #464e5f; padding : 3px; border : 10px;">
    <h1 style = "color : white; text-align : center;">Metadata Extracter</h1>
    </div>
"""

HTML_BANNER_IMAGE = """
    <div style = "background-color : #464e5f; padding : 3px; border : 10px;">
    <h1 style = "color : white; text-align : center;">Image Metadata Extraction</h1>
    </div>
"""

HTML_BANNER_AUDIO = """
    <div style = "background-color : #464e5f; padding : 3px; border : 10px;">
    <h1 style = "color : white; text-align : center;">Audio Metadata Extraction</h1>
    </div>
"""

HTML_BANNER_DOCUMENT = """
    <div style = "background-color : #464e5f; padding : 3px; border : 10px;">
    <h1 style = "color : white; text-align : center;">Document Metadata Extraction</h1>
    </div>
"""

HTML_BANNER_ANALYTICS = """
    <div style = "background-color : #464e5f; padding : 3px; border : 10px;">
    <h1 style = "color : white; text-align : center;">Analytics and Monitor</h1>
    </div>
"""

### DataBase
conn = sqlite3.connect("Database.db")
cur = conn.cursor()
def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS Filestable(Filename TEXT , Filetype TEXT , Filesize TEXT , Upload_data TIMESTAMP)")
def add_file(Filename , Filetype , Filesize , Upload_data):
    cur.execute("INSERT INTO Filestable(Filename , Filetype , Filesize , Upload_data) VALUES (? , ? , ? , ?)" , (Filename , Filetype , Filesize , Upload_data))
    conn.commit()
def view_all_data():
    cur.execute("SELECT * FROM Filestable")
    data = cur.fetchall()
    return data

def main():
    choice = st.sidebar.selectbox(label = "Menu" , options = ["Home" , "Image" , "Audio" , "Document" , "Analytics"])
    create_table()
    if choice == "Home":
        stc.html(html = HTML_BANNER_HOME)
        col1 , col2 , col3 = st.columns(spec = 3)
        with col1:
            with st.expander("Image Metadata"):
                st.info("Image Metadata")
                st.text("Upload JPG , PNG , JPEG")
        with col2:
            with st.expander("Audio Metadata"):
                st.info("Audio Metadata")
                st.text("Upload MP3 , OGG , WAV")   
        with col3:
            with st.expander("Document Metadata"):
                st.info("Document Metadata")
                st.text("Upload PDF")

    elif choice == "Image":
        stc.html(html = HTML_BANNER_IMAGE)
        image_file = st.file_uploader(label = "Upload Image" , type = ["PNG" , "JPG" , "JPEG"])
        if image_file is not None:
            with st.expander("File Status"):
                st.info("File Status")
                file_details = {"Filename" : image_file.name , "Filesize" : image_file.size , "Filetype" : image_file.type}
                st.write(file_details)
                add_file(image_file.name , image_file.type , image_file.size , datetime.now())
            col1 , col2 = st.columns(spec = 2)
            with col1:
                with st.expander("View Image"):
                    st.info("View Image")
                    img = Image.open(image_file)
                    st.image(img)
            with col2:
                with st.expander("Image Details"):
                    st.info("Image Details")
                    img = Image.open(image_file)
                    img_details = {
                        "Format" : img.format , 
                        "Format_desc" : img.format_description , 
                        "Size" : img.size , 
                        "Height" : img.height , 
                        "Width" : img.width , 
                        "Info" : img.info
                    }
                    df = pd.DataFrame(list(img_details.items()) , columns = ["Meta Tag" , "Value"])
                    st.dataframe(df)

    elif choice == "Audio":
        stc.html(html = HTML_BANNER_AUDIO)
        audio_file = st.file_uploader(label = "Upload Audio" , type = ["mp3" , "ogg" , "wav"])
        if audio_file is not None:
            col1 , col2 = st.columns(spec = 2)
            with col1:
                st.audio(audio_file.read())
            with col2:
                with st.expander("File Status"):
                    st.info("File Status")
                    file_details = {"Filename" : audio_file.name , "Filesize" : audio_file.size , "Filetype" : audio_file.type}
                    st.write(file_details)
                    add_file(audio_file.name , audio_file.type , audio_file.size , datetime.now())

    elif choice == "Document":
        stc.html(html = HTML_BANNER_DOCUMENT)
        doc_file = st.file_uploader(label = "Upload Document" , type = ["PDF"])
        if doc_file is not None:
            col1 , col2 = st.columns(spec = 2)
            with col1:
                with st.expander("File Status"):
                    st.info("File Status")
                    file_details = {"Filename" : doc_file.name , "Filesize" : doc_file.size , "Filetype" : doc_file.type}
                    st.write(file_details)
                    add_file(doc_file.name , doc_file.type , doc_file.size , datetime.now())
            with col2:
                with st.expander("Metadata with PdfFileReader"):
                    st.info("Reading one page")
                    pdf_file = PdfReader(doc_file)
                    st.write(pdf_file.pages[0].extract_text())
                    
    else:
        stc.html(html = HTML_BANNER_ANALYTICS)
        all_upload_data = view_all_data()
        df = pd.DataFrame(all_upload_data , columns = ["Filename" , "Filetype" , "Filesize" , "Upload_time"])
        with st.expander("Monitor"):
            st.success("View all Uploaded files")
            st.dataframe(df)
        with st.expander("Distribution of Filetypes"):
            st.info("Distribution of Filetypes")
            fig = plt.figure()
            sns.countplot(data = df , x = "Filetype" , hue = "Filetype")
            st.pyplot(fig)
            
if __name__ == "__main__":
    main()