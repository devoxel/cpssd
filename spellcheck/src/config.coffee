###
# Wand
- Created by Aaron Delaney for a DCU Assignment
~ For details refer to the README in the root of this project
###

# config.coffee
# - contains the Config class

class Config
  # The config class handles all of the constant-like data, as well as defaults
  # for things like edit message, and debug mode.
  constructor: ->
    @debug = true
    @welcome_text = "Welcome to wand"
    @welcome_text_length = 3
    @word_list = []
    @wordlist_url = "https://gist.githubusercontent.com/devoxel/223fcb59b3072884dd0f/raw/552cace09728fae9cbf75df1f314bb893db2289d/10000wordlist.txt"
    @wordlist_request = $.ajax(@wordlist_url,
      cache: true,
      crossDomain: true,
      dataType: "text"
    ).done (data, textStatus, jqXHR) =>
      console.log("Finished downloading wordlist") if @debug
      @word_list = data.split(/\n/)
    @recommend_length = 4 # the amount of reccomended words provided
