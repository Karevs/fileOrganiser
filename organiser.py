#Python File organiser by file extension

import os as os
import glob as gl
import pathlib as pt
import shutil

#path where files will be organised
path1 = r"C:\Users\radek\Downloads"

#path where files that are in need of organisation are 
filePath = r'C:\Users\radek\Downloads\*'

#listing all to be organised files filepaths
listFilePath = gl.glob(filePath)

#lists that prevent continous folder creation
folder_list = []
file_list = []

#to prevent backslash escape
backslash = "\\"

#creates folders with file extensions as folder names
class FolderCreation():
    
    for x in listFilePath:
        
        #reads file extensions
        name, extension = os.path.splitext(x)
        
        #checks for existing directories
        if os.path.isdir(x):
            folder_list.append(x)

        #if prevents unnecessary folder creation
        if (extension not in folder_list) and (extension not in file_list):
            file_list.append(extension)
            directory = "%s"%extension

            #creates folders based on file extensions and in directory of path1
            path2 = os.path.join(path1, directory)
            pt.Path(path2, directory).mkdir(parents=True, exist_ok=True)

#moves files to their appropriate folders per file extension
class FileMoving():
    for x in listFilePath:
        name, extension = os.path.splitext(x)
        if (extension in file_list) and (extension !=''):
            src_path = r"{0}{1}".format(name, extension)
            dst_path = r"{0}{1}{2}".format(path1, backslash, extension)
            shutil.move(src_path, dst_path)

FolderCreation()
FileMoving()
        
print(file_list)
print(folder_list)