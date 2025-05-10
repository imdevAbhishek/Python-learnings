import os

# Specify the directory path
directory_path = '/'  # Current directory

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print the entries
print(f"Contents of '{directory_path}':")
for entry in entries:
    print(entry)
