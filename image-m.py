#Working with files

import os
import shutil


picture_path = input("Please Input Picture folder Path: ") 
#'C:/Users/vikra/Desktop/mia1 backup/Camera'
entries = os.listdir(picture_path)

pictures_name_file_path = input("For Storing pictures IDs in a file Please Input path with file name : ") 
 #"C:/Users/vikra/Desktop/mia1 backup/all-pictures.txt"
all_pictures = open(pictures_name_file_path,"w+")
 
pictures_dup_name_path = input("For Storing duplicate pictures IDs in a file Please Input path with file name : ") 
 #"C:/Users/vikra/Desktop/mia1 backup/pictures-dup.txt"
 
duplicate_pictures = open(pictures_dup_name_path,"w+")
 

substring = "("

move_picture_path = input("Input path where you wanna move your dumplicate files")
#'C:/Users/vikra/Desktop/mia1 backup/Camera/duplicate/'
for entry in entries:
   
 if substring in entry :
     duplicate_pictures.write("Image => "+ entry + "\n" )
     shutil.move(picture_path+'/'+entry, move_picture_path)
 else:
     all_pictures.write("Image => "+ entry + "\n" )
   
all_pictures.close
duplicate_pictures.close
 

    
