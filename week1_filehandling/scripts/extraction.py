import os  # it is a module to interact with the operating system
import shutil # it is a module to use copy files

source= "data" 
destination = "outputs/txt_files"  

os.makedirs(destination, exist_ok=True) # create destination folder if it doesn't exist

for filename in os.listdir(source): # looping through files in source folder
    if filename.endswith('.txt'): # only pics with .txt extension
        src_path = os.path.join(source , filename) # the address of source file you want to copy
        dest_path = os.path.join(destination, filename) # the address of destination where you want to copy the file    
        shutil.copy(src_path, dest_path) # copy the file from source to destination
        print(f"Copied: {filename} to {destination}")

print("File extraction completed.")
