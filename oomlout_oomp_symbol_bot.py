import os
import yaml
import oom_kicad
import oom_git

import oom_markdown

def load_data():
    github_datas = []
    github_datas.append("https://github.com/oomlout/oomlout_oomp_symbol_src")
    github_datas.append("https://github.com/oomlout/oomlout_oomp_symbol_all_the_kicad_symbols")

    for github_data in github_datas:

        #make tmp/data directory if it doesn't already exist
        if not os.path.exists("tmp\\data\\"):
            os.makedirs("tmp\\data\\")
        #clone to tmp/
        oom_git.clone(repo=github_data, directory="tmp\\data\\")
        dir_full  = os.path.join("tmp\\data\\", github_data.split("/")[-1])
        oom_git.pull(directory=dir_full)

def copy_data():
    print("Copying data")
    directory_src = rf"tmp\data\oomlout_oomp_symbol_src\symbols_flat"
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
                    #make_readme(yaml_file=filename)                 


def make_readme_old(**kwargs):
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


def generate_readme(**kwargs):
    
    overwrite = kwargs.get("overwrite",False)
    filename = kwargs.get("filename",None)
    #get directory from filename
    directory = os.path.dirname(filename) 
    readme_file = os.path.join(directory,"readme.md")
    print(f"generating readme for {directory}")
    #create a deep copy of kwargs
    import copy
    p2 = copy.deepcopy(kwargs)
    p2["directory"] = directory
    readme = get_readme(**p2)

    #write readme file
    #as unicode
    with open(readme_file, 'w', encoding='utf-8') as text_file:
        text_file.write(readme)


def get_readme(**kwargs):
    directory = kwargs.get("directory","none")

    readme = "# OOMP Symbol  \n"
    import copy
    p2 = copy.deepcopy(kwargs)
    yaml_file = p2.get("directory", "none") + "\\working.yaml"
    if os.path.exists(yaml_file):
        import yaml
        with open(yaml_file, 'r') as stream:
            try:
                yaml_dict = yaml.load(stream, Loader=yaml.FullLoader)
            except:
                print("yaml file error")
                readme += "yaml file error"
                return readme
        #if yaml dict is a list then take the first element
        if isinstance(yaml_dict, list):
            yaml_dict = yaml_dict[0]
        
        p2["yaml_dict"] = yaml_dict
        p2["readme"] = readme
        readme += get_intro(**p2)
        ###### footprint
        p2["readme"] = readme
        readme += get_symbol(**p2)
        ###### images
        p2["readme"] = readme
        readme += get_images(**p2)



        return readme
    else:
        print( "no yaml file found")
        readme += "no yaml file found"
        return readme

def get_intro(**kwargs):
    yaml_dict = kwargs.get("yaml_dict",None)
    yd = yaml_dict
    name = yd.get("name","none")
    owner = yd.get("owner","none")
    library_name = yd.get("library_name","none")
    oomp_key = yd.get("oomp_key","none")
    repo = yd.get("repo","none")
    repo_link = ""
    if repo != "none":
        repo_link = repo.get("url","none")
        ###### introduction
    readme = ""
    readme += f'## {name}  by {owner}  \n'
    readme += f'  \n'
    readme += f'oomp key: {oomp_key}  \n'
    readme += f'  \n'
    repo_link_link = oom_markdown.get_link(link=repo_link)
    readme += f'source repo at: {repo_link_link}  \n'

    return readme

def get_symbol(**kwargs):
    yaml_dict = kwargs.get("yaml_dict",None)
    yd = yaml_dict
    directory = kwargs.get("directory","none")
    name = yd.get("library_name","none")
    owner = yd.get("library_owner","none")
    library_name = yd.get("library_name","none")
    oomp_key = yd.get("oomp_key","none")
    links = yd.get("links","none")
    oomp_bot_github = ""
    if links != "none":
        oomp_bot_github = links.get("oomp_bot_github","none")

    readme = "## Symbol  \n"
    ###### board
    image_link = oom_markdown.get_link_image_scale(image="working.png",resolution="600")
    readme += f'  \n'
    readme += f'{image_link}  \n'
    symbol_filename = f'{directory}/working.kicad_mod'
    #oom_kicad.get_footprint_pin_names(filename=footprint_filename)
    table_array = []
    table_array.append(["symbol name", name])
    table_array.append(["library name", library_name])
    table_array.append(["oomp key", oomp_key])
    table_array.append(["oomp bot github", oomp_bot_github])
    readme+=oom_markdown.get_table(data=table_array)

    return readme

def get_images(**kwargs):
    
    directory = kwargs.get("directory","none")
    readme = "## Images  \n"

    #get all images in directory
    import glob
    images = glob.glob(directory + "\\*.png")
    images += glob.glob(directory + "\\*.jpg")
    images += glob.glob(directory + "\\*.jpeg")
    for image in images:
        #grab the filename split after the last _
        test = image.split("_")[-1]
        digit_test = test[1:3].isdigit()
        if not digit_test:
            just_filename = os.path.basename(image)
            image_link = oom_markdown.get_link_image_scale(image=just_filename)

            readme += f'  \n'
            readme += f'{image_link}  \n'





    return readme
    







    