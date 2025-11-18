## Phen Converter for GitBash

A simple utility that converts standard Windows file paths into Git Bash compatible paths and optionally copies the converted path to your clipboard.
  
## What This Tool Does

Accepts a Windows path like:

C:\Coding\Pr\MyFolder


Converts it automatically into Git Bash format like:

c:/Coding/Pr/MyFolder


Allows you to instantly copy the converted path to your clipboard for quick use in terminals or scripts.

## Installation

Make sure Python is installed on your system.

Install the required module:

pip install pyperclip


Download or clone the project:

git clone https://github.com/PhenPen/phen-converter.git

## Usage

Run the script using:

python main.py


You will be prompted to enter a location in this format:

C:/Coding/Pr/Folder


The tool will then:

Convert backslashes (\\) to forward slashes (/)

Change the drive letter to Git Bash format

Display the Git Bash ready path

Ask whether to copy it to the clipboard (Y/N)

##  Running the EXE Version

This project also includes a standalone Windows executable (`gitbash_LocationConverter.exe`).

You can run it without installing Python:

1. Download the EXE from the repository  .
2. Double-click `gitbash_LocationConverter.exe`.
3. Enter your Windows path when prompted.
4. Choose whether to copy the converted Git Bash path to your clipboard.

No installation or dependencies required for the exe version.


Example

Input:

C:\Users\Phen\Desktop\TestFolder


Output:

c:/Users/Phen/Desktop/TestFolder


If you choose “Y”, this output will be copied to your clipboard.

## Requirements (For only the python script and not the exe)

Python 3.x

pyperclip module

## Contributing

Contributions are welcome!
Submit an issue or a pull request on GitHub.

## Other Phen Utilities

Check out more tools at:
https://github.com/PhenPen
