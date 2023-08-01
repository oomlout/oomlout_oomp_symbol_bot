import oom_kicad
import os


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



if __name__ == '__main__':
    go_through_directories()