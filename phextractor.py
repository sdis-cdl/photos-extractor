import os, shutil

print("photo-extractor")
print("Licence: TBD")
print("2025-11-14 v1.0")
print("================\n")

srcDir  = input("Source path: ")
destDir = input("Destination path: ") + "\\slideshow"

folders = [x for x in os.scandir(srcDir) if x.is_dir() and x.name[0] != '.']

print(f"{len(folders)} folders detected")
# print(folders) #for debugging

fileCount = 0

if not os.path.isdir(destDir):
    os.mkdir(destDir)

for folder in folders:
    exportDir = folder.path + "\\Export"
    if not os.path.isdir(exportDir):
        print(f"Folder {folder.name} has no export folder")
        continue
        
    if os.path.isfile(exportDir + "\\Readme.md"): #if readme is present, photos are internal
        continue

    files = [x for x in os.scandir(exportDir) if x.is_file()]
    fileCount += len(files)
    for file in files:
        shutil.copy2(file.path, f"{destDir}\\{folder.name}_{file.name}")

print(f"{fileCount} images copied")
os.system("pause")
