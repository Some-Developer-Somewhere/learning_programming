# Install python module streamlit:
# > python -m pip install streamlit
#
# Run this python streamlit application (dont use the "python" command):
# > streamlit run program.py
#
# Use this program/web server:
# It should start your browser automatically with the correct url

import streamlit as st
import os
import pathlib


def change_directory(path):
    os.chdir(path)
    st.rerun()

def list_dirs(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if st.button(f"📁 {item}"):
                st.session_state.current_dir = item_path
                change_directory(st.session_state.current_dir)

def list_files(directory):
    items = os.listdir('.')
    for file_or_folder in items:
        if os.path.isfile(file_or_folder):
            st.write(file_or_folder)

if 'current_dir' not in st.session_state:
    st.session_state.current_dir = pathlib.Path('.')

st.title("File Explorer")

path = os.getcwd()

st.write(path)

if st.button(f"Go to parent folder"):
    change_directory("..")

st.header("Folders:")
list_dirs(path)

st.header("Files:")
list_files(path)

