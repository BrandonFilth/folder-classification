from PIL import Image
import os

downloadsFolder = "/Users/brand/Downloads/"
picturesFolder = "/Users/brand/Downloads/Imag/"
videosFolder = "/Users/brand/Downloads/Videos/"
compFolder = "/Users/brand/Downloads/Comp/"
programFolder = "/Users/brand/Downloads/Programs/"
musicFolder = "/Users/brand/Downloads/Music/"
docFolder = "/Users/brand/Downloads/Docs/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            os.rename(downloadsFolder + filename, picturesFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp3"]: 
            os.rename(downloadsFolder + filename, musicFolder + filename)
            print(name + ": " + extension)

        if extension in [".mp4", ".3gp"]:
            os.rename(downloadsFolder + filename, videosFolder + filename)
            print(name + ": " + extension)

        if extension in [".pdf", ".docx", ".txt"]:    
            os.rename(downloadsFolder + filename, docFolder + filename)
            print(name + ": " + extension)

        if extension in [".zip"]:  
            os.rename(downloadsFolder + filename, compFolder + filename)
            print(name + ": " + extension)

        if extension in [".c", ".exe"]:   
            os.rename(downloadsFolder + filename, programFolder + filename)
            print(name + ": " + extension)
