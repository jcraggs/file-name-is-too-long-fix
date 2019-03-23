""" A quick fix for files that are too long to use in windows7/8"""
import os
import tkinter as tk
import subprocess

def main():
    """Main program"""
    origin_path = dir_select()
    selected_file = file_select(origin_path)
    new_folder_path = create_folder()
    copy_file(origin_path, selected_file, new_folder_path)


def dir_select():
    """Getting the user to select the folder in which the file is located"""
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    print("\nPlease select the folder directory where the file is located")
    origin_directory = filedialog.askdirectory()
    print("\nSelected directory path:")
    origin_path = os.path.realpath(origin_directory)
    print(origin_path + "\n")
    return origin_path


def file_select(origin_path):
    """Getting the user to select the file they want"""
    rolling_number = 1
    for root, dirs, files in os.walk(origin_path, topdown=True):
        dirs.clear()
        for file in files:
            print(str(rolling_number) + ") " + file)
            rolling_number += 1

    file_num = input("\nType the number of the file you wish to copy: ")
    selected_file = files[int(file_num)-1]
    print(selected_file + "\n")
    return selected_file


def create_folder():
    """Creates a temp_folder on the users desktop"""
    new_folder_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\temp_folder')
    try:
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
    except OSError:
        print("Error: Creating directory: " + new_folder_path)
    return new_folder_path


def copy_file(origin_path, selected_file, new_folder_path):
    """Copies the selected file into the new temp_folder"""
    subprocess.call(['cmd', '/c', 'robocopy', origin_path, new_folder_path, selected_file], shell=True)
    input("\n"+ '"' + selected_file + '"' + " has been copied to the temp_folder on your desktop. \nPress any key to exit ")


if __name__ == "__main__":
    main()
