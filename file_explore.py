import os

def list_files(directory, indent=0):
    try:
        items = os.listdir(directory)
        for item in items:
            print("  " * indent + item)
            path = os.path.join(directory, item)
            if os.path.isdir(path):
                list_files(path, indent + 1)  # Recurse into subdirectories
    except PermissionError:
        pass

list_files(".")

#list_files("C:\temp\")
