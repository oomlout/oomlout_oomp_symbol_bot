import os
import shutil

def main():
    directory_doc = "c:/gh/oomlout_oomp_symbol_doc"
    #if directory doesn't exist, create it
    if not os.path.exists(directory_doc):
        os.makedirs(directory_doc)
    #recursively go through all files in the symbols directory
    for root, dirs, files in os.walk("symbols"):
        #for every file
        for file in files:
            full_file = os.path.join(root, file)
            #replace \\ with /
            full_file = full_file.replace("\\", "/")
            src = full_file
            file_slashes = full_file.replace("_", "/")
            dst = os.path.join(directory_doc, file_slashes)
            #replace \\ with /
            dst = dst.replace("\\", "/")
            #copy and overwrite if there using shutil
            #if directories don't exist create them
            if not os.path.exists(os.path.dirname(dst)):
                os.makedirs(os.path.dirname(dst))
            shutil.copyfile(src, dst)
            







if __name__ == '__main__':
    main()