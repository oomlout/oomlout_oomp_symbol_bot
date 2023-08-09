import os
import shutil
import oom_base

def main():
    directory_doc = "c:/gh/oomlout_oomp_symbol_doc"
    #if directory doesn't exist, create it
    if not os.path.exists(directory_doc):
        os.makedirs(directory_doc)
    #recursively go through all files in the symbols directory
    for root, dirs, files in os.walk("symbols"):
        #for every file
        for file in files:
            if "working.yaml" in file:
                directory = root.replace("\\", "/")

                src = os.path.join(root, file)
                src = src.replace("\\", "/")

                yaml_file = f'{directory}/{file}'
                yaml_file = yaml_file.replace("\\", "/")
                #load yaml file
                import yaml
                with open(yaml_file) as f:
                    yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
                owner = yaml_dict.get("owner", "")
                library = yaml_dict.get("library_name", "")
                library = library.lower()
                #replace special characters using oom_base
                library = oom_base.remove_special_characters(library)
                
                symbol_name = yaml_dict.get("name", "")
                symbol_name = symbol_name.replace(f"{library}_", "")

                dst = f"c:/gh/oomlout_oomp_symbol_doc/symbols/{owner}/{library}/{symbol_name}"

                #copy all files in source directory inclusion subfodlers to dst directory using shutil
                print(f"Copying {src} to {dst}")
                shutil.copytree(directory, dst, dirs_exist_ok=True)


                pass
                
            







if __name__ == '__main__':
    main()