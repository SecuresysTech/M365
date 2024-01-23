'''
This short script helps to search for all PST files present on your local system.
PST files contain emails that are linked to Microsoft Outlook, which are often required 
when you migrate emails from one tenant to another via the PST route'''

import os

folder = input("Enter the directory to be searched: ")

for root, dirs, files in os.walk(folder):  # utilizes builtin walk method to iterate through each file and subdirectory
    for file in files:
        if file.endswith('.pst'):  # specifies file type
            try:
                location = os.path.abspath(os.path.join(root, file))  # Stores path for current file within loop
                size = os.stat(location).st_size  # returns file size in bytes
                print("Name: " + file)
                print("Location: " + location)
                print("Size: " + str(size // 1000) + ' kbs ' + str(size // 1000000) + ' mbs\n')
            except:
                print("An Error occurred trying to access the file, " + file)
