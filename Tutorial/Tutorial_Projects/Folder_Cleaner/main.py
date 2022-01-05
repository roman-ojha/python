from genericpath import isfile
import os

# here in this project we are trying to clean or organize the file

files=os.listdir()
files.remove("main.py")
# return all of the main root file avilabel 
# print(files)

def createDir(folder):
    if not os.path.exists(folder):
        # here we are creating the folder if doesn't exist
        os.makedirs(folder)

# Moving all of the files in the corrosponding folder

def moveFile(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")
# for video in videos:
#     os.replace(video,f"Video/{video}")


if __name__ == "__main__":
    # os.removedirs("Media")
    # this will remove dir
    createDir("Images")
    createDir("Docs")
    createDir("Music")
    createDir("Video")
    createDir("Others")
    # this is crate the directory


    imgExts=[".png",".jpg",".jpeg"]
    images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    # here this will return all the img file related to .png, .jpg, .jpeg
    # here we are using for loop and if condition to check the file extention and getting it in the form of list
    # print(images)

    docsExts=[".txt",".docx",".doc",".pdf",".pptx",".xls"]
    document=[file for file in files if os.path.splitext(file)[1].lower() in docsExts]
    # here this will return all the document file related to  ".txt",".docx",".doc",".pdf",".pptx",".xls"
    # print(document)

    musicExts=[".mp3",".wav"]
    musics=[file for file in files if os.path.splitext(file)[1].lower() in musicExts]
    # print(music)


    videoExts=[".mp4"]
    videos=[file for file in files if os.path.splitext(file)[1].lower() in videoExts]
    # print(video)


    others=[]

    for file in files:
        ext= os.path.splitext(file)[1].lower()
        if (ext not in docsExts) and (ext not in musicExts) and (ext not in imgExts) and (ext not in videoExts) and os.path.isfile(file):
            others.append(file)

    print(others)

    moveFile("Music",musics)
    moveFile("Video",videos)
    moveFile("Images",images)
    moveFile("Docs",document)
    moveFile("Others",others)