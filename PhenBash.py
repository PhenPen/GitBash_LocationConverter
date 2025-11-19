"""Phen Converter for GitBash"""
import pyperclip

# Header of program
print("Phen Converter for GitBash")
print("For other Phen Programs, check https://github.com/PhenPen")
print(f"{"*"}"*60)

# Body of program
location = input("Enter location in this format C:/Coding/Pr/.... : ")
locationSlashChange = location.replace("\\","/")
gitBashLocation = "c" + locationSlashChange[1:]
print(gitBashLocation)

# Copy to clipboard
while True:
    clipboardSelect = input("Do you want location copied to clipboard (y/n) : ").upper()
    if clipboardSelect == "Y" :
        pyperclip.copy(gitBashLocation)
        print("Copied to clipboard")
        break
    elif clipboardSelect == "N" :
        print("No copy to clipboard selected")
        break
    else:
        print("Invalid Selection. Try again")




print()
# To end program
input("Press Enter to exit...")