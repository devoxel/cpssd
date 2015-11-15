###
Author: Aaron Delaney

Find more details in spellcheck/README.md
###

# config.coffee
# -------------------
# Contains:
# - the Config class

class Config
  # The config class handles all of the constant-like data, as well as defaults
  # for things like edit message, and debug mode.
  # It also handles the AJAX request for the wordlist
  constructor: ->
    @debug = true
    @welcome_text = "Welcome to wand"
    @welcome_text_length = 3
    @word_list = []

    @bktree = undefined
    @wordset = undefined

    # Max tolerence greatly changes the speed of the lookup time
    # however it reduces the results for very badly mispelled text
    @max_tolerence = 2
    # The wordlist also greatly changes speed, particulary of load time
    # to decrease the load and query time, change medium.txt to small.txt
    @wordlist_url = "https://raw.githubusercontent.com/devoxel/octo_wordlist/master/medium.txt"
    # ASSIGNMENT RELATED VARIABLES
    @spellcheck_types = ['min_edit', 'kernighan']
    @current_type = @spellcheck_types[0]
    @recommend_length = 4 # the amount of reccomended words provided
