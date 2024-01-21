
## Arithmetic Operations:

```python
addition = 3 + 4
subtraction = 5 - 2
multiplication = 6 * 7
division = 8 / 4
modulus = 9 % 4
exponentiation = 2 ** 3
Built-in Data Types:
```


```python
integer_example = 5
float_example = 3.14
string_example = "Hello"
list_example = [1, 2, 3]
tuple_example = (4, 5, 6)
set_example = {7, 8, 9}
dictionary_example = {'a': 1, 'b': 2}
boolean_example = True
```


## Control Flow Statements:

If-else statement:


```python
if a > b:
    # code if true
else:
    # code if false
```

### For-each loop:

```python
for item in iterable:
    # code for each item
```


## Function Definition and Usage:

```python
def greet(name):
    return "Hello " + name

print(greet("Alice"))
```

## Exception Handling:

```python
try:
    result = 0 / 0
except ZeroDivisionError:
    print("You cannot divide 0 by 0.")
```

## Basic File Operations:

```python
with open('example.txt', 'w') as file:
    file.write("Hello from file\nThis is a second line")

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```


## Classes:

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def run_birthday(self):
        self.age += 1

person = Person("John", "Doe", 28)
print(f"{person.full_name()} is {person.age} years old.")
person.run_birthday()
print(f"Now, {person.full_name()} is {person.age} years old.")
```


## Using Imported Modules (os module):

### Get Current Working Directory:


```python
import os
current_directory = os.getcwd()
print(current_directory)
```


### List Directory Contents:


```python
import os
items = os.listdir('.')
print(items)
```

### Join Paths:

```python
import os
full_path = os.path.join('folder', 'file.txt')
print(full_path)
```


### Check if Path is a File or Directory:


```python
import os
path = 'example.txt'
print("Is a file:", os.path.isfile(path))
print("Is a directory:", os.path.isdir(path))
```


### Change Directory:


```python
import os
os.chdir('new_directory')
print("Changed directory to:", os.getcwd())
```


## Using Python Streamlit:



```python
import streamlit as st

# Initialize the count in session state if not already present
if 'count' not in st.session_state:
    st.session_state.count = 0

st.title("Counter")

# Increment count when the button is pressed
if st.button('Count'):
    st.session_state.count += 1

st.write(f"Current Count: {st.session_state.count}")
```


## Using Python Flask:



```python
from flask import Flask

app = Flask(__name__)

@app.route('/<int:number>')
def hello_number(number):
    return f'Hello, world {number}'

if __name__ == '__main__':
    app.run()
```


## Combinations of Functionality - Streamlit and os Module:

### A)

```python
import streamlit as st
import os
import pathlib

if 'current_dir' not in st.session_state:
    st.session_state.current_dir = pathlib.Path('.')

def list_files_and_dirs(directory):
    st.write(f"Current directory: {directory}")
    for item in os.listdir(directory):
        item_path = directory / item
        if item_path.is_dir():
            if st.button(f"📁 {item}"):
                st.session_state.current_dir
```

### B)

```python
import streamlit as st
import os
import pathlib

if 'current_dir' not in st.session_state:
    st.session_state.current_dir = pathlib.Path('.')
if 'file_content' not in st.session_state:
    st.session_state.file_content = ''

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(directory / f)]

def list_files_and_dirs(directory):
    st.write(f"Current directory: {directory}")
    for item in os.listdir(directory):
        item_path = directory / item
        if item_path.is_dir():
            if st.button(f"📁 {item}"):
                st.session_state.current_dir = item_path

    st.write("Files in this directory:")
    for item in os.listdir(directory):
        item_path = directory / item
        if item_path.is_file():
            st.write(f"📄 {item}")

st.title("File Explorer")

if st.button('Go to Parent Directory'):
    st.session_state.current_dir = st.session_state.current_dir.parent

selected_file = st.selectbox('Select a file', list_files(st.session_state.current_dir))

if st.button('Open'):
    file_to_open = st.session_state.current_dir / selected_file
    with open(file_to_open, 'r') as file:
        st.session_state.file_content = file.read()

st.text_area('File content', st.session_state.file_content, height=250)

if st.button('Save'):
    file_to_save = st.session_state.current_dir / selected_file
    with open(file_to_save, 'w') as file:
        file.write(st.session_state.file_content)

list_files_and_dirs(st.session_state.current_dir)
```

