import os


def collect_code_files(root_dir, output_file, extensions=None, skip_dirs=None):
    if not os.path.exists(root_dir):
        raise FileNotFoundError(f"Directory not found: {root_dir}")

    if extensions is None:
        extensions = [".py"]  # Adjust as needed

    if skip_dirs is None:
        skip_dirs = ["frontend", "__pycache__", "node_modules", ".next", "staticdir"]  # Default skip directories

    with open(output_file, "w", encoding="utf-8") as out_file:
        for subdir, _, files in os.walk(root_dir):
            print(f"Processing subdir {subdir}")
            if any(skip_dir in subdir for skip_dir in skip_dirs):
                print(f"SUBDIR {subdir} SKIPPED")
                continue
            for file in files:
                print(f"Found file {file}")
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(subdir, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as in_file:
                            print(f"Processing {file_path}")
                            file_content = in_file.read()
                            out_file.write(f"\n\n--- {file_path} ---\n\n")
                            out_file.write(file_content)
                            print(f"Written content of {file_path}")
                    except Exception as e:
                        print(f"Failed to read {file_path}: {e}")


root_directory = ""  # Adjust as needed
output_filename = ""
file_extensions = [".py", ".tsx", ".ts", ".js", ".mjs", ".css", ".html"]  # Add file extensions as needed
skip_directories = ["frontend", "__pycache__", "node_modules", ".next", "staticdir"]  # Directories to skip

collect_code_files(root_directory, output_filename, file_extensions, skip_directories)
print(f"Code files have been consolidated into {output_filename}")
with open(output_filename, "r", encoding="utf-8") as f:
    print(f"Total characters in the output file: {len(f.read())}")
