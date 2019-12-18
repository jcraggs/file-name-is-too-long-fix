# file-name-is-too-long-fix
A python script which copies files rendered inaccessible by the Windows 7/8 max directory path limit, to a temporary folder on the user’s desktop thus shortening the overall file directory length, allowing them to be accessed.

Note: Computers with Windows 10 installed have the ability to enable ‘NTFS Long paths’ which means these systems can handle much longer file directory lengths. If you have Windows 10 installed enabelling ‘NTFS Long paths’ will be a better fix.

## What causes the "file name is too long" error in the first place?
The reason the error occurs on Windows 7/8 is because for these operating system versions the maximum length for a directory path is set to 260 characters. If you exceed this 260-character limit you cannot access the file or perform any actions on it.

Fortunately, command line operations have a max path length of 8191 characters, so we can perform actions on the file via the command line and get it in to a directory length that windows 7/8 can handle. In this instance the file is pasted to a temp_folder on the user’s desktop.

## What does this program do? 
The script works in four stages:
* Stage 1: Gets the user to select the folder in which the file is located.
* Stage 2: Displays the files within the selected folder in the python terminal and gets the user to select the specific file they want by entering the attributed number of the file in the command line.
* Stage 3: Creates a temporary folder (called "temp_folder") on the users desktop.
* Stage 4: Utilises all of the inputs from the previous 3 stages and copies the selected file into the new "temp_folder" via subprocess robocopy.


## Help: The file name is still too long after being copied to the desktop
Note if the filename is still too long to access after being copied to the users desktop (means it'll be >200 characters), then you'll need to rename the file to something shorter.

You can do this through the directory:

* Step 1) Open your command prompt with the start menu then navigate to the newly created folder by typing `cd Desktop\temp_folder` and pressing enter. 

You can check to see which files are in the current directory by typing `dir` and then pressing enter.

* Step 2) Type `rename {current directory}\filename newfilename` and press enter. 

**Where:**

-`{current directory}` is the directory file path to the temp_folder on your desktop (should be something like "C:\Users\YOUR NAME\Desktop\temp_folder"

-`\filename` is the name of the file you want to access, i.e. the one you just copied across. 

-`newfilename` is what you want to call the new file e.g "hello_world.txt". Make sure to keep the file format tag (e.g. .txt, .docx, .jpg etc) when you rename the file. 

Note: The file name is case sensitive and any spaces in the file name must be contained within quotation marks like so: “ ”

* Step 3) When you press enter after the rename command you should not receive any errors and now should be able to view the file.

Getting an error message? You have to make sure that what you type matches the directory exactly , if you don’t it’s likely that the command line will state “The system cannot find the file specified".
