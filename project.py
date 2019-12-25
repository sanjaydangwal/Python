import os,shutil
documents = ('.pdf','.docx','.csv')
image = ('.jpg','png')
video = ('.mp4')
python = ('.py')

folder = input("enter path   ")
get_files(folder,documents)

def get_files(folder_path,files_extension):
    files = []
    for items in os.listdir(folder_path):
        for extension in files_extension:
            if items.endswith(extension):
                files.append(folder_path +"/"+items)
    print(files)