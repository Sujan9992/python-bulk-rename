import os


def rename_files(folder_path: str, prefix: str) -> None:
    """
    Rename files in a folder with a given prefix.
    """
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Get a list of files in the folder
    files: list[str] = os.listdir(folder_path)

    # Iterate through each file and rename it
    for index, file_name in enumerate(files):
        # Construct the new file name
        new_file_name: str = f"{prefix}_{index+1}{os.path.splitext(file_name)[1]}"

        # Construct the full paths for old and new names
        old_file_path: str = os.path.join(folder_path, file_name)
        new_file_path: str = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)

        print(f"Renamed '{file_name}' to '{new_file_name}'")


def check_folder_path(path: str) -> bool:
    return os.path.exists(path)


if __name__ == "__main__":
    while True:
        # Folder path where the files are located
        folder_path: str = input("Enter the folder path:\n")
        if not check_folder_path(folder_path):
            print(f"Folder '{folder_path}' does not exist.")
            continue
        else:
            break

    # Prefix to be added to each file name
    prefix: str = input("Enter the prefix to be added:\n")

    # Call the function to rename files
    rename_files(folder_path, prefix)
