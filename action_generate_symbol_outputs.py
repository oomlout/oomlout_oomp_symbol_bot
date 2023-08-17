import oom_kicad
import os


def go_through_directories():
    # go through all directories in footprints
    count = 1
    for root, dirs, files in os.walk("symbols"):
        #for each directory
        for name in dirs:
            if name != "working":
                #go through the files in this directory just one level
                name = name.replace("\\", "/")
                name = f'{name}/working'
                for file in os.listdir(os.path.join(root, name)):
                    #if kicad_mod file
                    #
                    # if file.endswith(".kicad_sym"):  ### was missing ones with depndancies
                    if file.endswith(".yaml"):
                        filter = "nettie"
                        #filter = ""
                        #exclude filter array
                        filter_exclude = "fpga"
                        #if not in filter
                        filename = os.path.join(root, name, file)
                        filename = filename.replace(".yaml", ".kicad_sym")
                        if filter_exclude not in filename.lower():
                            
                            if filter in filename.lower():

                                counter = oom_kicad.generate_outputs_symbol(filename=filename)

                                count += counter
                                #commit to github using oom_kicad after 250 files
                                if count % 250 == 0:
                                    oom_kicad.push_to_git(count=count)
    oom_kicad.push_to_git(count=count)


if __name__ == '__main__':
    go_through_directories()