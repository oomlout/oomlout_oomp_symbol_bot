# oomlout_oomp_symbol_bot

## getting running

* run action_setup.py
* add the symols to symbol library ( tmp\data\symbols_all_the_symbols_one_library )
* open up a symbol editor window
* open up a symbol to test
* run action_generate_symbol_outputs.py 

## actions

* action_setup -- pulls in src and sets up everything required
* action_generate_symbol_outputs.py -- generate all the outputs for every kicad_sym file

## knowin issues

* all symbols with a '-' or other no alphanumberic charachters aren't having their outputs properly generated
