import os



def main():
    #rename_folders()
    lower_case_folders()


def lower_case_folders():
    for root, dirs, files in os.walk("symbols"):
        #for each directory
        for name in dirs:
            #rename the lower case version
            new_name = name.lower()
            os.rename(os.path.join(root, name), os.path.join(root, new_name))



    
    
    
def rename_folders():
    #go through all directories in symbols/
    for root, dirs, files in os.walk("symbols"):
        #for each directory
        for name in dirs:
            #go through the files in this directory just one level
            remove_strings = ["kicad_library_","libraries_kicad_symbols_"]
            for remove_string in remove_strings:
                #rename the directory by remoiving remove_string
                if remove_string in name:
                    new_name = name.replace(remove_string, "")
                    os.rename(os.path.join(root, name), os.path.join(root, new_name))
                    name = new_name
                    pass


    





if __name__ == '__main__':
    main()
