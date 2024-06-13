# Codebase Consolidator README

## Overview
The `Codebase Consolidator` is a Python script designed to recursively traverse a given directory, collect code files based on specified extensions, and consolidate their contents into a single output file. It is particularly useful for merging multiple source code files for review, analysis, or archival purposes.

## Features
- Traverses directories recursively starting from a specified root directory.
- Collects files with specific extensions.
- Skips specified directories during the traversal.
- Writes the contents of the collected files into a single output file, with file paths clearly indicated.

## Prerequisites
- Python 3.x
- Ensure you have read and write permissions for the directories and files you intend to process.

## Usage

### Script Configuration

1. **Root Directory**: Set the root directory from where the script will start traversing.
   ```python
   root_directory = "C:/path/to/your/root/directory"  # Adjust as needed
   ```

2. **Output Filename**: Specify the path and name of the output file where the consolidated code will be saved.
   ```python
   output_filename = "C:/path/to/your/output/directory/output_file.txt"
   ```

3. **File Extensions**: Define the file extensions that you want to include in the consolidation.
   ```python
   file_extensions = [".py", ".tsx", ".ts", ".js", ".mjs", ".css", ".html"]  # Add file extensions as needed
   ```

4. **Skip Directories**: List the directories that should be skipped during traversal.
   ```python
   skip_directories = ["frontend", "__pycache__", "node_modules", ".next", "staticdir"]  # Directories to skip
   ```

### Running the Script

Run the script using a Python interpreter:
```sh
python path/to/your/script.py
```

### Example

```python
root_directory = "C:/Users/jarem/python-projects/django-goals"  # Adjust as needed
output_filename = "C:/Users/jarem/python-projects/consolidate-codebase/codebase_backend.txt"
file_extensions = [".py", ".tsx", ".ts", ".js", ".mjs", ".css", ".html"]  # Add file extensions as needed
skip_directories = ["frontend", "__pycache__", "node_modules", ".next", "staticdir"]  # Directories to skip

collect_code_files(root_directory, output_filename, file_extensions, skip_directories)
print(f"Code files have been consolidated into {output_filename}")
with open(output_filename, "r", encoding="utf-8") as f:
    print(f"Total characters in the output file: {len(f.read())}")
```

### Script Output
The script will create an output file at the specified location containing the contents of all collected files. Each file's contents are preceded by a header indicating the file path, allowing for easy identification.

Example of output file structure:
```
--- C:/Users/jarem/python-projects/django-goals/app/views.py ---

<content of views.py>

--- C:/Users/jarem/python-projects/django-goals/app/models.py ---

<content of models.py>
```

### Error Handling
- If the root directory does not exist, the script will raise a `FileNotFoundError`.
- The script will print error messages for any files that cannot be read, along with the exception details.

## Contribution
Feel free to fork the repository and submit pull requests. For any issues or feature requests, please open an issue on the repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

This `Codebase Consolidator` script aims to simplify the process of consolidating and reviewing code spread across multiple files and directories. Adjust the configurations as per your project structure and requirements. Happy coding!