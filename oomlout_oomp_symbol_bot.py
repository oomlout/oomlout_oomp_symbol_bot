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

    #go through all readme.md in symbols and reanem readme_src.md
    for root, dirs, files in os.walk("symbols"):
        for file in files:
            #if kicad_mod file
            if file.endswith("readme.md"):
                filename = os.path.join(root, file)
                #rename readme.md to readme_src.md delete any prexisting readme_src first
                if os.path.exists(filename.replace("readme.md", "readme_src.md")):
                    os.remove(filename.replace("readme.md", "readme_src.md"))                
                os.rename(filename, filename.replace("readme.md", "readme_src.md"))



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

def make_readmes():
    # go through all directories in footprints
    for root, dirs, files in os.walk("symbols"):
        #for each directory
        for name in dirs:
            #go through the files in this directory just one level
            name = name.replace("\\", "/")
            name = f'{name}/working'
            for file in os.listdir(os.path.join(root, name)):
                #if kicad_mod file
                if file.endswith("working.yaml"):
                    filename = os.path.join(root, name, file)
                    #make readme
                    make_readme(yaml_file=filename)                 


def make_readme(**kwargs):
    yaml_file = kwargs.get('yaml_file', None)
    #load yanml file into symb
    with open(yaml_file, 'r') as stream:
        symb = yaml.safe_load(stream)
    symbol = symb['symbol']
    repo = symb['repo']
    
    #adding oomp_deets
    oomp_deets = oom_kicad.get_oomp_deets_symbol(symb=symb)


    symb["oomp_deets"] = oomp_deets

    #rename yaml_file from .yaml to _original.yaml
    os.rename(yaml_file, yaml_file.replace(".yaml", "_original.yaml"))
    #dump symb to yaml_file
    with open(yaml_file, 'w') as outfile:
        yaml.dump(symb, outfile, default_flow_style=False)



    







    