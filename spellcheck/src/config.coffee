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
    @wordlist_url = "https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt"
    @wordlist_request = $.ajax(@wordlist_url,
      cache: true,
      crossDomain: true,
      dataType: "text"
    ).done (data, textStatus, jqXHR) =>
      console.log("Finished downloading wordlist") if @debug
      @word_list = data.split(/\n/)
    @length_of_reccomends = 4 # the amount of reccomended words provided
