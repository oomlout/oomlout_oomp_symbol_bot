import os
import yaml
import oom_kicad

def load_data():
    github_data = "https://github.com/oomlout/oomlout_oomp_symbol_src"

    #make tmp/data directory if it doesn't already exist
    if not os.path.exists("tmp\\data\\"):
        os.makedirs("tmp\\data\\")
    #clone to tmp/
    os.system("git clone " + github_data + " tmp\\data\\")   

def copy_data():
    print("Copying data")
    directory_src = rf"tmp\data\symbols_flat"
    directory_dst = rf"symbols"
    #copy with directory tree with shutil
    import shutil
    shutil.copytree(directory_src, directory_dst, dirs_exist_ok=True)
    print("Data copied")

def go_through_directories():
    # go through all directories in footprints
    for root, dirs, files in os.walk("symbols"):
        #for each directory
        for name in dirs:
            #go through the files in this directory just one level
            name = name.replace("\\", "/")
            name = f'{name}/working'
            for file in os.listdir(os.path.join(root, name)):
                #if kicad_mod file
                if file.endswith(".kicad_sym"):
                    filename = os.path.join(root, name, file)

                    oom_kicad.generate_outputs_symbol(filename=filename)
            