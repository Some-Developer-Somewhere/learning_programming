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


if 'current_dir' not in st.session_state:
    st.session_state.current_dir = pathlib.Path('.')
if 'files_list' not in st.session_state:
    st.session_state.files_list = []
if 'file_content' not in st.session_state:
    st.session_state.file_content = ''


def change_directory(path):
    os.chdir(path)
    st.rerun()

def list_dirs_and_create_navigation(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            if st.button(f"📁 {item}"):
                st.session_state.current_dir = item_path
                change_directory(st.session_state.current_dir)

def list_and_return_files_list(directory):
    files_list = []
    items = os.listdir('.')
    for file_or_folder in items:
        if os.path.isfile(file_or_folder):
            st.write(file_or_folder)
            files_list.append(file_or_folder)
    st.session_state.files_list = files_list


st.title("File Explorer and editor")

path = os.getcwd()

st.write(path)

if st.button(f"Go to parent folder"):
    change_directory("..")

st.header("Folders:")
list_dirs_and_create_navigation(path)

st.header("Files:")
list_and_return_files_list(path)



st.header("Edit:")
files_list = st.session_state.files_list
selected_file = st.selectbox('Select a file', files_list)

opened_file_content = ''
opened_file = ''
if st.button('Open'):
    file_to_open = st.session_state.current_dir / selected_file
    with open(file_to_open, 'r') as file:
        opened_file_content = file.read()
        st.session_state.file_content = opened_file_content
        opened_file = file_to_open

st.write(opened_file)

st.session_state.file_content = st.text_area("File content:", st.session_state.file_content, height=400)

no_file_content = len(st.session_state.file_content) == 0
no_change_in_file_content = st.session_state.file_content == opened_file_content

if st.button('Save', disabled=no_file_content or no_change_in_file_content):
    file_to_save = st.session_state.current_dir / selected_file
    with open(file_to_save, 'w') as file:
        file.write(st.session_state.file_content)

