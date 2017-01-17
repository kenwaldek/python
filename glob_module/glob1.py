from glob import glob
import os

# drie jpegs in de map die zo gestructureerd waren
# 212121211-1.jpg, 5454545-2.jpg
# omzetten naar jpeg zonder die cijferzooi links van - streep

pathFromUser = input("Enter the Path")
files_list = glob(os.path.join(pathFromUser, '*.jpg'))
for each_file in files_list:
    number = os.path.basename(each_file).split("-")[1].split(".")[0]
    os.rename(each_file, number + ".jpg")

# dit verandert alle jpegs naar 1,2,3 jpg enz zie map

