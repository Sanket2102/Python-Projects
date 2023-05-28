import os
from shutil import move

# Stored our source path in a variable where sorting will be done
source = "D:\Downloads"

# Paths for different file formats

videosrc = "D:\Downloads\Songs and Videos"
docssrc = "D:\Downloads\Documents"
notebooksrc = "D:\Downloads\Jupyter notebooks"
exesrc = "D:\Downloads\Applications"
zipsrc = "D:\Downloads\Zips"

# Stored all the files in our source folder in a list
dirList = os.listdir(source)

# Assigned different extention type to the folder paths 

ext_dict = {'mp4':videosrc,'mp3':videosrc,'amr':videosrc,'wav':videosrc,'mkv':videosrc,
            'pdf':docssrc,'docx':docssrc,'txt':docssrc,'csv':docssrc,'xlsx':docssrc,'pptx':docssrc,
            'ipynb':notebooksrc,'py':notebooksrc,
            'exe':exesrc,'iso':exesrc,
            'zip':zipsrc,'rar':zipsrc}

# For loop to iterate through every item in our source folder
for i in dirList:
    # If the file don't have a '.' in it, it is a folder so we will skip that iteration
    if '.' in i:
        list = i.split('.')  # Splitted the item on every occurence of '.'
        ext = list[-1] # The extention will always be the last item in our list so we store it in a variable
        temp = os.path.join(source,i) # We get the file path by joining it to the source path
        move(temp,ext_dict[ext]) # Moved the file to the destined folder by comparing its extention to our extention dictionary containing folder paths for each type
