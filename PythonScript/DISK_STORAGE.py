import shutil

def print_disk_storage(path="/"):
    """Prints the disk storage details for the specified path."""
    total, used, free = shutil.disk_usage(path)

    print(f"Disk Storage Details for {path}:")
    print(f"Total: {total / (1024**3):.2f} GB")
    print(f"Used: {used / (1024**3):.2f} GB")
    print(f"Free: {free / (1024**3):.2f} GB\n")

# Example usage
print_disk_storage("C:/")
print_disk_storage("D:/")