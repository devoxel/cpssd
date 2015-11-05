###
Author: Aaron Delaney
Date:   29/10/2015

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
    @wordlist_url = "http://www.mieliestronk.com/corncob_lowercase.txt"
    @wordlist_request = $.ajax(@wordlist_url,
      cache: true,
      crossDomain: true,
      dataType: "text"
    ).done (data, textStatus, jqXHR) =>
      console.log("Finished downloading wordlist") if @debug
      @word_list = data.split(/\n/)
    @recommend_length = 4 # the amount of reccomended words provided
