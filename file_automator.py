import os
import shutil
from pathlib import Path


def organize_by_extension(folder_path):
    """Organize files into folders by their extension"""
    folder = Path(folder_path)
    
    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower().strip(".")
            if not ext:
                ext = "no_extension"
            
            target_dir = folder / ext
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(file), str(target_dir / file.name))
            print(f"Moved: {file.name} → {ext}/")
    
    print("\nDone! Files organized.")


def bulk_rename(folder_path, prefix="file"):
    """Rename all files with a numbered prefix"""
    folder = Path(folder_path)
    
    for i, file in enumerate(sorted(folder.iterdir()), 1):
        if file.is_file():
            new_name = f"{prefix}_{i:03d}{file.suffix}"
            file.rename(folder / new_name)
            print(f"Renamed: {file.name} → {new_name}")


def find_duplicates(folder_path):
    """Find duplicate files by size"""
    folder = Path(folder_path)
    sizes = {}
    duplicates = []
    
    for file in folder.rglob("*"):
        if file.is_file():
            size = file.stat().st_size
            if size in sizes:
                duplicates.append((file, sizes[size]))
            else:
                sizes[size] = file
    
    return duplicates


if __name__ == "__main__":
    path = input("Enter folder path: ")
    print("\n1. Organize by extension")
    print("2. Bulk rename")
    print("3. Find duplicates")
    choice = input("\nChoice: ")
    
    if choice == "1":
        organize_by_extension(path)
    elif choice == "2":
        prefix = input("Enter prefix: ")
        bulk_rename(path, prefix)
    elif choice == "3":
        dupes = find_duplicates(path)
        for d in dupes:
            print(f"Duplicate: {d[0]} = {d[1]}")
