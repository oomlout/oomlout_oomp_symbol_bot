import oom_kicad
import os


def go_through_directories():
    # go through all directories in footprints
    count = 1
    for root, dirs, files in os.walk("symbols"):
        #for each directory
        for name in dirs:
            #go through the files in this directory just one level
            name = name.replace("\\", "/")
            name = f'{name}/working'
            for file in os.listdir(os.path.join(root, name)):
                #if kicad_mod file
                if file.endswith(".kicad_sym"):
                    #exclude filter array
                    filter_exclude = "fpga"
                    #if not in filter
                    filename = os.path.join(root, name, file)
                    if filter_exclude not in filename.lower():
                        
                        

                        counter = oom_kicad.generate_outputs_symbol(filename=filename)

                        count += counter
                        #commit to github using oom_kicad after 250 files
                        if count % 2 == 0:
                            oom_kicad.push_to_git()



if __name__ == '__main__':
    go_through_directories()