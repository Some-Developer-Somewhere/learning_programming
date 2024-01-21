# Install python module streamlit:
# > python -m pip install streamlit
#
# Run this python streamlit application (dont use the "python" command):
# > streamlit run program.py
#
# Use this program/web server:
# It should start your browser automatically with the correct url


# import streamlit as st
# import os
# import pathlib

# if 'current_dir' not in st.session_state:
#     st.session_state.current_dir = pathlib.Path('.')
# if 'file_content' not in st.session_state:
#     st.session_state.file_content = ''

# def list_files(directory):
#     return [f for f in os.listdir(directory) if os.path.isfile(directory / f)]

# def list_files_and_dirs(directory):
#     st.write(f"Current directory: {directory}")
#     for item in os.listdir(directory):
#         item_path = directory / item
#         if item_path.is_dir():
#             if st.button(f"📁 {item}"):
#                 st.session_state.current_dir = item_path

#     st.write("Files in this directory:")
#     for item in os.listdir(directory):
#         item_path = directory / item
#         if item_path.is_file():
#             st.write(f"📄 {item}")

# st.title("File Explorer")

# if st.button('Go to Parent Directory'):
#     st.session_state.current_dir = st.session_state.current_dir.parent

# selected_file = st.selectbox('Select a file', list_files(st.session_state.current_dir))

# if st.button('Open'):
#     file_to_open = st.session_state.current_dir / selected_file
#     with open(file_to_open, 'r') as file:
#         st.session_state.file_content = file.read()

# st.text_area('File content', st.session_state.file_content, height=250)

# if st.button('Save'):
#     file_to_save = st.session_state.current_dir / selected_file
#     with open(file_to_save, 'w') as file:
#         file.write(st.session_state.file_content)

# list_files_and_dirs(st.session_state.current_dir)