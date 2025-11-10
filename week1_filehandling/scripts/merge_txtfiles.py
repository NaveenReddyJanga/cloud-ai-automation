import os

source = "./data"
destination = "outputs/merged.txt"

os.makedirs(os.path.dirname(destination),exist_ok = True )

with open(destination,'w',encoding='utf-8') as dest_file:
    for filename in os.listdir(source):
        if filename.endswith('.txt'):
            file_path = os.path.join(source,filename)
            with open(file_path,'r',encoding='utf-8') as src_file:
                contents = src_file.read()
            dest_file.write(f"\n----{filename}-----------\n")
            dest_file.write(f" {contents} \n")

print(f"Merged text files from '{source}' into '{destination}'")    

