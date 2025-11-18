location = input("Enter location : ")
locationSlashChange = location.replace("\\","/")
gitBashLocation = "c" + locationSlashChange[1:]
print(gitBashLocation)