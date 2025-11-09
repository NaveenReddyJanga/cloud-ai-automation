import os

folder = "data"
for count, filename in enumerate(os.listdir(folder), start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f"file_{count}{ext}"
    os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

print("Files renamed successfully.")

