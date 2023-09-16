import tmp.data.oomlout_oomp_symbol_src.oomlout_oomp_symbol_src as oomlout_oomp_symbol_src
import action_setup
import action_generate_symbol_outputs
import action_generate_image_resolutions
import action_generate_readmes
import oom_git



def main(**kwargs):
    import time
    #time_start 
    test=False
    dir_src = "tmp/data/oomlout_oomp_symbol_src"
    oom_git.pull(directory=dir_src)
    oomlout_oomp_symbol_src.clone_and_copy_symbols(test=test, dir_base="tmp/data/oomlout_oomp_symbol_src")
    oomlout_oomp_symbol_src.make_symbols_readme()
    dir_all_symbols = "tmp/data/oomlout_oomp_symbol_all_the_kicad_symbols"
    #oom_git.push_to_git(directory=dir_all_symbols)
    action_setup.main()

    action_generate_symbol_outputs.main()
    action_generate_readmes.main()
    action_generate_image_resolutions.main()


if __name__ == '__main__':
    main()