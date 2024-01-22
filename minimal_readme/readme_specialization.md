# Learning Programming Specialization (Using a module for a specific "domain")

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