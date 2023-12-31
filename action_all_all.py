import tmp.data.oomlout_oomp_symbol_src.oomlout_oomp_symbol_src as oomlout_oomp_symbol_src
import action_setup
import action_generate_symbol_outputs
import action_generate_image_resolutions
import action_generate_readmes

import os



def main(**kwargs):
    import time
    start_time = time.time()
    # src portion

    test=True
    test=False
    kwargs["test"] = test
    #kwargs["repo_filter"] = "oomlout"
    kwargs["repo_filter"] = ""

    #kwargs["filter"] = "filter"
    kwargs["filter"] = ""
    dir_src = "tmp/data/oomlout_oomp_symbol_src"
    dir_base = "tmp/data/oomlout_oomp_symbol_src"
    kwargs["dir_src"] = dir_src
    kwargs["dir_base"] = dir_base
    import oom_git
    oom_git.pull(directory=dir_src)
    
    #also make the library
    oomlout_oomp_symbol_src.clone_and_copy_symbols(**kwargs)
    
    oomlout_oomp_symbol_src.make_symbols_readme(**kwargs)
    
    cwd = os.getcwd()
    #commit src
    oom_git.push_to_git(directory=dir_src)
    #commit all symbol library
    dir_all_symbols = f"{dir_src}/tmp/generated/oomlout_oomp_symbol_all_the_kicad_symbols"
    oom_git.push_to_git(directory=dir_all_symbols)
    
    # bot portion

    action_setup.main()

    import oom_git
    oom_git.push_to_git()

    #action_generate_symbol_outputs.main()
    action_generate_readmes.main()
    #this has git commits in it
    action_generate_image_resolutions.main()

    oom_git.push_to_git()

    end_time = time.time()
    end_time_hours_minutes_seconds = time.strftime("%H:%M:%S", time.gmtime(end_time - start_time))
    print(f"total time: {end_time_hours_minutes_seconds}")


if __name__ == '__main__':
    main()