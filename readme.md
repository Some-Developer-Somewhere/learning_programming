# Learning Programming

For now, tih repo just contains som simple notes that I can share for creating an overview of how to get into programming.

The main language will be Python, as my opinion is that that language is the best for getting into the basics of programming as it is easy to start with, and ypou can do almost anything with it.

## Setting up the coding environment (python and an editor)

### Installing python

- Download the latest Python 3 version: https://www.python.org/downloads/
- Make sure to select the option to "add to path" (on windows) and then restart machine after installing python.
- VS code is a good and easy code editor to use across many coding languages, so it is a fine pick here as well. It will give you 3 areas on the screen with 1) a file/folder explorer, 2) edit view for an opened file, 3) you can open a terminal window as well.
    - To use VS Code with python, I recommend you install the python extention "Python" (by Microsoft)

### Running python (In the most basic standard way)

Create a text file "program.py" with the following content:

```python
a = 5
b = 7

print(a + b)
```

Open a terminal and make sure the terminal shows the folder path to the folder where the file is (There are several ways to do this).

In the terminal, write the following and press enter:

```
python program.py
```

The following output should now be printed 

Result:
```
12
```

## Overview of the basic functionality of python

### Assigning values to variables and printing to the "terminal"

```python
a = 5
b = 7

print(a + b)
```

Result:
```
12
```

### Arithmetic Operations:

```python
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
exponentiation = a ** b
modulus = a % b
```

### Built-in Data Types:

```python
integer_example = 5
float_example = 3.14
string_example = "Hello"
list_example = [1, 2, 3]
dictionary_example = {'a': 1, 'b': 2}
boolean_example = True
```

Note: Make sure to use float values when dividing to get a "normal" division. You can convert 

### If-else statement:

```python
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
```

Result:
```
a is not greater than b
```

### For-each loop:

```python
a_list = [1,2,3,4,5]

for a_number in a_list:
    print(a_number)
```

Result:
```
1
2
3
4
5
```

### Exception Handling:

```python
try:
    result = 0 / 0
except:
    print("You cannot divide 0 by 0.")
```

Result:
```
You cannot divide 0 by 0.
```

### Basic File Operations (read/write):

```python
some_text = "Hello from file\nThis is a second line"

with open('example.txt', 'w') as file:
    file.write(some_text)

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

Result:
```
Hello from file
This is a second line
```

### Function Definition and Usage:

```python
def greet(name):
    return "Hello " + name

print(greet("Alice"))
```

Result:
```
Hello Alice
```

### Classes:

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

print(f"{person.full_name()} is {person.age} years old.")
```

Result:
```
John Doe is 28 years old.
John Doe is 29 years old.
```


## Examples of using a standard python module "os" to get access to functionality from the OS (Windows/mac/linux)

### Get Current Working Directory:


```python
import os
current_directory = os.getcwd()
print(current_directory)
```

Result:
```
c:\GIT\GitHub_sds\learning_programming
```

### List Directory Contents (folder contents):

```python
import os
items = os.listdir('.')
print(items)
```

Result:
```
['.git', 'example.txt', 'inner_folder', 'Jupyter_notebook_with_examples.ipynb', 'readme.md', 'temp_notes.md']
```

### Join Paths:

```python
import os
folder_path = 'c:\\GIT\\GitHub_sds\\learning_programming'
file_name = 'example.txt'
file_path = os.path.join(folder_path, file_name)
print(file_path)
```

Result:
```
c:\GIT\GitHub_sds\learning_programming\example.txt
```

### Check if Path is a File or Directory:


```python
import os
path = 'example.txt'
print("Is a file:", os.path.isfile(path))
print("Is a directory:", os.path.isdir(path))
```

Result:
```
Is a file: True
Is a directory: False
```

### Change Directory (folder path):

```python
import os
os.chdir('inner_folder')
print("Changed directory to:", os.getcwd())
```

Result:
```
Changed directory to: c:\GIT\GitHub_sds\learning_programming\inner_folder
```