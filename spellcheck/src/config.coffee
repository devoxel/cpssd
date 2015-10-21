###
# Wand
Created by Aaron Delaney for a DCU Assignment

Refer to README for more information
###

# config.coffee
# - contains the Config class

class Config
  constructor: ->
    @debug = true
    @welcome_text = "Welcome to wand"
    @word_regex = /[\ ,\.\!\;\?]|<br>/
    @word_list = []
    @wordlist_url = "https://raw.githubusercontent.com/sindresorhus/word-list/master/words.txt"
    @wordlist_request = $.ajax(@wordlist_url,
      cache: true,
      crossDomain: true,
      dataType: "text"
    ).done (data, textStatus, jqXHR) =>
      console.log("Finished downloading wordlist") if @debug
      @word_list = data.split(/\n/)
    @length_of_reccomends = 4
