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
    @wordlist_url = "https://raw.githubusercontent.com/devoxel/octo_wordlist/master/large.txt"
    @wordlist_request = $.ajax(@wordlist_url,
      cache: true,
      crossDomain: true,
      dataType: "text"
    ).done (data, textStatus, jqXHR) =>
      console.log("Finished downloading wordlist") if @debug
      @word_list = data.split(/\n/)

    # ASSIGNMENT RELATED VARIABLES
    @spellcheck_types = ['min_edit', 'kernighan']
    @current_type = @spellcheck_types[0]
    @recommend_length = 4 # the amount of reccomended words provided
